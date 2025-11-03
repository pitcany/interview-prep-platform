import React, { useState } from 'react';
import { CheckCircle, XCircle, Clock, Award, Save, Download, ArrowRight } from 'lucide-react';
import type { ExecutionResult } from '../../types';

interface QuestionResult {
  questionId: number;
  questionTitle: string;
  timeSpent: number; // seconds
  completed: boolean;
  result?: ExecutionResult;
  code?: string;
}

interface MockInterviewReportProps {
  category: 'leetcode' | 'ml_system_design';
  duration: number; // total time in seconds
  questionResults: QuestionResult[];
  onGenerateFeedback: () => void;
  onSaveSession: () => void;
  onViewSolutions: () => void;
  onClose: () => void;
}

export default function MockInterviewReport({
  category,
  duration,
  questionResults,
  onGenerateFeedback,
  onSaveSession,
  onViewSolutions,
  onClose,
}: MockInterviewReportProps) {
  const [isSaving, setIsSaving] = useState(false);
  const [saved, setSaved] = useState(false);

  const totalTimeSpent = questionResults.reduce((acc, q) => acc + q.timeSpent, 0);
  const completedCount = questionResults.filter((q) => q.completed).length;
  const passedCount = questionResults.filter(
    (q) => q.result?.status === 'passed'
  ).length;

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}m ${secs}s`;
  };

  const handleSave = async () => {
    setIsSaving(true);
    await onSaveSession();
    setSaved(true);
    setIsSaving(false);
  };

  return (
    <div className="min-h-screen bg-gray-900 p-8">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-white mb-2">
            Interview Complete!
          </h1>
          <p className="text-gray-400">
            Here's how you performed
          </p>
        </div>

        {/* Summary Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
            <div className="flex items-center justify-between mb-2">
              <span className="text-gray-400 text-sm">Time Used</span>
              <Clock className="text-blue-500" size={20} />
            </div>
            <div className="text-2xl font-bold text-white">
              {formatTime(totalTimeSpent)}
            </div>
            <div className="text-xs text-gray-500 mt-1">
              of {formatTime(duration)}
            </div>
          </div>

          <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
            <div className="flex items-center justify-between mb-2">
              <span className="text-gray-400 text-sm">Completed</span>
              <Award className="text-green-500" size={20} />
            </div>
            <div className="text-2xl font-bold text-white">
              {completedCount}/{questionResults.length}
            </div>
            <div className="text-xs text-gray-500 mt-1">
              questions
            </div>
          </div>

          {category === 'leetcode' && (
            <>
              <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
                <div className="flex items-center justify-between mb-2">
                  <span className="text-gray-400 text-sm">Tests Passed</span>
                  <CheckCircle className="text-green-500" size={20} />
                </div>
                <div className="text-2xl font-bold text-white">
                  {passedCount}/{questionResults.length}
                </div>
                <div className="text-xs text-gray-500 mt-1">
                  problems
                </div>
              </div>

              <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
                <div className="flex items-center justify-between mb-2">
                  <span className="text-gray-400 text-sm">Success Rate</span>
                  <Award className="text-purple-500" size={20} />
                </div>
                <div className="text-2xl font-bold text-white">
                  {questionResults.length > 0
                    ? Math.round((passedCount / questionResults.length) * 100)
                    : 0}%
                </div>
              </div>
            </>
          )}
        </div>

        {/* Question Details */}
        <div className="bg-gray-800 rounded-lg border border-gray-700 p-6 mb-8">
          <h2 className="text-xl font-bold text-white mb-4">Question Performance</h2>
          <div className="space-y-4">
            {questionResults.map((question, index) => (
              <div
                key={question.questionId}
                className="bg-gray-900 rounded-lg p-4 border border-gray-700"
              >
                <div className="flex items-start justify-between mb-3">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <span className="text-gray-400 text-sm">
                        Question {index + 1}
                      </span>
                      {question.completed ? (
                        <CheckCircle className="text-green-500" size={16} />
                      ) : (
                        <XCircle className="text-gray-500" size={16} />
                      )}
                    </div>
                    <h3 className="text-white font-semibold">
                      {question.questionTitle}
                    </h3>
                  </div>
                  <div className="text-right">
                    <div className="text-sm text-gray-400">Time Spent</div>
                    <div className="text-white font-semibold">
                      {formatTime(question.timeSpent)}
                    </div>
                  </div>
                </div>

                {category === 'leetcode' && question.result && (
                  <div className="mt-3 pt-3 border-t border-gray-700">
                    <div className="flex items-center justify-between text-sm">
                      <span className="text-gray-400">Test Results:</span>
                      <span
                        className={
                          question.result.status === 'passed'
                            ? 'text-green-500'
                            : 'text-red-500'
                        }
                      >
                        {question.result.testResults.filter((t) => t.passed).length}/
                        {question.result.testResults.length} passed
                      </span>
                    </div>
                    {question.result.executionTime > 0 && (
                      <div className="flex items-center justify-between text-sm mt-1">
                        <span className="text-gray-400">Execution Time:</span>
                        <span className="text-white">
                          {question.result.executionTime}ms
                        </span>
                      </div>
                    )}
                  </div>
                )}

                {!question.completed && (
                  <div className="mt-3 pt-3 border-t border-gray-700">
                    <span className="text-sm text-gray-400">
                      Not completed during interview
                    </span>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Actions */}
        <div className="bg-gray-800 rounded-lg border border-gray-700 p-6">
          <h2 className="text-xl font-bold text-white mb-4">Next Steps</h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {/* Generate Feedback */}
            <button
              onClick={onGenerateFeedback}
              className="p-4 bg-blue-600 hover:bg-blue-700 rounded-lg transition-colors text-left"
            >
              <div className="flex items-center justify-between mb-2">
                <Award className="text-white" size={24} />
                <ArrowRight className="text-white" size={20} />
              </div>
              <div className="text-white font-semibold mb-1">
                Get AI Feedback
              </div>
              <div className="text-sm text-blue-100">
                Detailed analysis of your performance
              </div>
            </button>

            {/* View Solutions */}
            <button
              onClick={onViewSolutions}
              className="p-4 bg-purple-600 hover:bg-purple-700 rounded-lg transition-colors text-left"
            >
              <div className="flex items-center justify-between mb-2">
                <CheckCircle className="text-white" size={24} />
                <ArrowRight className="text-white" size={20} />
              </div>
              <div className="text-white font-semibold mb-1">
                View Solutions
              </div>
              <div className="text-sm text-purple-100">
                See optimal approaches
              </div>
            </button>

            {/* Save Session */}
            <button
              onClick={handleSave}
              disabled={isSaving || saved}
              className={`p-4 rounded-lg transition-colors text-left ${
                saved
                  ? 'bg-green-600'
                  : 'bg-gray-700 hover:bg-gray-600'
              }`}
            >
              <div className="flex items-center justify-between mb-2">
                <Save className="text-white" size={24} />
                {saved && <CheckCircle className="text-white" size={20} />}
              </div>
              <div className="text-white font-semibold mb-1">
                {saved ? 'Session Saved!' : 'Save Session'}
              </div>
              <div className="text-sm text-gray-300">
                {saved ? 'Review anytime in your history' : 'Keep for later review'}
              </div>
            </button>

            {/* Close */}
            <button
              onClick={onClose}
              className="p-4 bg-gray-700 hover:bg-gray-600 rounded-lg transition-colors text-left"
            >
              <div className="flex items-center justify-between mb-2">
                <Download className="text-white" size={24} />
                <ArrowRight className="text-white" size={20} />
              </div>
              <div className="text-white font-semibold mb-1">
                Exit Interview
              </div>
              <div className="text-sm text-gray-300">
                Return to dashboard
              </div>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
