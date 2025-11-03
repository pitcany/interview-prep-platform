import React, { useState, useEffect } from 'react';
import { Clock, Brain, Code, ArrowRight, Shuffle, ChevronDown } from 'lucide-react';
import { api } from '../../services/api';
import type { Question } from '../../types';

interface MockInterviewSetupProps {
  onStart: (config: InterviewConfig) => void;
  onCancel: () => void;
}

export interface InterviewConfig {
  category: 'leetcode' | 'ml_system_design';
  duration: number; // in minutes
  questionSelection: 'random' | 'manual';
  selectedQuestions: number[]; // question IDs
  questionCount: number; // 2 for leetcode, 1 for ML
}

export default function MockInterviewSetup({ onStart, onCancel }: MockInterviewSetupProps) {
  const [category, setCategory] = useState<'leetcode' | 'ml_system_design'>('leetcode');
  const [duration, setDuration] = useState(30);
  const [questionSelection, setQuestionSelection] = useState<'random' | 'manual'>('random');
  const [availableQuestions, setAvailableQuestions] = useState<Question[]>([]);
  const [selectedQuestions, setSelectedQuestions] = useState<number[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const questionCount = category === 'leetcode' ? 2 : 1;

  useEffect(() => {
    if (questionSelection === 'manual') {
      loadQuestions();
    }
  }, [category, questionSelection]);

  const loadQuestions = async () => {
    setIsLoading(true);
    try {
      const difficulty = category === 'leetcode' ? 'medium' : undefined;
      const questions = await api.getQuestions(
        category === 'leetcode' ? 'leetcode' : 'ml_system_design',
        difficulty
      );
      setAvailableQuestions(questions);
    } catch (error) {
      console.error('Failed to load questions:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleQuestionToggle = (questionId: number) => {
    setSelectedQuestions((prev) => {
      if (prev.includes(questionId)) {
        return prev.filter((id) => id !== questionId);
      } else if (prev.length < questionCount) {
        return [...prev, questionId];
      }
      return prev;
    });
  };

  const handleStart = () => {
    if (questionSelection === 'manual' && selectedQuestions.length !== questionCount) {
      alert(`Please select exactly ${questionCount} question(s)`);
      return;
    }

    const config: InterviewConfig = {
      category,
      duration,
      questionSelection,
      selectedQuestions: questionSelection === 'manual' ? selectedQuestions : [],
      questionCount,
    };

    onStart(config);
  };

  const canStart = questionSelection === 'random' || selectedQuestions.length === questionCount;

  return (
    <div className="min-h-screen bg-gray-900 p-8">
      <div className="max-w-3xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-white mb-2">
            Start Mock Interview
          </h1>
          <p className="text-gray-400">
            Configure your interview settings and begin practicing
          </p>
        </div>

        <div className="bg-gray-800 rounded-lg border border-gray-700 p-8 space-y-8">
          {/* Category Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-3">
              Interview Type
            </label>
            <div className="grid grid-cols-2 gap-4">
              <button
                onClick={() => setCategory('leetcode')}
                className={`p-6 rounded-lg border-2 transition-all ${
                  category === 'leetcode'
                    ? 'border-blue-500 bg-blue-500/10'
                    : 'border-gray-700 hover:border-gray-600'
                }`}
              >
                <Code className="mx-auto mb-3 text-blue-500" size={32} />
                <div className="text-white font-semibold mb-1">LeetCode</div>
                <div className="text-sm text-gray-400">2 Medium Problems</div>
              </button>

              <button
                onClick={() => setCategory('ml_system_design')}
                className={`p-6 rounded-lg border-2 transition-all ${
                  category === 'ml_system_design'
                    ? 'border-purple-500 bg-purple-500/10'
                    : 'border-gray-700 hover:border-gray-600'
                }`}
              >
                <Brain className="mx-auto mb-3 text-purple-500" size={32} />
                <div className="text-white font-semibold mb-1">ML System Design</div>
                <div className="text-sm text-gray-400">1 Design Question</div>
              </button>
            </div>
          </div>

          {/* Duration Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-3">
              Duration
            </label>
            <div className="grid grid-cols-3 gap-4">
              {[30, 45, 60].map((mins) => (
                <button
                  key={mins}
                  onClick={() => setDuration(mins)}
                  className={`p-4 rounded-lg border-2 transition-all ${
                    duration === mins
                      ? 'border-blue-500 bg-blue-500/10'
                      : 'border-gray-700 hover:border-gray-600'
                  }`}
                >
                  <Clock className="mx-auto mb-2 text-gray-400" size={24} />
                  <div className="text-white font-semibold">{mins} min</div>
                </button>
              ))}
            </div>
          </div>

          {/* Question Selection Method */}
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-3">
              Question Selection
            </label>
            <div className="grid grid-cols-2 gap-4">
              <button
                onClick={() => setQuestionSelection('random')}
                className={`p-4 rounded-lg border-2 transition-all ${
                  questionSelection === 'random'
                    ? 'border-blue-500 bg-blue-500/10'
                    : 'border-gray-700 hover:border-gray-600'
                }`}
              >
                <Shuffle className="mx-auto mb-2 text-gray-400" size={24} />
                <div className="text-white font-medium mb-1">Random</div>
                <div className="text-xs text-gray-400">
                  Surprise me with questions
                </div>
              </button>

              <button
                onClick={() => setQuestionSelection('manual')}
                className={`p-4 rounded-lg border-2 transition-all ${
                  questionSelection === 'manual'
                    ? 'border-blue-500 bg-blue-500/10'
                    : 'border-gray-700 hover:border-gray-600'
                }`}
              >
                <ChevronDown className="mx-auto mb-2 text-gray-400" size={24} />
                <div className="text-white font-medium mb-1">Choose</div>
                <div className="text-xs text-gray-400">
                  Pick specific questions
                </div>
              </button>
            </div>
          </div>

          {/* Manual Question Selection */}
          {questionSelection === 'manual' && (
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-3">
                Select {questionCount} Question{questionCount > 1 ? 's' : ''}
                {selectedQuestions.length > 0 && (
                  <span className="ml-2 text-blue-500">
                    ({selectedQuestions.length}/{questionCount} selected)
                  </span>
                )}
              </label>
              
              {isLoading ? (
                <div className="text-center py-8 text-gray-400">
                  Loading questions...
                </div>
              ) : (
                <div className="space-y-2 max-h-64 overflow-y-auto">
                  {availableQuestions.map((question) => (
                    <button
                      key={question.id}
                      onClick={() => handleQuestionToggle(question.id)}
                      disabled={
                        !selectedQuestions.includes(question.id) &&
                        selectedQuestions.length >= questionCount
                      }
                      className={`w-full text-left p-3 rounded-lg border transition-all ${
                        selectedQuestions.includes(question.id)
                          ? 'border-blue-500 bg-blue-500/10'
                          : 'border-gray-700 hover:border-gray-600'
                      } disabled:opacity-50 disabled:cursor-not-allowed`}
                    >
                      <div className="flex items-center justify-between">
                        <span className="text-white font-medium">
                          {question.title}
                        </span>
                        <span
                          className={`text-xs px-2 py-1 rounded ${
                            question.difficulty === 'easy'
                              ? 'bg-green-500/20 text-green-500'
                              : question.difficulty === 'medium'
                              ? 'bg-yellow-500/20 text-yellow-500'
                              : 'bg-red-500/20 text-red-500'
                          }`}
                        >
                          {question.difficulty}
                        </span>
                      </div>
                    </button>
                  ))}
                </div>
              )}
            </div>
          )}

          {/* Instructions */}
          <div className="bg-gray-900 rounded-lg p-4 border border-gray-700">
            <h3 className="text-white font-semibold mb-2">Instructions</h3>
            <ul className="text-sm text-gray-400 space-y-1">
              <li>• You cannot switch between questions during the interview</li>
              <li>• Timer warnings at 10, 5, and 1 minute remaining</li>
              <li>• Interview auto-submits when time expires</li>
              <li>• AI feedback generated after completion</li>
              <li>• You can save the session for later review</li>
            </ul>
          </div>

          {/* Action Buttons */}
          <div className="flex gap-4">
            <button
              onClick={onCancel}
              className="flex-1 px-6 py-3 bg-gray-700 hover:bg-gray-600 text-white rounded-lg transition-colors"
            >
              Cancel
            </button>
            <button
              onClick={handleStart}
              disabled={!canStart}
              className="flex-1 px-6 py-3 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-700 disabled:cursor-not-allowed text-white rounded-lg transition-colors flex items-center justify-center gap-2"
            >
              Start Interview
              <ArrowRight size={20} />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
