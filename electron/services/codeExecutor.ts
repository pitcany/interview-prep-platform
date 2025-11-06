import { spawn } from 'child_process';
import * as path from 'path';
import * as fs from 'fs';
import * as os from 'os';

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

  constructor(userDataPath?: string) {
    // Use userDataPath/code-exec instead of /tmp to avoid Docker mount issues
    const baseDir = userDataPath || os.tmpdir();
    this.tempDir = path.join(baseDir, 'code-exec');
    this.pythonServicePath = path.join(__dirname, '../../python-service');

    // Use Python service if SANDBOX_MODE is 'local', otherwise use Docker
    this.usePythonService = process.env.SANDBOX_MODE === 'local';

    console.log('CodeExecutor mode:', this.usePythonService ? 'Local Python' : 'Docker');
    console.log('CodeExecutor temp dir:', this.tempDir);
  }

  async initialize() {
    // Create temp directory if it doesn't exist
    if (!fs.existsSync(this.tempDir)) {
      fs.mkdirSync(this.tempDir, { recursive: true });
    }

    // Check if Python service is available
    const testRunnerPath = path.join(this.pythonServicePath, 'test_runner.py');
    if (this.usePythonService && !fs.existsSync(testRunnerPath)) {
      console.warn('Python service not found at:', this.pythonServicePath);
      console.warn('Falling back to Docker execution');
      this.usePythonService = false;
    }

    console.log('Code executor initialized');
    console.log('Execution mode:', this.usePythonService ? 'Python Service (local)' : 'Docker');
  }

  async executeCode(
    code: string,
    language: string,
    testCases: TestCase[]
  ): Promise<ExecutionResult> {
    console.log('executeCode called with:', {
      codeLength: code.length,
      language,
      testCasesCount: testCases.length,
      testCases: testCases
    });

    // Use Python service for local execution (faster, supports only Python)
    if (this.usePythonService && language === 'python') {
      console.log('Using Python service for execution');
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
      console.log('Test runner path:', testRunnerPath);

      const inputData = JSON.stringify({
        code,
        testCases,
        language: 'python',
        timeout: this.maxExecutionTime / 1000, // Convert to seconds
        maxMemory: this.maxMemory,
      });
      console.log('Spawning Python process with input data length:', inputData.length);

      const pythonProcess = spawn('python3', [testRunnerPath]);
      console.log('Python process spawned with PID:', pythonProcess.pid);

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
        console.log('Python stdout:', data.toString());
      });

      pythonProcess.stderr.on('data', (data) => {
        stderr += data.toString();
        console.log('Python stderr:', data.toString());
      });

      pythonProcess.on('error', (error) => {
        console.error('Python process error:', error);
      });

      pythonProcess.on('close', (code) => {
        clearTimeout(timeout);
        console.log('Python process closed with code:', code);
        console.log('Final stdout length:', stdout.length);
        console.log('Final stderr length:', stderr.length);

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

          console.log('Formatted result:', formattedResult);
          resolve(formattedResult);
        } catch (error) {
          console.error('Failed to parse Python output:', error);
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
    // Create a temporary file for the code
    const fileName = `code_${Date.now()}${this.getFileExtension(language)}`;
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

    switch (language) {
      case 'python':
        return `
import json
import sys
from typing import List, Optional, Dict, Set, Tuple

# Define common data structures used in LeetCode problems
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def _list_to_linked_list(values):
    """Convert a Python list to a ListNode linked list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def _linked_list_to_list(node):
    """Convert a ListNode linked list to a Python list."""
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result

${code}

# Test case input
test_input = json.loads('${inputStr.replace(/'/g, "\\'")}')

# Execute the solution
try:
    sol = Solution()

    # First, get all available methods from Solution class
    all_methods = [m for m in dir(sol) if not m.startswith('_') and callable(getattr(sol, m))]

    if not all_methods:
        raise AttributeError("Solution class has no callable methods")

    # Try to use extracted method name if it exists and is available
    method_name = None
    extracted_method = '${methodName}'
    if extracted_method and extracted_method != '' and extracted_method != 'solve' and extracted_method in all_methods:
        method_name = extracted_method

    # If extracted method doesn't exist or is 'solve', use the first available method
    if not method_name:
        method_name = all_methods[0]

    # Check if this is a linked list problem
    code_uses_listnode = 'ListNode' in """${code.replace(/"/g, '\\"').replace(/\n/g, '\\n')}"""

    # Prepare input - convert lists to ListNodes if needed
    processed_input = test_input
    if code_uses_listnode and isinstance(test_input, list):
        # Convert each list in the input to a ListNode
        processed_input = []
        for item in test_input:
            if isinstance(item, list):
                processed_input.append(_list_to_linked_list(item))
            else:
                processed_input.append(item)

    # Call the method
    method = getattr(sol, method_name)
    if isinstance(processed_input, list) and len(processed_input) > 0:
        result = method(*processed_input)
    else:
        result = method(processed_input)

    # Convert ListNode output back to list if needed
    if code_uses_listnode:
        if result is None:
            result = []
        elif hasattr(result, 'val') and hasattr(result, 'next'):
            result = _linked_list_to_list(result)

    print(json.dumps(result))
except AttributeError as e:
    error_msg = str(e)
    available_methods = all_methods if 'all_methods' in locals() else 'unknown'
    print(json.dumps({"error": f"Solution class method error: {error_msg}. Available methods: {available_methods}", "method_tried": "${methodName}"}))
    sys.exit(1)
except Exception as e:
    print(json.dumps({"error": str(e), "error_type": type(e).__name__}))
    sys.exit(1)
`;

      case 'java':
        // For Java, we'd need to parse the method signature, but for now use a generic approach
        // Note: This is simplified and may need adjustment based on actual Java code structure
        return `
import com.google.gson.*;

${code}

public class Main {
    public static void main(String[] args) {
        Gson gson = new Gson();
        String input = "${inputStr.replace(/"/g, '\\"')}";
        
        // Parse input and call solution
        // Note: This is simplified, actual implementation needs type handling
        // For now, try common method names or use reflection
        Solution sol = new Solution();
        try {
            java.lang.reflect.Method method = sol.getClass().getDeclaredMethods()[0];
            Object result = method.invoke(sol, gson.fromJson(input, Object.class));
            System.out.println(gson.toJson(result));
        } catch (Exception e) {
            System.out.println("{\\"error\\": \\"" + e.getMessage() + "\\"}");
        }
    }
}
`;

      case 'cpp':
        // For C++, we'd need to parse the method signature, but for now use a generic approach
        // Note: This is simplified and may need adjustment based on actual C++ code structure
        return `
#include <iostream>
#include <string>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

${code}

int main() {
    std::string input = R"(${inputStr})";
    json j = json::parse(input);
    
    Solution sol;
    // Note: This assumes the Solution class has a method that can be called
    // For proper implementation, we'd need to parse the method signature
    // For now, this is a placeholder that will need language-specific handling
    auto result = sol.solve(j);  // This will need to be adjusted based on actual method
    
    std::cout << json(result).dump() << std::endl;
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

      // Get execution command and split into shell args
      const execCmd = this.getExecutionCommand(language, fileName);

      const dockerArgs = [
        'run',
        '--rm',
        '-v', volumeMount,
        '--memory', `${this.maxMemory}m`,
        '--cpus', '1',
        '--network', 'none',
        containerName,
        'sh', '-c', execCmd  // Use shell to execute complex commands with pipes
      ];

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
