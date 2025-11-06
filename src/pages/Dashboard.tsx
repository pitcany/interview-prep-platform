import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppStore } from '../store';
import { api } from '../services/api';
import { Code, Brain, Clock, TrendingUp, Award, Target } from 'lucide-react';
import type { UserStats, Feedback } from '../types';

export default function Dashboard() {
  const navigate = useNavigate();
  const currentUser = useAppStore((state) => state.currentUser);
  const [stats, setStats] = useState<UserStats | null>(null);
  const [recentFeedback, setRecentFeedback] = useState<Feedback[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    if (!currentUser) return;

    try {
      setIsLoading(true);
      const [userStats, feedback] = await Promise.all([
        api.getUserStats(currentUser.id),
        api.getUserFeedback(currentUser.id, 5),
      ]);
      setStats(userStats);
      setRecentFeedback(feedback);
    } catch (error) {
      console.error('Failed to load dashboard data:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const calculateSuccessRate = () => {
    if (!stats || stats.total_attempts === 0) return 0;
    return Math.round((stats.solved_count / stats.total_attempts) * 100);
  };

  const quickActions = [
    {
      title: 'LeetCode Practice',
      description: 'Practice coding problems',
      icon: Code,
      color: 'blue',
      path: '/practice/leetcode',
    },
    {
      title: 'ML System Design',
      description: 'Design ML systems',
      icon: Brain,
      color: 'purple',
      path: '/practice/ml_system_design',
    },
    {
      title: 'Mock Interview',
      description: 'Timed interview practice',
      icon: Clock,
      color: 'green',
      path: '/mock-interview',
    },
  ];

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-gray-400">Loading...</div>
      </div>
    );
  }

  return (
    <div className="p-8 max-w-7xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-white mb-2">
          Welcome back, {currentUser?.username}!
        </h1>
        <p className="text-gray-400">
          Ready to level up your interview skills?
        </p>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
          <div className="flex items-center justify-between mb-2">
            <Target className="text-blue-500" size={24} />
          </div>
          <p className="text-2xl font-bold text-white">
            {stats?.total_attempts || 0}
          </p>
          <p className="text-sm text-gray-400">Total Attempts</p>
        </div>

        <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
          <div className="flex items-center justify-between mb-2">
            <Award className="text-green-500" size={24} />
          </div>
          <p className="text-2xl font-bold text-white">
            {stats?.solved_count || 0}
          </p>
          <p className="text-sm text-gray-400">Problems Solved</p>
        </div>

        <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
          <div className="flex items-center justify-between mb-2">
            <TrendingUp className="text-purple-500" size={24} />
          </div>
          <p className="text-2xl font-bold text-white">
            {calculateSuccessRate()}%
          </p>
          <p className="text-sm text-gray-400">Success Rate</p>
        </div>

        <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
          <div className="flex items-center justify-between mb-2">
            <Clock className="text-orange-500" size={24} />
          </div>
          <p className="text-2xl font-bold text-white">
            {Math.round((stats?.total_time_spent || 0) / 60)}m
          </p>
          <p className="text-sm text-gray-400">Time Spent</p>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="mb-8">
        <h2 className="text-xl font-bold text-white mb-4">Quick Actions</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {quickActions.map((action) => {
            const Icon = action.icon;
            return (
              <button
                key={action.path}
                onClick={() => navigate(action.path)}
                className="bg-gray-800 hover:bg-gray-700 border border-gray-700 rounded-lg p-6 text-left transition-colors"
              >
                <div
                  className={`w-12 h-12 rounded-lg bg-${action.color}-500/10 flex items-center justify-center mb-4`}
                >
                  <Icon
                    className={`text-${action.color}-500`}
                    size={24}
                  />
                </div>
                <h3 className="text-lg font-semibold text-white mb-1">
                  {action.title}
                </h3>
                <p className="text-sm text-gray-400">{action.description}</p>
              </button>
            );
          })}
        </div>
      </div>

      {/* Recent Feedback */}
      {recentFeedback.length > 0 && (
        <div>
          <h2 className="text-xl font-bold text-white mb-4">Recent Feedback</h2>
          <div className="space-y-4">
            {recentFeedback.map((feedback) => (
              <div
                key={feedback.id}
                className="bg-gray-800 border border-gray-700 rounded-lg p-6"
              >
                <div className="flex items-start justify-between mb-2">
                  <h3 className="font-semibold text-white">
                    {feedback.question_title}
                  </h3>
                  <span className="text-xs text-gray-400">
                    {new Date(feedback.generated_at).toLocaleDateString()}
                  </span>
                </div>
                <div className="flex gap-2 mb-3">
                  {Object.entries(JSON.parse(feedback.scores as any) || {}).map(
                    ([key, value]) => (
                      <span
                        key={key}
                        className="px-2 py-1 bg-gray-700 rounded text-xs text-gray-300"
                      >
                        {key}: {value}/10
                      </span>
                    )
                  )}
                </div>
                <p className="text-sm text-gray-400 line-clamp-2">
                  {JSON.parse(feedback.strengths as any)?.[0] ||
                    'No strengths recorded'}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Empty State */}
      {stats?.total_attempts === 0 && (
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-12 text-center">
          <Code className="mx-auto mb-4 text-gray-500" size={48} />
          <h3 className="text-xl font-semibold text-white mb-2">
            Start Your Journey
          </h3>
          <p className="text-gray-400 mb-6">
            Begin practicing with LeetCode problems or ML system design questions
          </p>
          <button
            onClick={() => navigate('/practice')}
            className="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors"
          >
            Start Practicing
          </button>
        </div>
      )}
    </div>
  );
}
