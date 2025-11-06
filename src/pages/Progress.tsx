import React, { useEffect, useState } from 'react';
import { useAppStore } from '../store';
import { api } from '../services/api';
import { 
  TrendingUp, 
  Award, 
  Target, 
  Clock, 
  Calendar, 
  CheckCircle2,
  XCircle,
  Code,
  Brain,
  RotateCcw
} from 'lucide-react';
import { PieChart, Pie, Cell, BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import type { UserStats, UserProgress, Feedback } from '../types';
import { ConfirmModal } from '../components/ConfirmModal';

export default function Progress() {
  const currentUser = useAppStore((state) => state.currentUser);
  const [stats, setStats] = useState<UserStats | null>(null);
  const [progress, setProgress] = useState<UserProgress[]>([]);
  const [recentFeedback, setRecentFeedback] = useState<Feedback[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'overview' | 'problems' | 'feedback'>('overview');
  const [showResetModal, setShowResetModal] = useState(false);
  const [isResetting, setIsResetting] = useState(false);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    if (!currentUser) return;

    try {
      setIsLoading(true);
      const [userStats, userProgress, feedback] = await Promise.all([
        api.getUserStats(currentUser.id),
        api.getUserProgress(currentUser.id),
        api.getUserFeedback(currentUser.id, 10),
      ]);
      setStats(userStats);
      setProgress(userProgress);
      setRecentFeedback(feedback);
    } catch (error) {
      console.error('Failed to load progress data:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const getDifficultyData = () => {
    if (!stats) return [];
    
    return stats.byDifficulty.map((item) => ({
      name: item.difficulty.charAt(0).toUpperCase() + item.difficulty.slice(1),
      value: item.solved,
      total: item.attempts,
    }));
  };

  const getCategoryData = () => {
    const leetcode = progress.filter((p) => p.category === 'leetcode');
    const mlDesign = progress.filter((p) => p.category === 'ml_system_design');
    
    return [
      {
        name: 'LeetCode',
        solved: leetcode.filter((p) => p.solved).length,
        attempted: leetcode.length,
      },
      {
        name: 'ML Design',
        solved: mlDesign.filter((p) => p.solved).length,
        attempted: mlDesign.length,
      },
    ];
  };

  const getSuccessRate = () => {
    if (!stats || stats.total_attempts === 0) return 0;
    return Math.round((stats.solved_count / stats.total_attempts) * 100);
  };

  const handleResetProgress = async () => {
    if (!currentUser) return;

    setIsResetting(true);
    try {
      await api.resetUserProgress(currentUser.id);
      setShowResetModal(false);
      // Reload data after reset
      await loadData();
    } catch (error) {
      console.error('Failed to reset progress:', error);
      alert('Failed to reset progress. Please try again.');
    } finally {
      setIsResetting(false);
    }
  };

  const COLORS = {
    easy: '#22c55e',
    medium: '#eab308',
    hard: '#ef4444',
    solved: '#3b82f6',
    attempted: '#6b7280',
  };

  if (!currentUser) {
    return null;
  }

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-gray-400">Loading progress...</div>
      </div>
    );
  }

  return (
    <div className="h-screen flex flex-col bg-gray-900 overflow-hidden">
      {/* Header */}
      <div className="px-8 py-6 bg-gray-800 border-b border-gray-700">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-white mb-2">Your Progress</h1>
            <p className="text-gray-400">
              Track your performance and improvement over time
            </p>
          </div>
          <button
            onClick={() => setShowResetModal(true)}
            className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg transition-colors flex items-center gap-2"
            title="Reset all progress, submissions, and mock interviews"
          >
            <RotateCcw size={18} />
            Reset Progress
          </button>
        </div>
      </div>

      {/* Tabs */}
      <div className="px-8 py-3 bg-gray-800 border-b border-gray-700">
        <div className="flex gap-4">
          {(['overview', 'problems', 'feedback'] as const).map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                activeTab === tab
                  ? 'bg-blue-600 text-white'
                  : 'text-gray-400 hover:text-white hover:bg-gray-700'
              }`}
            >
              {tab.charAt(0).toUpperCase() + tab.slice(1)}
            </button>
          ))}
        </div>
      </div>

      {/* Content */}
      <div className="flex-1 overflow-y-auto p-8">
        {activeTab === 'overview' && (
          <div className="space-y-8 max-w-7xl mx-auto">
            {/* Stats Grid */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
              <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
                <div className="flex items-center justify-between mb-2">
                  <Target className="text-blue-500" size={24} />
                </div>
                <p className="text-3xl font-bold text-white">
                  {stats?.total_attempts || 0}
                </p>
                <p className="text-sm text-gray-400">Total Attempts</p>
              </div>

              <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
                <div className="flex items-center justify-between mb-2">
                  <Award className="text-green-500" size={24} />
                </div>
                <p className="text-3xl font-bold text-white">
                  {stats?.solved_count || 0}
                </p>
                <p className="text-sm text-gray-400">Problems Solved</p>
              </div>

              <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
                <div className="flex items-center justify-between mb-2">
                  <TrendingUp className="text-purple-500" size={24} />
                </div>
                <p className="text-3xl font-bold text-white">
                  {getSuccessRate()}%
                </p>
                <p className="text-sm text-gray-400">Success Rate</p>
              </div>

              <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
                <div className="flex items-center justify-between mb-2">
                  <Clock className="text-orange-500" size={24} />
                </div>
                <p className="text-3xl font-bold text-white">
                  {Math.round((stats?.total_time_spent || 0) / 60)}m
                </p>
                <p className="text-sm text-gray-400">Time Spent</p>
              </div>
            </div>

            {/* Charts Row */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* Difficulty Breakdown */}
              <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
                <h2 className="text-xl font-bold text-white mb-4">
                  Solved by Difficulty
                </h2>
                <ResponsiveContainer width="100%" height={300}>
                  <PieChart>
                    <Pie
                      data={getDifficultyData()}
                      cx="50%"
                      cy="50%"
                      labelLine={false}
                      label={({ name, value }) => `${name}: ${value}`}
                      outerRadius={80}
                      fill="#8884d8"
                      dataKey="value"
                    >
                      {getDifficultyData().map((entry, index) => (
                        <Cell 
                          key={`cell-${index}`} 
                          fill={COLORS[entry.name.toLowerCase() as keyof typeof COLORS]} 
                        />
                      ))}
                    </Pie>
                    <Tooltip />
                  </PieChart>
                </ResponsiveContainer>
              </div>

              {/* Category Breakdown */}
              <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
                <h2 className="text-xl font-bold text-white mb-4">
                  Progress by Category
                </h2>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={getCategoryData()}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                    <XAxis dataKey="name" stroke="#9ca3af" />
                    <YAxis stroke="#9ca3af" />
                    <Tooltip 
                      contentStyle={{ 
                        backgroundColor: '#1f2937', 
                        border: '1px solid #374151',
                        borderRadius: '8px',
                        color: '#fff'
                      }}
                    />
                    <Legend />
                    <Bar dataKey="solved" fill={COLORS.solved} name="Solved" />
                    <Bar dataKey="attempted" fill={COLORS.attempted} name="Attempted" />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>

            {/* Recent Activity */}
            <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
              <h2 className="text-xl font-bold text-white mb-4">
                Recent Activity
              </h2>
              <div className="space-y-3">
                {progress.slice(0, 10).map((item) => (
                  <div
                    key={item.id}
                    className="flex items-center justify-between p-4 bg-gray-700 rounded-lg"
                  >
                    <div className="flex items-center gap-3">
                      {item.solved ? (
                        <CheckCircle2 className="text-green-500" size={20} />
                      ) : (
                        <XCircle className="text-red-500" size={20} />
                      )}
                      <div>
                        <h3 className="text-white font-medium">{item.title}</h3>
                        <div className="flex items-center gap-2 mt-1">
                          <span className={`text-xs px-2 py-0.5 rounded ${
                            item.difficulty === 'easy' ? 'bg-green-500/20 text-green-500' :
                            item.difficulty === 'medium' ? 'bg-yellow-500/20 text-yellow-500' :
                            'bg-red-500/20 text-red-500'
                          }`}>
                            {item.difficulty}
                          </span>
                          <span className="text-xs text-gray-400">
                            {item.attempts} {item.attempts === 1 ? 'attempt' : 'attempts'}
                          </span>
                        </div>
                      </div>
                    </div>
                    <div className="text-sm text-gray-400">
                      {new Date(item.last_attempt_at).toLocaleDateString()}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {activeTab === 'problems' && (
          <div className="max-w-7xl mx-auto">
            <div className="bg-gray-800 rounded-lg border border-gray-700 overflow-hidden">
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead className="bg-gray-700 border-b border-gray-700">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                        Status
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                        Problem
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                        Difficulty
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                        Category
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                        Attempts
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                        Last Attempt
                      </th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-700">
                    {progress.map((item) => (
                      <tr key={item.id} className="hover:bg-gray-750 transition-colors">
                        <td className="px-6 py-4 whitespace-nowrap">
                          {item.solved ? (
                            <CheckCircle2 className="text-green-500" size={20} />
                          ) : (
                            <XCircle className="text-gray-600" size={20} />
                          )}
                        </td>
                        <td className="px-6 py-4">
                          <div className="text-white font-medium">{item.title}</div>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <span className={`px-2 py-1 text-xs rounded font-medium ${
                            item.difficulty === 'easy' ? 'bg-green-500/20 text-green-500' :
                            item.difficulty === 'medium' ? 'bg-yellow-500/20 text-yellow-500' :
                            'bg-red-500/20 text-red-500'
                          }`}>
                            {item.difficulty}
                          </span>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <div className="flex items-center gap-2">
                            {item.category === 'leetcode' ? (
                              <Code size={16} className="text-blue-500" />
                            ) : (
                              <Brain size={16} className="text-purple-500" />
                            )}
                            <span className="text-gray-400 text-sm">
                              {item.category === 'leetcode' ? 'LeetCode' : 'ML Design'}
                            </span>
                          </div>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-gray-400">
                          {item.attempts}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-gray-400 text-sm">
                          {new Date(item.last_attempt_at).toLocaleDateString()}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'feedback' && (
          <div className="max-w-7xl mx-auto space-y-6">
            {recentFeedback.length === 0 ? (
              <div className="bg-gray-800 rounded-lg border border-gray-700 p-12 text-center">
                <p className="text-gray-400 mb-2">No feedback yet</p>
                <p className="text-sm text-gray-500">
                  Complete and submit problems to receive AI-powered feedback
                </p>
              </div>
            ) : (
              recentFeedback.map((feedback) => (
                <div
                  key={feedback.id}
                  className="bg-gray-800 rounded-lg border border-gray-700 p-6"
                >
                  <div className="flex items-start justify-between mb-4">
                    <div>
                      <h3 className="text-xl font-semibold text-white mb-1">
                        {feedback.question_title}
                      </h3>
                      <p className="text-sm text-gray-400">
                        {new Date(feedback.generated_at).toLocaleDateString()}
                      </p>
                    </div>
                    <div className="flex gap-2">
                      {Object.entries(JSON.parse(feedback.scores as any) || {}).map(
                        ([key, value]) => (
                          <div
                            key={key}
                            className="px-3 py-1 bg-blue-500/20 rounded-lg text-center"
                          >
                            <div className="text-lg font-bold text-blue-400">
                              {value}/10
                            </div>
                            <div className="text-xs text-gray-400">
                              {key.replace(/([A-Z])/g, ' $1').trim()}
                            </div>
                          </div>
                        )
                      )}
                    </div>
                  </div>

                  <div className="space-y-4">
                    {/* Strengths */}
                    {JSON.parse(feedback.strengths as any)?.length > 0 && (
                      <div>
                        <h4 className="font-semibold text-green-400 mb-2 flex items-center gap-2">
                          <CheckCircle2 size={18} />
                          Strengths
                        </h4>
                        <ul className="list-disc list-inside space-y-1 text-gray-300">
                          {JSON.parse(feedback.strengths as any).map((strength: string, i: number) => (
                            <li key={i}>{strength}</li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {/* Improvements */}
                    {JSON.parse(feedback.improvements as any)?.length > 0 && (
                      <div>
                        <h4 className="font-semibold text-orange-400 mb-2 flex items-center gap-2">
                          <TrendingUp size={18} />
                          Areas for Improvement
                        </h4>
                        <ul className="list-disc list-inside space-y-1 text-gray-300">
                          {JSON.parse(feedback.improvements as any).map((improvement: string, i: number) => (
                            <li key={i}>{improvement}</li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {/* Full feedback text */}
                    <details className="mt-4">
                      <summary className="cursor-pointer text-blue-400 hover:text-blue-300 text-sm font-medium">
                        View Full Feedback
                      </summary>
                      <div className="mt-3 text-sm text-gray-300 whitespace-pre-wrap bg-gray-900 p-4 rounded">
                        {feedback.feedback_text}
                      </div>
                    </details>
                  </div>
                </div>
              ))
            )}
          </div>
        )}
      </div>

      {/* Reset Progress Confirmation Modal */}
      <ConfirmModal
        isOpen={showResetModal}
        onCancel={() => setShowResetModal(false)}
        onConfirm={handleResetProgress}
        title="Reset Progress"
        message="Are you sure you want to reset all your progress? This will delete all your:

• Progress data (attempts, solved status)
• Code submissions
• Design submissions
• AI feedback
• Mock interviews

This action cannot be undone."
        confirmText={isResetting ? "Resetting..." : "Reset Progress"}
        cancelText="Cancel"
        variant="danger"
      />
    </div>
  );
}
