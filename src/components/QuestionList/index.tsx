import React, { useEffect, useState } from 'react';
import { api } from '../../services/api';
import { CheckCircle2, Circle } from 'lucide-react';
import type { Question, UserProgress } from '../../types';

interface QuestionListProps {
  category: 'leetcode' | 'ml_system_design';
  onSelectQuestion: (question: Question) => void;
  selectedQuestionId?: number;
  userId: number;
  onCategoryChange?: (category: 'leetcode' | 'ml_system_design') => void;
}

export default function QuestionList({
  category,
  onSelectQuestion,
  selectedQuestionId,
  userId,
  onCategoryChange,
}: QuestionListProps) {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [progress, setProgress] = useState<UserProgress[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [filter, setFilter] = useState<'all' | 'easy' | 'medium' | 'hard'>('all');
  const [statusFilter, setStatusFilter] = useState<'all' | 'solved' | 'unsolved'>('all');

  useEffect(() => {
    loadData();
  }, [category, filter, userId]);

  const loadData = async () => {
    try {
      setIsLoading(true);
      const difficultyFilter = filter === 'all' ? undefined : filter;
      const [questionsData, progressData] = await Promise.all([
        api.getQuestions(category, difficultyFilter),
        api.getUserProgress(userId),
      ]);
      setQuestions(questionsData);
      setProgress(progressData);
    } catch (error) {
      console.error('Failed to load questions:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const isQuestionSolved = (questionId: number) => {
    return progress.some((p) => p.question_id === questionId && p.solved);
  };

  const getQuestionAttempts = (questionId: number) => {
    return progress.find((p) => p.question_id === questionId)?.attempts || 0;
  };

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'easy':
        return 'text-green-500 bg-green-500/10';
      case 'medium':
        return 'text-yellow-500 bg-yellow-500/10';
      case 'hard':
        return 'text-red-500 bg-red-500/10';
      default:
        return 'text-gray-500 bg-gray-500/10';
    }
  };

  const filteredQuestions = questions.filter((q) => {
    if (statusFilter === 'solved') return isQuestionSolved(q.id);
    if (statusFilter === 'unsolved') return !isQuestionSolved(q.id);
    return true;
  });

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-gray-400">Loading questions...</div>
      </div>
    );
  }

  return (
    <div className="flex flex-col h-full">
      {/* Header */}
      <div className="p-4 border-b border-gray-700">
        <h2 className="text-lg font-bold text-white mb-3">Practice</h2>

        {/* Category toggle */}
        {onCategoryChange && (
          <div className="flex gap-2 mb-3">
            <button
              onClick={() => onCategoryChange('leetcode')}
              className={`flex-1 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                category === 'leetcode'
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
              }`}
            >
              LeetCode
            </button>
            <button
              onClick={() => onCategoryChange('ml_system_design')}
              className={`flex-1 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                category === 'ml_system_design'
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
              }`}
            >
              ML Design
            </button>
          </div>
        )}

        {/* Difficulty filter */}
        <div className="flex gap-2 mb-2">
          {(['all', 'easy', 'medium', 'hard'] as const).map((level) => (
            <button
              key={level}
              onClick={() => setFilter(level)}
              className={`px-3 py-1 rounded-lg text-sm transition-colors ${
                filter === level
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
              }`}
            >
              {level.charAt(0).toUpperCase() + level.slice(1)}
            </button>
          ))}
        </div>

        {/* Status filter */}
        <div className="flex gap-2">
          {(['all', 'solved', 'unsolved'] as const).map((status) => (
            <button
              key={status}
              onClick={() => setStatusFilter(status)}
              className={`px-3 py-1 rounded-lg text-sm transition-colors ${
                statusFilter === status
                  ? 'bg-purple-600 text-white'
                  : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
              }`}
            >
              {status.charAt(0).toUpperCase() + status.slice(1)}
            </button>
          ))}
        </div>
      </div>

      {/* Question list */}
      <div className="flex-1 overflow-y-auto p-4 space-y-2">
        {filteredQuestions.length === 0 ? (
          <div className="text-center py-8 text-gray-400">
            No questions found
          </div>
        ) : (
          filteredQuestions.map((question) => {
            const solved = isQuestionSolved(question.id);
            const attempts = getQuestionAttempts(question.id);

            return (
              <button
                key={question.id}
                onClick={() => onSelectQuestion(question)}
                className={`w-full text-left p-3 rounded-lg transition-colors border ${
                  selectedQuestionId === question.id
                    ? 'bg-gray-700 border-blue-500'
                    : 'bg-gray-800 border-gray-700 hover:bg-gray-750'
                }`}
              >
                <div className="flex items-start gap-3">
                  {/* Status icon */}
                  <div className="mt-1">
                    {solved ? (
                      <CheckCircle2 className="text-green-500" size={20} />
                    ) : (
                      <Circle className="text-gray-600" size={20} />
                    )}
                  </div>

                  <div className="flex-1 min-w-0">
                    <h3 className="font-medium text-white truncate mb-1">
                      {question.title}
                    </h3>

                    <div className="flex items-center gap-2 flex-wrap">
                      <span
                        className={`text-xs px-2 py-0.5 rounded font-medium ${getDifficultyColor(
                          question.difficulty
                        )}`}
                      >
                        {question.difficulty}
                      </span>

                      {attempts > 0 && (
                        <span className="text-xs text-gray-400">
                          {attempts} {attempts === 1 ? 'attempt' : 'attempts'}
                        </span>
                      )}
                    </div>

                    {question.tags && (
                      <div className="flex gap-1 flex-wrap mt-2">
                        {JSON.parse(question.tags).slice(0, 3).map((tag: string) => (
                          <span
                            key={tag}
                            className="text-xs px-2 py-0.5 bg-gray-700 text-gray-400 rounded"
                          >
                            {tag}
                          </span>
                        ))}
                      </div>
                    )}
                  </div>
                </div>
              </button>
            );
          })
        )}
      </div>

      {/* Stats footer */}
      <div className="p-4 border-t border-gray-700 bg-gray-800">
        <div className="flex justify-between text-sm">
          <span className="text-gray-400">
            Solved: {progress.filter((p) => p.solved).length}
          </span>
          <span className="text-gray-400">Total: {questions.length}</span>
        </div>
      </div>
    </div>
  );
}
