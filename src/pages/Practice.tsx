import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAppStore } from '../store';
import { api } from '../services/api';
import QuestionList from '../components/QuestionList';
import CodeEditor from '../components/CodeEditor';
import TestRunner from '../components/TestRunner';
import DiagramEditor from '../components/DiagramEditor';
import SolutionViewer from '../components/SolutionViewer';
import { Toast } from '../components/Toast';
import { useToast } from '../hooks/useToast';
import { Play, Send, Sparkles, Loader2, ChevronLeft, FileText, Lightbulb } from 'lucide-react';
import type { Question, LeetCodeQuestion, MLDesignQuestion, TestCase, ExecutionResult, DiagramData } from '../types';

export default function Practice() {
  const { category = 'leetcode' } = useParams<{ category?: 'leetcode' | 'ml_system_design' }>();
  const navigate = useNavigate();
  const currentUser = useAppStore((state) => state.currentUser);
  const { toasts, showToast, hideToast } = useToast();
  
  const [selectedQuestion, setSelectedQuestion] = useState<Question | null>(null);

  // LeetCode-specific state
  const [questionDetails, setQuestionDetails] = useState<LeetCodeQuestion | null>(null);
  const [code, setCode] = useState('');
  const [originalCode, setOriginalCode] = useState('');
  const [language, setLanguage] = useState<'python' | 'java' | 'cpp'>('python');
  const [testCases, setTestCases] = useState<TestCase[]>([]);
  const [isRunning, setIsRunning] = useState(false);
  const [results, setResults] = useState<ExecutionResult | null>(null);

  // ML Design-specific state
  const [mlDesignDetails, setMlDesignDetails] = useState<MLDesignQuestion | null>(null);
  const [diagramData, setDiagramData] = useState<DiagramData>({ nodes: [], edges: [] });
  const [explanation, setExplanation] = useState('');
  const [designStartTime, setDesignStartTime] = useState<number>(Date.now());

  // Common state
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [showDescription, setShowDescription] = useState(true);
  const [hints, setHints] = useState<string[]>([]);
  const [revealedHints, setRevealedHints] = useState<number>(0);
  const [hintsLoaded, setHintsLoaded] = useState(false);

  useEffect(() => {
    if (selectedQuestion) {
      loadQuestionDetails();
      // Reset hints when question changes
      setHints([]);
      setRevealedHints(0);
      setHintsLoaded(false);
    }
  }, [selectedQuestion, language]);

  const loadQuestionDetails = async () => {
    if (!selectedQuestion) return;

    try {
      if (category === 'leetcode') {
        const details = await api.getLeetCodeDetails(selectedQuestion.id);
        setQuestionDetails(details);
        setMlDesignDetails(null);

        // Set initial code based on language
        const signatureKey = `function_signature_${language}` as keyof LeetCodeQuestion;
        const initialCode = (details[signatureKey] as string) || '';
        setCode(initialCode);
        setOriginalCode(initialCode);

        // Parse test cases
        const cases = JSON.parse(details.test_cases);
        setTestCases(cases);
        setResults(null);

        // Load hints from question details
        if (details.hints && Array.isArray(details.hints) && details.hints.length > 0) {
          setHints(details.hints);
          setHintsLoaded(true);
        } else {
          setHints([]);
          setHintsLoaded(true);
        }
        setRevealedHints(0);
      } else {
        const details = await api.getMLDesignDetails(selectedQuestion.id);
        setMlDesignDetails(details);
        setQuestionDetails(null);

        // Reset ML Design state
        setDiagramData({ nodes: [], edges: [] });
        setExplanation('');
        setDesignStartTime(Date.now());
      }
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
    // Diagnostic logging
    console.log('handleSubmit called', {
      currentUser: !!currentUser,
      selectedQuestion: !!selectedQuestion,
      questionDetails: !!questionDetails,
    });

    if (!currentUser) {
      console.error('Submit failed: No current user');
      showToast('Please log in first', 'error');
      return;
    }
    if (!selectedQuestion) {
      console.error('Submit failed: No question selected');
      showToast('Please select a question first', 'error');
      return;
    }
    if (!questionDetails) {
      console.error('Submit failed: Question details not loaded');
      showToast('Question details are still loading. Please wait and try again.', 'error');
      return;
    }

    setIsSubmitting(true);
    try {
      // Always use test cases from question details for submission
      // This ensures we always have the official test cases even if state is empty
      let visibleTestCases: TestCase[] = [];
      
      if (questionDetails.test_cases) {
        try {
          visibleTestCases = JSON.parse(questionDetails.test_cases);
        } catch (e) {
          console.error('Failed to parse test cases from question:', e);
          // Fallback to state test cases if parsing fails
          visibleTestCases = testCases;
        }
      } else {
        // Fallback to state test cases if question doesn't have test cases
        visibleTestCases = testCases;
      }

      // Parse hidden test cases if available
      let hiddenTestCases: TestCase[] = [];
      if (questionDetails.hidden_test_cases) {
        try {
          hiddenTestCases = JSON.parse(questionDetails.hidden_test_cases);
        } catch (e) {
          console.error('Failed to parse hidden test cases from question:', e);
        }
      }

      // Combine visible and hidden test cases for submission
      // Hidden test cases are run but results are only shown as pass/fail
      const allTestCases = [...visibleTestCases, ...hiddenTestCases];

      // Ensure we have test cases to run
      if (allTestCases.length === 0) {
        throw new Error('No test cases available for this question');
      }

      const result = await api.submitCode({
        userId: currentUser.id,
        questionId: selectedQuestion.id,
        code,
        language,
        customTestCases: allTestCases,
      });

      setResults(result.executionResult);

      // Generate feedback if all tests passed (optional, don't fail if not configured)
      if (result.executionResult.status === 'passed') {
        try {
          await api.generateFeedback({
            userId: currentUser.id,
            submissionId: result.submission.id,
            submissionType: 'code',
          });
        } catch (feedbackError: any) {
          console.warn('Feedback generation not available:', feedbackError.message);
          // Don't overwrite the successful test results
        }
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

  const handleSubmitDesign = async () => {
    if (!currentUser || !selectedQuestion || !mlDesignDetails) return;

    if (diagramData.nodes.length === 0) {
      showToast('Please create a system design diagram before submitting.', 'warning');
      return;
    }

    if (!explanation.trim()) {
      showToast('Please provide a written explanation of your design.', 'warning');
      return;
    }

    setIsSubmitting(true);
    try {
      const timeSpent = Math.floor((Date.now() - designStartTime) / 1000);
      const submission = await api.submitDesign({
        userId: currentUser.id,
        questionId: selectedQuestion.id,
        diagramData,
        writtenExplanation: explanation,
        timeSpent,
      });

      // Generate AI feedback
      await api.generateFeedback({
        userId: currentUser.id,
        submissionId: submission.id,
        submissionType: 'design',
      });

      showToast('Design submitted successfully! Check the Progress page for feedback.', 'success');
      
      // Delay navigation to allow toast to be visible
      setTimeout(() => {
        navigate('/progress');
      }, 1500);
    } catch (error: any) {
      console.error('Failed to submit design:', error);
      showToast('Failed to submit design: ' + error.message, 'error');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleSaveDiagram = (nodes: any[], edges: any[]) => {
    setDiagramData({ nodes, edges });
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

  const handleGetHint = async () => {
    if (!selectedQuestion) return;

    // If no hints are available, show a message
    if (hintsLoaded && hints.length === 0) {
      showToast('No hints available for this question', 'info');
      return;
    }

    // If we haven't loaded hints yet, try to get them from question details
    if (!hintsLoaded && questionDetails?.hints) {
      setHints(questionDetails.hints);
      setHintsLoaded(true);
    }

    // Reveal the next hint
    if (revealedHints < hints.length) {
      setRevealedHints(revealedHints + 1);
    } else if (hints.length > 0) {
      showToast('All hints have been revealed', 'info');
    }
  };

  const handleCategoryChange = (newCategory: 'leetcode' | 'ml_system_design') => {
    navigate(`/practice/${newCategory}`);
    setSelectedQuestion(null);
    setQuestionDetails(null);
    setMlDesignDetails(null);
    setDiagramData({ nodes: [], edges: [] });
    setExplanation('');
    setCode('');
    setResults(null);
    setHints([]);
    setRevealedHints(0);
    setHintsLoaded(false);
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
    <>
      <div className="h-screen flex overflow-hidden">
        {/* Left sidebar - Question list */}
        <div className="w-80 border-r border-gray-700 flex-shrink-0">
          <QuestionList
            category={category}
            onSelectQuestion={setSelectedQuestion}
            selectedQuestionId={selectedQuestion?.id}
            userId={currentUser.id}
            onCategoryChange={handleCategoryChange}
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
            
            <div className="flex items-center gap-3">
              {selectedQuestion && (category === 'leetcode' || category === 'ml_system_design') && (
                <button
                  onClick={handleGetHint}
                  disabled={hintsLoaded && (hints.length === 0 || revealedHints >= hints.length)}
                  className="px-3 py-1.5 text-sm bg-yellow-600 hover:bg-yellow-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white rounded-lg transition-colors flex items-center gap-2"
                  title={
                    hintsLoaded && hints.length === 0 ? 'No hints available' :
                    hintsLoaded && revealedHints >= hints.length ? 'All hints revealed' :
                    'Get a hint'
                  }
                >
                  <Lightbulb size={16} />
                  {hintsLoaded && hints.length === 0 ? 'No Hints Available' :
                   hintsLoaded && revealedHints >= hints.length ? 'All Hints Revealed' :
                   hintsLoaded ? `Get Hint (${revealedHints}/${hints.length})` :
                   `Get Hint (0/?)`}
                </button>
              )}
              <button
                onClick={() => setShowDescription(!showDescription)}
                className="px-3 py-1 text-sm text-gray-400 hover:text-white transition-colors"
              >
                {showDescription ? 'Hide' : 'Show'} Description
              </button>
            </div>
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

                  {category === 'leetcode' && selectedQuestion.examples && (
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

                  {category === 'leetcode' && questionDetails?.expected_time_complexity && (
                    <div className="mt-6">
                      <h3 className="text-white font-semibold mb-2">Constraints</h3>
                      <div className="text-sm text-gray-400">
                        <p>Time Complexity: {questionDetails.expected_time_complexity}</p>
                        <p>Space Complexity: {questionDetails.expected_space_complexity}</p>
                      </div>
                    </div>
                  )}

                  {/* Hints Section */}
                  {revealedHints > 0 && (
                    <div className="mt-6">
                      <h3 className="text-white font-semibold mb-3 flex items-center gap-2">
                        <Lightbulb className="text-yellow-500" size={20} />
                        Hints
                      </h3>
                      <div className="space-y-3">
                        {hints.slice(0, revealedHints).map((hint, index) => (
                          <div key={index} className="p-4 bg-yellow-500/10 border border-yellow-500/20 rounded-lg">
                            <div className="flex items-start gap-3">
                              <span className="text-yellow-500 font-semibold text-sm mt-0.5">
                                Hint {index + 1}:
                              </span>
                              <p className="text-sm text-gray-300 flex-1">{hint}</p>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {category === 'ml_system_design' && mlDesignDetails && (
                    <>
                      {mlDesignDetails.scenario && (
                        <div className="mt-6">
                          <h3 className="text-white font-semibold mb-3">Scenario</h3>
                          <div className="text-sm text-gray-300 whitespace-pre-wrap">
                            {mlDesignDetails.scenario}
                          </div>
                        </div>
                      )}

                      {mlDesignDetails.requirements && (
                        <div className="mt-6">
                          <h3 className="text-white font-semibold mb-3">Requirements</h3>
                          <ul className="text-sm text-gray-300 space-y-2 list-disc list-inside">
                            {mlDesignDetails.requirements.map((req: string, i: number) => (
                              <li key={i}>{req}</li>
                            ))}
                          </ul>
                        </div>
                      )}

                      {mlDesignDetails.key_components && mlDesignDetails.key_components.length > 0 && (
                        <div className="mt-6">
                          <h3 className="text-white font-semibold mb-3">Key Components</h3>
                          <div className="flex flex-wrap gap-2">
                            {mlDesignDetails.key_components.map((component: string, i: number) => (
                              <span key={i} className="text-xs px-2 py-1 bg-blue-600/20 text-blue-400 rounded">
                                {component}
                              </span>
                            ))}
                          </div>
                        </div>
                      )}

                      {mlDesignDetails.evaluation_criteria && (
                        <div className="mt-6">
                          <h3 className="text-white font-semibold mb-3">Evaluation Criteria</h3>
                          <div className="text-sm text-gray-300 space-y-2">
                            {Object.entries(mlDesignDetails.evaluation_criteria).map(([key, value]) => (
                              <div key={key}>
                                <span className="font-medium text-blue-400">{key}:</span> {value}
                              </div>
                            ))}
                          </div>
                        </div>
                      )}
                    </>
                  )}
                </div>
              </div>
            )}

            {/* Main editor area - conditional based on category */}
            <div className={`flex-1 flex flex-col min-w-0 ${showDescription ? '' : 'w-full'}`}>
              {category === 'leetcode' ? (
                <>
                  {/* Split view: Code editor top, Test runner bottom */}
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

                  {/* Solution Viewer for LeetCode */}
                  <SolutionViewer
                    category="leetcode"
                    solutionPython={questionDetails?.solution_python}
                    solutionJava={questionDetails?.solution_java}
                    solutionCpp={questionDetails?.solution_cpp}
                    solutionExplanation={questionDetails?.solution_explanation}
                  />
                </>
              ) : (
                <>
                  {/* ML System Design: Diagram editor top, explanation bottom */}
                  <div className="flex-1 min-h-0">
                    <DiagramEditor
                      initialNodes={diagramData.nodes}
                      initialEdges={diagramData.edges}
                      onSave={handleSaveDiagram}
                    />
                  </div>

                  <div className="h-80 border-t border-gray-700 bg-gray-900 flex flex-col">
                    <div className="px-4 py-2 bg-gray-800 border-b border-gray-700 flex items-center gap-2">
                      <FileText size={18} className="text-gray-400" />
                      <span className="text-sm font-medium text-white">Written Explanation</span>
                      <span className="text-xs text-gray-500 ml-auto">
                        {explanation.length} characters
                      </span>
                    </div>
                    <textarea
                      value={explanation}
                      onChange={(e) => setExplanation(e.target.value)}
                      placeholder="Explain your system design here. Describe the components, data flow, scaling strategies, trade-offs, and how it meets the requirements..."
                      className="flex-1 bg-gray-900 text-gray-300 px-4 py-3 resize-none focus:outline-none font-mono text-sm"
                    />
                  </div>

                  {/* Solution Viewer for ML Design */}
                  <SolutionViewer
                    category="ml_system_design"
                    sampleSolution={mlDesignDetails?.sample_solution}
                  />
                </>
              )}
            </div>
          </div>

          {/* Action bar */}
          <div className="px-6 py-3 bg-gray-800 border-t border-gray-700 flex items-center justify-between">
            {category === 'leetcode' ? (
              <>
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
              </>
            ) : (
              <>
                <div className="flex items-center gap-3 text-sm text-gray-400">
                  <span>Save your diagram and provide a written explanation</span>
                </div>

                <div className="flex items-center gap-3">
                  <button
                    onClick={handleSubmitDesign}
                    disabled={isSubmitting}
                    className="px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white rounded-lg transition-colors flex items-center gap-2"
                  >
                    {isSubmitting ? (
                      <><Loader2 size={18} className="animate-spin" /> Submitting...</>
                    ) : (
                      <><Send size={18} /> Submit Design</>
                    )}
                  </button>

                  <button
                    onClick={() => navigate('/progress')}
                    className="px-3 py-1 bg-purple-600 hover:bg-purple-700 text-white text-sm rounded-lg transition-colors flex items-center gap-1"
                  >
                    <Sparkles size={16} />
                    View Feedback
                  </button>
                </div>
              </>
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

      {/* Toast notifications */}
      {toasts.map((toast) => (
        <Toast
          key={toast.id}
          message={toast.message}
          type={toast.type}
          onClose={() => hideToast(toast.id)}
        />
      ))}
    </>
  );
}
