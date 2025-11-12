import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAppStore } from '../store';
import { api } from '../services/api';
import QuestionList from '../components/QuestionList';
import QuestionHeader from '../components/Practice/QuestionHeader';
import QuestionDescription from '../components/Practice/QuestionDescription';
import LeetCodePracticeView from '../components/Practice/LeetCodePracticeView';
import MLDesignPracticeView from '../components/Practice/MLDesignPracticeView';
import { Toast } from '../components/Toast';
import { useToast } from '../hooks/useToast';
import type { Question, LeetCodeQuestion, MLDesignQuestion, TestCase, ExecutionResult, DiagramData } from '../types';
import { validateCode, validateExplanation } from '../utils/validation';
import { ERROR_MESSAGES, SUCCESS_MESSAGES } from '../constants';

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
  const [isLoadingQuestion, setIsLoadingQuestion] = useState(false);
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

    setIsLoadingQuestion(true);
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

        // Load hints from ML Design details
        if (details.hints && Array.isArray(details.hints) && details.hints.length > 0) {
          setHints(details.hints);
          setHintsLoaded(true);
        } else {
          setHints([]);
          setHintsLoaded(true);
        }
        setRevealedHints(0);
      }
    } catch (error) {
      console.error('Failed to load question details:', error);
      showToast('Failed to load question details. Please try again.', 'error');
    } finally {
      setIsLoadingQuestion(false);
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
    if (!currentUser) {
      console.error('Submit failed: No current user');
      showToast(ERROR_MESSAGES.NO_USER_SELECTED, 'error');
      return;
    }
    if (!selectedQuestion) {
      console.error('Submit failed: No question selected');
      showToast(ERROR_MESSAGES.SELECT_QUESTION, 'error');
      return;
    }
    if (!questionDetails) {
      console.error('Submit failed: Question details not loaded');
      showToast('Question details are still loading. Please wait and try again.', 'error');
      return;
    }

    // Validate code content
    const codeValidation = validateCode(code);
    if (!codeValidation.isValid) {
      showToast(codeValidation.error!, 'error');
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

      // Generate feedback if all tests passed
      if (result.executionResult.status === 'passed') {
        try {
          await api.generateFeedback({
            userId: currentUser.id,
            submissionId: result.submission.id,
            submissionType: 'code',
          });
          showToast(`${SUCCESS_MESSAGES.FEEDBACK_GENERATED} Check the Progress page to view it.`, 'success');
        } catch (feedbackError: any) {
          console.error('[PRACTICE] Feedback generation failed:', feedbackError);
          showToast(`AI feedback unavailable: ${feedbackError.message || 'Unknown error'}`, 'warning');
          // Don't fail the submission even if feedback fails
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

    // Validate explanation content and length
    const explanationValidation = validateExplanation(explanation, 50);
    if (!explanationValidation.isValid) {
      showToast(explanationValidation.error!, 'warning');
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

      showToast(`${SUCCESS_MESSAGES.DESIGN_SUBMITTED} Check the Progress page for feedback.`, 'success');
      
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
            {/* Question header */}
            <QuestionHeader
              question={selectedQuestion}
              category={category}
              showDescription={showDescription}
              hints={hints}
              revealedHints={revealedHints}
              hintsLoaded={hintsLoaded}
              onBack={() => setSelectedQuestion(null)}
              onToggleDescription={() => setShowDescription(!showDescription)}
              onGetHint={handleGetHint}
            />

            {/* Content area */}
            <div className="flex-1 flex min-h-0">
              {/* Question description (collapsible) */}
              {showDescription && (
                <QuestionDescription
                  question={selectedQuestion}
                  category={category}
                  questionDetails={questionDetails}
                  mlDesignDetails={mlDesignDetails}
                  hints={hints}
                  revealedHints={revealedHints}
                />
              )}

              {/* Main editor area - conditional based on category */}
              <div className={`flex-1 flex flex-col min-w-0 ${showDescription ? '' : 'w-full'}`}>
                {isLoadingQuestion ? (
                  <div className="flex-1 flex items-center justify-center bg-gray-900">
                    <div className="text-center">
                      <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mb-4"></div>
                      <p className="text-gray-400">Loading question details...</p>
                    </div>
                  </div>
                ) : category === 'leetcode' && questionDetails ? (
                  <LeetCodePracticeView
                    questionDetails={questionDetails}
                    code={code}
                    language={language}
                    testCases={testCases}
                    results={results}
                    isRunning={isRunning}
                    isSubmitting={isSubmitting}
                    onCodeChange={setCode}
                    onLanguageChange={setLanguage}
                    onResetCode={handleResetCode}
                    onRunCode={handleRunCode}
                    onSubmit={handleSubmit}
                    onAddTestCase={handleAddTestCase}
                    onRemoveTestCase={handleRemoveTestCase}
                    onViewFeedback={() => navigate('/progress')}
                  />
                ) : category === 'ml_system_design' && mlDesignDetails ? (
                  <MLDesignPracticeView
                    mlDesignDetails={mlDesignDetails}
                    diagramData={diagramData}
                    explanation={explanation}
                    isSubmitting={isSubmitting}
                    onSaveDiagram={handleSaveDiagram}
                    onExplanationChange={setExplanation}
                    onSubmitDesign={handleSubmitDesign}
                    onViewFeedback={() => navigate('/progress')}
                  />
                ) : null}
              </div>
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
