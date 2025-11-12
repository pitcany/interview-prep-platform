import { Play, Send, Loader2, Sparkles } from 'lucide-react';
import CodeEditor from '../CodeEditor';
import TestRunner from '../TestRunner';
import SolutionViewer from '../SolutionViewer';
import type { LeetCodeQuestion, TestCase, ExecutionResult } from '../../types';

interface LeetCodePracticeViewProps {
  questionDetails: LeetCodeQuestion;
  code: string;
  language: 'python' | 'java' | 'cpp';
  testCases: TestCase[];
  results: ExecutionResult | null;
  isRunning: boolean;
  isSubmitting: boolean;
  onCodeChange: (code: string) => void;
  onLanguageChange: (language: 'python' | 'java' | 'cpp') => void;
  onResetCode: () => void;
  onRunCode: () => void;
  onSubmit: () => void;
  onAddTestCase: (testCase: TestCase) => void;
  onRemoveTestCase: (index: number) => void;
  onViewFeedback: () => void;
}

export default function LeetCodePracticeView({
  questionDetails,
  code,
  language,
  testCases,
  results,
  isRunning,
  isSubmitting,
  onCodeChange,
  onLanguageChange,
  onResetCode,
  onRunCode,
  onSubmit,
  onAddTestCase,
  onRemoveTestCase,
  onViewFeedback,
}: LeetCodePracticeViewProps) {
  const getStatusColor = () => {
    if (!results) return 'text-gray-400';
    switch (results.status) {
      case 'passed': return 'text-green-500';
      case 'failed': return 'text-red-500';
      case 'error': return 'text-orange-500';
      case 'timeout': return 'text-yellow-500';
      default: return 'text-gray-400';
    }
  };

  return (
    <div className="flex-1 flex flex-col min-w-0">
      {/* Code editor */}
      <div className="flex-1 min-h-0">
        <CodeEditor
          code={code}
          language={language}
          onChange={onCodeChange}
          onLanguageChange={onLanguageChange}
          onReset={onResetCode}
        />
      </div>

      {/* Test runner */}
      <div className="h-80 border-t border-gray-700">
        <TestRunner
          testCases={testCases}
          results={results?.testResults}
          onAddTestCase={onAddTestCase}
          onRemoveTestCase={onRemoveTestCase}
        />
      </div>

      {/* Solution viewer */}
      <SolutionViewer
        category="leetcode"
        solutionPython={questionDetails.solution_python}
        solutionJava={questionDetails.solution_java}
        solutionCpp={questionDetails.solution_cpp}
        solutionExplanation={questionDetails.solution_explanation}
      />

      {/* Action bar */}
      <div className="px-6 py-3 bg-gray-800 border-t border-gray-700 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <button
            onClick={onRunCode}
            disabled={isRunning || isSubmitting}
            className="px-4 py-2 bg-green-600 hover:bg-green-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white rounded-lg transition-colors flex items-center gap-2"
          >
            {isRunning ? (
              <><Loader2 size={18} className="animate-spin" /> Running...</>
            ) : (
              <><Play size={18} /> Run Code</>
            )}
          </button>

          <button
            onClick={onSubmit}
            disabled={isRunning || isSubmitting}
            className="px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white rounded-lg transition-colors flex items-center gap-2"
          >
            {isSubmitting ? (
              <><Loader2 size={18} className="animate-spin" /> Submitting...</>
            ) : (
              <><Send size={18} /> Submit</>
            )}
          </button>
        </div>

        {results && (
          <div className="flex items-center gap-4">
            <div className="text-sm">
              <span className={`font-medium ${getStatusColor()}`}>
                {results.status.toUpperCase()}
              </span>
              <span className="text-gray-400 ml-2">
                {results.testResults?.filter((t) => t.passed).length || 0}/
                {results.testResults?.length || 0} tests passed
              </span>
            </div>

            {results.executionTime > 0 && (
              <div className="text-sm text-gray-400">
                {results.executionTime}ms • {results.memoryUsed}KB
              </div>
            )}

            {results.status === 'passed' && (
              <button
                onClick={onViewFeedback}
                className="px-3 py-1 bg-purple-600 hover:bg-purple-700 text-white text-sm rounded-lg transition-colors flex items-center gap-1"
              >
                <Sparkles size={16} />
                View Feedback
              </button>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
