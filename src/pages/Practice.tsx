import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAppStore } from '../store';
import { api } from '../services/api';
import QuestionList from '../components/QuestionList';
import CodeEditor from '../components/CodeEditor';
import TestRunner from '../components/TestRunner';
import { Play, Send, Sparkles, Loader2, ChevronLeft } from 'lucide-react';
import type { Question, LeetCodeQuestion, TestCase, ExecutionResult } from '../types';

export default function Practice() {
  const { category = 'leetcode' } = useParams<{ category?: 'leetcode' | 'ml_system_design' }>();
  const navigate = useNavigate();
  const currentUser = useAppStore((state) => state.currentUser);
  
  const [selectedQuestion, setSelectedQuestion] = useState<Question | null>(null);
  const [questionDetails, setQuestionDetails] = useState<LeetCodeQuestion | null>(null);
  const [code, setCode] = useState('');
  const [originalCode, setOriginalCode] = useState('');
  const [language, setLanguage] = useState<'python' | 'java' | 'cpp'>('python');
  const [testCases, setTestCases] = useState<TestCase[]>([]);
  const [isRunning, setIsRunning] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [results, setResults] = useState<ExecutionResult | null>(null);
  const [showDescription, setShowDescription] = useState(true);

  useEffect(() => {
    if (selectedQuestion) {
      loadQuestionDetails();
    }
  }, [selectedQuestion, language]);

  const loadQuestionDetails = async () => {
    if (!selectedQuestion) return;

    try {
      const details = await api.getLeetCodeDetails(selectedQuestion.id);
      setQuestionDetails(details);
      
      // Set initial code based on language
      const signatureKey = `function_signature_${language}` as keyof LeetCodeQuestion;
      const initialCode = (details[signatureKey] as string) || '';
      setCode(initialCode);
      setOriginalCode(initialCode);
      
      // Parse test cases
      const cases = JSON.parse(details.test_cases);
      setTestCases(cases);
      setResults(null);
    } catch (error) {
      console.error('Failed to load question details:', error);
    }
  };

  const handleRunCode = async () => {
    if (!currentUser || !selectedQuestion || !questionDetails) return;

    setIsRunning(true);
    try {
      const result = await api.executeCode({
        code,
        language,
        testCases,
        questionId: selectedQuestion.id,
      });
      setResults(result);
    } catch (error: any) {
      console.error('Failed to run code:', error);
      setResults({
        status: 'error',
        testResults: [],
        executionTime: 0,
        memoryUsed: 0,
        errorMessage: error.message,
      });
    } finally {
      setIsRunning(false);
    }
  };

  const handleSubmit = async () => {
    if (!currentUser || !selectedQuestion || !questionDetails) return;

    setIsSubmitting(true);
    try {
      const result = await api.submitCode({
        userId: currentUser.id,
        questionId: selectedQuestion.id,
        code,
        language,
        customTestCases: testCases,
      });
      
      setResults(result.executionResult);
      
      // Generate feedback if all tests passed
      if (result.executionResult.status === 'passed') {
        await api.generateFeedback({
          userId: currentUser.id,
          submissionId: result.submission.id,
          submissionType: 'code',
        });
      }
    } catch (error: any) {
      console.error('Failed to submit code:', error);
      setResults({
        status: 'error',
        testResults: [],
        executionTime: 0,
        memoryUsed: 0,
        errorMessage: error.message,
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleAddTestCase = (testCase: TestCase) => {
    setTestCases([...testCases, testCase]);
  };

  const handleRemoveTestCase = (index: number) => {
    setTestCases(testCases.filter((_, i) => i !== index));
  };

  const handleResetCode = () => {
    if (confirm('Are you sure you want to reset your code to the template?')) {
      setCode(originalCode);
      setResults(null);
    }
  };

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

  if (!currentUser) {
    return null;
  }

  return (
    <div className="h-screen flex overflow-hidden">
      {/* Left sidebar - Question list */}
      <div className="w-80 border-r border-gray-700 flex-shrink-0">
        <QuestionList
          category={category}
          onSelectQuestion={setSelectedQuestion}
          selectedQuestionId={selectedQuestion?.id}
          userId={currentUser.id}
        />
      </div>

      {/* Main content */}
      {selectedQuestion ? (
        <div className="flex-1 flex flex-col min-w-0">
          {/* Top bar */}
          <div className="flex items-center justify-between px-6 py-3 bg-gray-800 border-b border-gray-700">
            <div className="flex items-center gap-3">
              <button
                onClick={() => setSelectedQuestion(null)}
                className="text-gray-400 hover:text-white transition-colors"
              >
                <ChevronLeft size={20} />
              </button>
              <div>
                <h1 className="text-lg font-bold text-white">
                  {selectedQuestion.title}
                </h1>
                <div className="flex items-center gap-2 mt-1">
                  <span className={`text-xs px-2 py-0.5 rounded font-medium ${
                    selectedQuestion.difficulty === 'easy' ? 'bg-green-500/20 text-green-500' :
                    selectedQuestion.difficulty === 'medium' ? 'bg-yellow-500/20 text-yellow-500' :
                    'bg-red-500/20 text-red-500'
                  }`}>
                    {selectedQuestion.difficulty}
                  </span>
                  {selectedQuestion.tags && JSON.parse(selectedQuestion.tags).slice(0, 3).map((tag: string) => (
                    <span key={tag} className="text-xs px-2 py-0.5 bg-gray-700 text-gray-400 rounded">
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            </div>
            
            <button
              onClick={() => setShowDescription(!showDescription)}
              className="px-3 py-1 text-sm text-gray-400 hover:text-white transition-colors"
            >
              {showDescription ? 'Hide' : 'Show'} Description
            </button>
          </div>

          {/* Content area */}
          <div className="flex-1 flex min-h-0">
            {/* Question description (collapsible) */}
            {showDescription && (
              <div className="w-1/3 border-r border-gray-700 overflow-y-auto p-6">
                <div className="prose prose-invert max-w-none">
                  <div className="whitespace-pre-wrap text-gray-300">
                    {selectedQuestion.description}
                  </div>
                  
                  {selectedQuestion.examples && (
                    <div className="mt-6">
                      <h3 className="text-white font-semibold mb-3">Examples</h3>
                      {JSON.parse(selectedQuestion.examples).map((example: any, i: number) => (
                        <div key={i} className="mb-4 p-4 bg-gray-800 rounded-lg">
                          <div className="text-sm">
                            <div className="mb-2">
                              <span className="text-gray-400">Input:</span>
                              <div className="font-mono text-white mt-1">
                                {JSON.stringify(example.input)}
                              </div>
                            </div>
                            <div className="mb-2">
                              <span className="text-gray-400">Output:</span>
                              <div className="font-mono text-white mt-1">
                                {JSON.stringify(example.output)}
                              </div>
                            </div>
                            {example.explanation && (
                              <div>
                                <span className="text-gray-400">Explanation:</span>
                                <div className="text-gray-300 mt-1">{example.explanation}</div>
                              </div>
                            )}
                          </div>
                        </div>
                      ))}
                    </div>
                  )}

                  {questionDetails?.expected_time_complexity && (
                    <div className="mt-6">
                      <h3 className="text-white font-semibold mb-2">Constraints</h3>
                      <div className="text-sm text-gray-400">
                        <p>Time Complexity: {questionDetails.expected_time_complexity}</p>
                        <p>Space Complexity: {questionDetails.expected_space_complexity}</p>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* Code editor and test runner */}
            <div className={`flex-1 flex flex-col min-w-0 ${showDescription ? '' : 'w-full'}`}>
              {/* Split view: Editor top, Test runner bottom */}
              <div className="flex-1 min-h-0">
                <CodeEditor
                  code={code}
                  language={language}
                  onChange={setCode}
                  onLanguageChange={setLanguage}
                  onReset={handleResetCode}
                />
              </div>

              <div className="h-80 border-t border-gray-700">
                <TestRunner
                  testCases={testCases}
                  results={results?.testResults}
                  onAddTestCase={handleAddTestCase}
                  onRemoveTestCase={handleRemoveTestCase}
                />
              </div>
            </div>
          </div>

          {/* Action bar */}
          <div className="px-6 py-3 bg-gray-800 border-t border-gray-700 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <button
                onClick={handleRunCode}
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
                onClick={handleSubmit}
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
                    onClick={() => navigate('/progress')}
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
      ) : (
        <div className="flex-1 flex items-center justify-center bg-gray-900">
          <div className="text-center">
            <p className="text-xl text-gray-400 mb-2">
              Select a question to get started
            </p>
            <p className="text-sm text-gray-500">
              Choose from the list on the left
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
