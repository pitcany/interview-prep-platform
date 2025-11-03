import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppStore } from '../store';
import { api } from '../services/api';
import MockInterviewSetup, { InterviewConfig } from '../components/MockInterviewSetup';
import Timer from '../components/Timer';
import MockInterviewReport from '../components/MockInterviewReport';
import CodeEditor from '../components/CodeEditor';
import TestRunner from '../components/TestRunner';
import DiagramEditor from '../components/DiagramEditor';
import { ArrowLeft, AlertCircle } from 'lucide-react';
import type { Question, LeetCodeQuestion, ExecutionResult } from '../types';
import { Node, Edge } from '@xyflow/react';

type InterviewStage = 'setup' | 'in_progress' | 'report';

interface QuestionState {
  question: Question;
  details?: LeetCodeQuestion;
  code: string;
  language: 'python' | 'java' | 'cpp';
  startTime: number;
  result?: ExecutionResult;
  diagramNodes?: Node[];
  diagramEdges?: Edge[];
  explanation?: string;
}

export default function MockInterview() {
  const navigate = useNavigate();
  const currentUser = useAppStore((state) => state.currentUser);

  const [stage, setStage] = useState<InterviewStage>('setup');
  const [config, setConfig] = useState<InterviewConfig | null>(null);
  const [questions, setQuestions] = useState<QuestionState[]>([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [interviewStartTime, setInterviewStartTime] = useState<number>(0);
  const [isRunning, setIsRunning] = useState(false);
  const [showWarning, setShowWarning] = useState(false);
  const [warningMessage, setWarningMessage] = useState('');

  useEffect(() => {
    if (!currentUser) {
      navigate('/login');
    }
  }, [currentUser, navigate]);

  const handleStartInterview = async (interviewConfig: InterviewConfig) => {
    setConfig(interviewConfig);

    // Get questions
    let selectedQuestions: Question[] = [];
    
    if (interviewConfig.questionSelection === 'random') {
      const allQuestions = await api.getQuestions(
        interviewConfig.category === 'leetcode' ? 'leetcode' : 'ml_system_design',
        interviewConfig.category === 'leetcode' ? 'medium' : undefined
      );

      const shuffled = [...allQuestions].sort(() => Math.random() - 0.5);
      selectedQuestions = shuffled.slice(0, interviewConfig.questionCount);
    } else {
      selectedQuestions = await Promise.all(
        interviewConfig.selectedQuestions.map((id) =>
          api.getQuestions(
            interviewConfig.category === 'leetcode' ? 'leetcode' : 'ml_system_design'
          ).then((questions) => questions.find((q) => q.id === id)!)
        )
      );
    }

    // Initialize question states
    const questionStates: QuestionState[] = await Promise.all(
      selectedQuestions.map(async (q) => {
        let details;
        let code = '';

        if (interviewConfig.category === 'leetcode') {
          details = await api.getLeetCodeDetails(q.id);
          code = details.function_signature_python || '';
        }

        return {
          question: q,
          details,
          code,
          language: 'python' as const,
          startTime: Date.now(),
        };
      })
    );

    setQuestions(questionStates);
    setCurrentQuestionIndex(0);
    setInterviewStartTime(Date.now());
    setStage('in_progress');
  };

  const handleTimeUp = () => {
    setStage('report');
  };

  const handleWarning = (minutesLeft: number) => {
    setShowWarning(true);
    setWarningMessage(`${minutesLeft} minute${minutesLeft > 1 ? 's' : ''} remaining!`);
    setTimeout(() => setShowWarning(false), 3000);
  };

  const handleRunCode = async () => {
    if (!config || config.category !== 'leetcode') return;

    const current = questions[currentQuestionIndex];
    if (!current.details) return;

    setIsRunning(true);

    try {
      const testCases = JSON.parse(current.details.test_cases);
      const result = await api.executeCode({
        code: current.code,
        language: current.language,
        testCases,
        questionId: current.question.id,
      });

      setQuestions((prev) =>
        prev.map((q, i) =>
          i === currentQuestionIndex ? { ...q, result } : q
        )
      );
    } catch (error) {
      console.error('Failed to run code:', error);
    } finally {
      setIsRunning(false);
    }
  };

  const handleSubmitQuestion = async () => {
    const current = questions[currentQuestionIndex];
    
    if (config?.category === 'leetcode' && !current.result) {
      await handleRunCode();
    }

    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex((i) => i + 1);
    } else {
      setStage('report');
    }
  };

  const handleGenerateFeedback = async () => {
    alert('AI Feedback generation - to be implemented with Claude API');
  };

  const handleSaveSession = async () => {
    console.log('Saving session...', questions);
    await new Promise((resolve) => setTimeout(resolve, 1000));
  };

  const handleViewSolutions = () => {
    alert('View solutions - to be implemented');
  };

  const handleClose = () => {
    navigate('/');
  };

  if (stage === 'setup') {
    return (
      <MockInterviewSetup
        onStart={handleStartInterview}
        onCancel={() => navigate('/')}
      />
    );
  }

  if (stage === 'report') {
    const questionResults = questions.map((q, index) => ({
      questionId: q.question.id,
      questionTitle: q.question.title,
      timeSpent: index < currentQuestionIndex
        ? (questions[index + 1]?.startTime || Date.now()) - q.startTime
        : Date.now() - q.startTime,
      completed: index <= currentQuestionIndex,
      result: q.result,
      code: q.code,
    }));

    return (
      <MockInterviewReport
        category={config!.category}
        duration={config!.duration * 60}
        questionResults={questionResults}
        onGenerateFeedback={handleGenerateFeedback}
        onSaveSession={handleSaveSession}
        onViewSolutions={handleViewSolutions}
        onClose={handleClose}
      />
    );
  }

  const current = questions[currentQuestionIndex];
  if (!current) return null;

  return (
    <div className="h-screen flex flex-col bg-gray-900">
      {/* Header with Timer */}
      <div className="flex items-center justify-between px-6 py-4 bg-gray-800 border-b border-gray-700">
        <div className="flex items-center gap-4">
          <button
            onClick={() => {
              if (window.confirm('Exit interview? Progress will be lost.')) {
                navigate('/');
              }
            }}
            className="p-2 hover:bg-gray-700 rounded-lg transition-colors"
          >
            <ArrowLeft size={20} className="text-gray-400" />
          </button>
          <div>
            <h2 className="text-white font-semibold">
              Question {currentQuestionIndex + 1} of {questions.length}
            </h2>
            <p className="text-sm text-gray-400">{current.question.title}</p>
          </div>
        </div>

        <Timer
          duration={config!.duration * 60}
          onTimeUp={handleTimeUp}
          onWarning={handleWarning}
        />
      </div>

      {/* Warning Notification */}
      {showWarning && (
        <div className="absolute top-20 right-6 bg-orange-500 text-white px-6 py-3 rounded-lg shadow-lg flex items-center gap-2 z-50 animate-pulse">
          <AlertCircle size={20} />
          {warningMessage}
        </div>
      )}

      {/* Content */}
      <div className="flex-1 overflow-hidden">
        {config?.category === 'leetcode' ? (
          <div className="h-full flex flex-col">
            <div className="h-2/3 border-b border-gray-700">
              <CodeEditor
                code={current.code}
                language={current.language}
                onChange={(code) =>
                  setQuestions((prev) =>
                    prev.map((q, i) =>
                      i === currentQuestionIndex ? { ...q, code } : q
                    )
                  )
                }
                onLanguageChange={(lang) =>
                  setQuestions((prev) =>
                    prev.map((q, i) =>
                      i === currentQuestionIndex ? { ...q, language: lang } : q
                    )
                  )
                }
                onRun={handleRunCode}
                onSubmit={handleSubmitQuestion}
                isRunning={isRunning}
              />
            </div>

            <div className="h-1/3">
              <TestRunner results={current.result || null} isRunning={isRunning} />
            </div>
          </div>
        ) : (
          <div className="h-full flex flex-col">
            <div className="h-[60%] border-b border-gray-700">
              <DiagramEditor
                initialNodes={current.diagramNodes}
                initialEdges={current.diagramEdges}
                onSave={(nodes, edges) =>
                  setQuestions((prev) =>
                    prev.map((q, i) =>
                      i === currentQuestionIndex
                        ? { ...q, diagramNodes: nodes, diagramEdges: edges }
                        : q
                    )
                  )
                }
              />
            </div>

            <div className="h-[40%] bg-gray-900 p-6 overflow-y-auto">
              <h3 className="text-white font-semibold mb-3">Your Explanation</h3>
              <textarea
                value={current.explanation || ''}
                onChange={(e) =>
                  setQuestions((prev) =>
                    prev.map((q, i) =>
                      i === currentQuestionIndex
                        ? { ...q, explanation: e.target.value }
                        : q
                    )
                  )
                }
                placeholder="Explain your system design: requirements, architecture, data flow, scaling, trade-offs..."
                className="w-full h-[calc(100%-80px)] bg-gray-800 text-white p-4 rounded-lg border border-gray-700 focus:border-blue-500 focus:outline-none resize-none"
              />

              <div className="mt-4">
                <button
                  onClick={handleSubmitQuestion}
                  className="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors"
                >
                  {currentQuestionIndex < questions.length - 1
                    ? 'Next Question'
                    : 'Finish Interview'}
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
