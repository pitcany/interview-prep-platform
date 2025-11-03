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

      const pythonProcess = spawn('python3', [testRunnerPath, inputData]);

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
          resolve(result);
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

  private prepareCodeWithTestCase(code: string, language: string, testCase: TestCase): string {
    const inputStr = JSON.stringify(testCase.input);

    switch (language) {
      case 'python':
        return `
import json
import sys

${code}

# Test case input
test_input = json.loads('${inputStr.replace(/'/g, "\\'")}')

# Execute the solution
if isinstance(test_input, list) and len(test_input) > 0:
    result = Solution().solve(*test_input)
else:
    result = Solution().solve(test_input)

# Output result as JSON
print(json.dumps(result))
`;

      case 'java':
        return `
import com.google.gson.*;

${code}

public class Main {
    public static void main(String[] args) {
        Gson gson = new Gson();
        String input = "${inputStr.replace(/"/g, '\\"')}";
        
        // Parse input and call solution
        // Note: This is simplified, actual implementation needs type handling
        Object result = new Solution().solve(gson.fromJson(input, Object.class));
        
        System.out.println(gson.toJson(result));
    }
}
`;

      case 'cpp':
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
    auto result = sol.solve(j);
    
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
