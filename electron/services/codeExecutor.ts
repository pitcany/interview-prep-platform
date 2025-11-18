import { spawn } from 'child_process';
import * as path from 'path';
import * as fs from 'fs';
import * as os from 'os';
import * as crypto from 'crypto';

interface TestCase {
  input: any;
  expectedOutput: any;
}

interface ExecutionResult {
  status: 'passed' | 'failed' | 'error' | 'timeout';
  testResults: TestResult[];
  executionTime: number;
  memoryUsed: number;
  errorMessage?: string;
}

interface TestResult {
  passed: boolean;
  input: any;
  expectedOutput: any;
  actualOutput: any;
  executionTime: number;
  error?: string;
}

export class CodeExecutorService {
  private tempDir: string;
  private pythonServicePath: string;
  private maxExecutionTime: number = 10000; // 10 seconds
  private maxMemory: number = 512; // 512 MB
  private usePythonService: boolean = false;
  private pythonWrapperTemplate: string;

  constructor(userDataPath?: string) {
    // Use userDataPath/code-exec instead of /tmp to avoid Docker mount issues
    const baseDir = userDataPath || os.tmpdir();
    this.tempDir = path.join(baseDir, 'code-exec');
    this.pythonServicePath = path.join(__dirname, '../../python-service');

    // Use Python service if SANDBOX_MODE is 'local', otherwise use Docker
    this.usePythonService = process.env.SANDBOX_MODE === 'local';

    // Load Python wrapper template
    const templatePath = path.join(__dirname, '../templates/python_wrapper.template.py');
    this.pythonWrapperTemplate = fs.readFileSync(templatePath, 'utf-8');
  }

  async initialize() {
    // Create temp directory if it doesn't exist
    if (!fs.existsSync(this.tempDir)) {
      fs.mkdirSync(this.tempDir, { recursive: true });
    }

    // Check if Python service is available
    const testRunnerPath = path.join(this.pythonServicePath, 'test_runner.py');
    if (this.usePythonService && !fs.existsSync(testRunnerPath)) {
      this.usePythonService = false;
    }
  }

  async executeCode(
    code: string,
    language: string,
    testCases: TestCase[]
  ): Promise<ExecutionResult> {
    // Validate language parameter
    const validLanguages = ['python', 'java', 'cpp'];
    if (!validLanguages.includes(language)) {
      throw new Error(`Invalid language: ${language}`);
    }

    // Validate code size
    if (!code || code.length === 0) {
      throw new Error('Code cannot be empty');
    }

    if (code.length > 100000) { // 100KB limit
      throw new Error('Code size exceeds maximum allowed (100KB)');
    }

    // Use Python service for local execution (faster, supports only Python)
    if (this.usePythonService && language === 'python') {
      return this.executeWithPythonService(code, testCases);
    }

    // Use Docker for all other cases
    const startTime = Date.now();
    const testResults: TestResult[] = [];

    try {
      // Execute each test case
      for (const testCase of testCases) {
        const result = await this.executeTestCase(code, language, testCase);
        testResults.push(result);
      }

      const allPassed = testResults.every(r => r.passed);
      const totalTime = Date.now() - startTime;
      const avgMemory = testResults.reduce((sum, r) => sum + (r as any).memoryUsed || 0, 0) / testResults.length;

      return {
        status: allPassed ? 'passed' : 'failed',
        testResults,
        executionTime: totalTime,
        memoryUsed: Math.round(avgMemory),
      };
    } catch (error: any) {
      return {
        status: 'error',
        testResults,
        executionTime: Date.now() - startTime,
        memoryUsed: 0,
        errorMessage: error.message,
      };
    }
  }

  private async executeWithPythonService(
    code: string,
    testCases: TestCase[]
  ): Promise<ExecutionResult> {
    return new Promise((resolve, _reject) => {
      const testRunnerPath = path.join(this.pythonServicePath, 'test_runner.py');

      const inputData = JSON.stringify({
        code,
        testCases,
        language: 'python',
        timeout: this.maxExecutionTime / 1000, // Convert to seconds
        maxMemory: this.maxMemory,
      });

      const pythonProcess = spawn('python3', [testRunnerPath]);

      // Write input data to stdin instead of command line args to avoid size limits
      pythonProcess.stdin.write(inputData);
      pythonProcess.stdin.end();

      let stdout = '';
      let stderr = '';

      const timeout = setTimeout(() => {
        pythonProcess.kill();
        resolve({
          status: 'timeout',
          testResults: [],
          executionTime: this.maxExecutionTime,
          memoryUsed: 0,
          errorMessage: 'Code execution timed out',
        });
      }, this.maxExecutionTime + 2000); // Extra buffer

      pythonProcess.stdout.on('data', (data) => {
        stdout += data.toString();
      });

      pythonProcess.stderr.on('data', (data) => {
        stderr += data.toString();
      });

      pythonProcess.on('error', (_error) => {
        // Error handled in close handler
      });

      pythonProcess.on('close', (code) => {
        clearTimeout(timeout);

        if (code !== 0 && !stdout) {
          resolve({
            status: 'error',
            testResults: [],
            executionTime: 0,
            memoryUsed: 0,
            errorMessage: stderr || `Process exited with code ${code}`,
          });
          return;
        }

        try {
          const result = JSON.parse(stdout);

          // Convert snake_case to camelCase for compatibility
          const formattedResult: ExecutionResult = {
            status: result.status,
            testResults: result.test_results || [],
            executionTime: result.execution_time || 0,
            memoryUsed: result.memory_used || 0,
            errorMessage: result.error_message || undefined,
          };

          resolve(formattedResult);
        } catch (error) {
          resolve({
            status: 'error',
            testResults: [],
            executionTime: 0,
            memoryUsed: 0,
            errorMessage: `Failed to parse output: ${stdout}`,
          });
        }
      });

      pythonProcess.on('error', (error) => {
        clearTimeout(timeout);
        resolve({
          status: 'error',
          testResults: [],
          executionTime: 0,
          memoryUsed: 0,
          errorMessage: error.message,
        });
      });
    });
  }

  private async executeTestCase(
    code: string,
    language: string,
    testCase: TestCase
  ): Promise<TestResult> {
    const startTime = Date.now();

    try {
      const result = await this.runInSandbox(code, language, testCase);
      const executionTime = Date.now() - startTime;

      // Compare output
      const passed = this.compareOutputs(result.output, testCase.expectedOutput);

      return {
        passed,
        input: testCase.input,
        expectedOutput: testCase.expectedOutput,
        actualOutput: result.output,
        executionTime,
      };
    } catch (error: any) {
      return {
        passed: false,
        input: testCase.input,
        expectedOutput: testCase.expectedOutput,
        actualOutput: null,
        executionTime: Date.now() - startTime,
        error: error.message,
      };
    }
  }

  private async runInSandbox(
    code: string,
    language: string,
    testCase: TestCase
  ): Promise<{ output: any; memoryUsed: number }> {
    // Create a temporary file for the code using crypto random
    const randomId = crypto.randomBytes(16).toString('hex');
    const fileName = `code_${randomId}${this.getFileExtension(language)}`;
    const filePath = path.join(this.tempDir, fileName);
    
    // Prepare code with test case
    const fullCode = this.prepareCodeWithTestCase(code, language, testCase);
    fs.writeFileSync(filePath, fullCode);

    try {
      const result = await this.executeInDocker(filePath, language);
      return result;
    } finally {
      // Cleanup
      if (fs.existsSync(filePath)) {
        fs.unlinkSync(filePath);
      }
    }
  }

  private extractMethodName(code: string, language: string): string {
    if (language === 'python') {
      // Extract method name from Solution class
      // Look for pattern: def methodName(self, or def methodName(self)
      // This regex handles multi-line class definitions with various whitespace
      const methodMatch = code.match(/class\s+Solution\s*:[\s\S]*?def\s+(\w+)\s*\(\s*self\s*,?/);
      if (methodMatch && methodMatch[1]) {
        return methodMatch[1];
      }

      // Try to find any method in Solution class with more flexible matching
      // Handle cases where class Solution might be on a different line
      const classStartIndex = code.indexOf('class Solution');
      if (classStartIndex !== -1) {
        const afterClass = code.substring(classStartIndex);
        // Match method definition after class, allowing for whitespace and comments
        const methodMatch = afterClass.match(/def\s+(\w+)\s*\(\s*self\s*,?/);
        if (methodMatch && methodMatch[1]) {
          return methodMatch[1];
        }
      }

      // Common LeetCode method names as fallback - check if they exist in code
      const commonMethods = [
        'twoSum', 'threeSum', 'maxProfit', 'findMedianSortedArrays',
        'lengthOfLongestSubstring', 'longestPalindrome', 'reverse',
        'myAtoi', 'isMatch', 'maxArea', 'intToRoman', 'romanToInt',
        'longestCommonPrefix', 'isValid', 'mergeTwoLists', 'removeDuplicates',
        'search', 'searchInsert', 'plusOne', 'addBinary', 'mySqrt',
        'climbStairs', 'deleteDuplicates', 'merge', 'isSameTree',
        'isSymmetric', 'maxDepth', 'levelOrder', 'sortedArrayToBST',
        'inorderTraversal', 'preorderTraversal', 'postorderTraversal',
        'hasPathSum', 'minDepth', 'isBalanced', 'flatten', 'connect',
        'buildTree', 'numIslands', 'cloneGraph', 'canFinish', 'findOrder'
      ];

      // Check if any common method exists in the code
      // Look for "def methodName(" pattern (with or without self parameter)
      for (const method of commonMethods) {
        // Escape special regex characters in method name
        const escapedMethod = method.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        const methodPattern = new RegExp(`def\\s+${escapedMethod}\\s*\\(`);
        if (methodPattern.test(code)) {
          return method;
        }
      }

      // Last resort: try to find any method in Solution class
      // Look for any method definition after "class Solution"
      const solutionClassMatch = code.match(/class\s+Solution[^:]*:([\s\S]*?)(?=\n\s*class|\n\n|$)/);
      if (solutionClassMatch) {
        const classBody = solutionClassMatch[1];
        const anyMethodMatch = classBody.match(/def\s+(\w+)\s*\(/);
        if (anyMethodMatch && anyMethodMatch[1] && anyMethodMatch[1] !== '__init__') {
          return anyMethodMatch[1];
        }
      }

      // Last resort: return empty string to trigger fallback logic in wrapper code
      // The wrapper code will use introspection to find any method
      return '';
    }

    // For other languages, return 'solve' as fallback
    return 'solve';
  }

  private prepareCodeWithTestCase(code: string, language: string, testCase: TestCase): string {
    const inputStr = JSON.stringify(testCase.input);
    const methodName = this.extractMethodName(code, language);
    // Escape code for embedding in Python string
    const escapedCode = code.replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, '\\n');

    switch (language) {
      case 'python':
        // Use template with placeholder substitution
        return this.pythonWrapperTemplate
          .replace('{{USER_CODE}}', code)
          .replace(/\{\{TEST_INPUT\}\}/g, inputStr.replace(/'/g, "\\'"))
          .replace(/\{\{ESCAPED_CODE\}\}/g, escapedCode)
          .replace(/\{\{METHOD_NAME\}\}/g, methodName);

      case 'java':
        // For Java, read input from stdin and use reflection to call the method
        // This approach works for most LeetCode-style problems
        return `
import com.google.gson.*;
import java.util.*;
import java.io.*;

${code}

public class Solution {
    public static void main(String[] args) {
        try {
            // Read input from stdin
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            String input = reader.readLine();

            Gson gson = new Gson();
            Object[] inputArray = gson.fromJson(input, Object[].class);

            Solution sol = new Solution();

            // Find the first public method that's not main
            java.lang.reflect.Method targetMethod = null;
            for (java.lang.reflect.Method m : sol.getClass().getDeclaredMethods()) {
                if (!m.getName().equals("main") &&
                    java.lang.reflect.Modifier.isPublic(m.getModifiers())) {
                    targetMethod = m;
                    break;
                }
            }

            if (targetMethod == null) {
                System.out.println("{\\"error\\": \\"No public method found in Solution class\\"}");
                return;
            }

            // Convert input array to proper argument types
            Class<?>[] paramTypes = targetMethod.getParameterTypes();
            Object[] args = new Object[paramTypes.length];

            for (int i = 0; i < paramTypes.length && i < inputArray.length; i++) {
                args[i] = convertType(inputArray[i], paramTypes[i], gson);
            }

            // Invoke method and print result
            Object result = targetMethod.invoke(sol, args);
            System.out.println(gson.toJson(result));

        } catch (Exception e) {
            System.out.println("{\\"error\\": \\"" + e.toString() + "\\"}");
        }
    }

    private static Object convertType(Object value, Class<?> targetType, Gson gson) {
        if (value == null) return null;
        if (targetType.isAssignableFrom(value.getClass())) return value;

        // Convert using Gson for complex types
        String json = gson.toJson(value);
        return gson.fromJson(json, targetType);
    }
}
`;

      case 'cpp':
        // For C++, we provide a main function that reads JSON input from stdin
        // and provides helper functions for parsing common types
        // Note: This is a simplified approach - C++ requires compile-time types
        return `
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
using namespace std;

${code}

// Helper function to convert json to vector<int>
vector<int> jsonToVectorInt(const json& j) {
    vector<int> result;
    for (const auto& item : j) {
        result.push_back(item.get<int>());
    }
    return result;
}

// Helper function to convert json to vector<vector<int>>
vector<vector<int>> jsonToVector2DInt(const json& j) {
    vector<vector<int>> result;
    for (const auto& row : j) {
        vector<int> rowVec;
        for (const auto& item : row) {
            rowVec.push_back(item.get<int>());
        }
        result.push_back(rowVec);
    }
    return result;
}

int main() {
    try {
        // Read input from stdin
        string input_line;
        getline(cin, input_line);

        json input = json::parse(input_line);

        Solution sol;
        json result;

        // For C++ we need to know the method signature at compile time
        // This is a limitation - for now, we provide a simple interface
        // Users can modify this main() function based on their method signature

        // Example: For twoSum(vector<int>& nums, int target)
        if (input.is_array() && input.size() >= 2) {
            if (input[0].is_array() && input[1].is_number()) {
                auto nums = jsonToVectorInt(input[0]);
                int target = input[1].get<int>();
                // Note: This assumes method name extracted is used
                // For now, we'll try common patterns

                // Attempt to call method - this is a placeholder
                // Real implementation would need method detection
                auto output = sol.${methodName || 'twoSum'}(nums, target);
                result = output;
            } else {
                result = "Error: Input format not supported for C++ auto-detection";
            }
        } else {
            result = "Error: Input must be an array with parameters";
        }

        cout << result.dump() << endl;

    } catch (const exception& e) {
        json error_result;
        error_result["error"] = e.what();
        cout << error_result.dump() << endl;
        return 1;
    }

    return 0;
}
`;

      default:
        throw new Error(`Unsupported language: ${language}`);
    }
  }

  private async executeInDocker(
    filePath: string,
    language: string
  ): Promise<{ output: any; memoryUsed: number }> {
    return new Promise((resolve, reject) => {
      const containerName = this.getContainerName(language);
      const volumeMount = `${path.dirname(filePath)}:/code`;
      const fileName = path.basename(filePath);

      // Validate fileName to prevent path traversal
      if (fileName.includes('..') || fileName.includes('/') || fileName.includes('\\')) {
        reject(new Error('Invalid file name'));
        return;
      }

      // Build Docker args based on language
      let dockerArgs: string[];

      if (language === 'python') {
        // Python: can execute directly without shell
        dockerArgs = [
          'run',
          '--rm',
          '-v', volumeMount,
          '--memory', `${this.maxMemory}m`,
          '--cpus', '1',
          '--network', 'none',
          containerName,
          'python3', `/code/${fileName}`
        ];
      } else {
        // Java/C++: require shell for compound commands (compile + execute)
        // Note: This is still a potential risk, but filename is validated
        const execCmd = this.getExecutionCommand(language, fileName);
        dockerArgs = [
          'run',
          '--rm',
          '-v', volumeMount,
          '--memory', `${this.maxMemory}m`,
          '--cpus', '1',
          '--network', 'none',
          containerName,
          'sh', '-c', execCmd
        ];
      }

      const docker = spawn('docker', dockerArgs);
      let stdout = '';
      let stderr = '';

      const timeout = setTimeout(() => {
        docker.kill();
        reject(new Error('Execution timeout'));
      }, this.maxExecutionTime);

      docker.stdout.on('data', (data) => {
        stdout += data.toString();
      });

      docker.stderr.on('data', (data) => {
        stderr += data.toString();
      });

      docker.on('close', (code) => {
        clearTimeout(timeout);

        if (code !== 0) {
          reject(new Error(stderr || `Process exited with code ${code}`));
          return;
        }

        try {
          const output = JSON.parse(stdout.trim());
          resolve({
            output,
            memoryUsed: 0, // Would need to query Docker stats for actual memory
          });
        } catch (error) {
          reject(new Error(`Failed to parse output: ${stdout}`));
        }
      });

      docker.on('error', (error) => {
        clearTimeout(timeout);
        reject(error);
      });
    });
  }

  private getContainerName(language: string): string {
    switch (language) {
      case 'python':
        return 'interview-prep-python';
      case 'java':
        return 'interview-prep-java';
      case 'cpp':
        return 'interview-prep-cpp';
      default:
        throw new Error(`No container for language: ${language}`);
    }
  }

  private getExecutionCommand(language: string, fileName: string): string {
    switch (language) {
      case 'python':
        return `python3 /code/${fileName}`;
      case 'java':
        return `javac /code/${fileName} && java -cp /code Main`;
      case 'cpp':
        return `g++ -std=c++17 /code/${fileName} -o /code/a.out && /code/a.out`;
      default:
        throw new Error(`No execution command for language: ${language}`);
    }
  }

  private getFileExtension(language: string): string {
    switch (language) {
      case 'python':
        return '.py';
      case 'java':
        return '.java';
      case 'cpp':
        return '.cpp';
      default:
        return '.txt';
    }
  }

  private compareOutputs(actual: any, expected: any): boolean {
    // Deep equality check
    return JSON.stringify(actual) === JSON.stringify(expected);
  }

  cleanup() {
    // Clean up temp directory
    if (fs.existsSync(this.tempDir)) {
      fs.rmSync(this.tempDir, { recursive: true, force: true });
    }
  }
}
