import React, { useState, useEffect } from 'react';
import { useAppStore } from '../store';
import { api } from '../services/api';
import type { User } from '../types';

export default function Login() {
  const [users, setUsers] = useState<User[]>([]);
  const [selectedUser, setSelectedUser] = useState<string>('');
  const [newUsername, setNewUsername] = useState('');
  const [newEmail, setNewEmail] = useState('');
  const [showNewUserForm, setShowNewUserForm] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const setCurrentUser = useAppStore((state) => state.setCurrentUser);

  useEffect(() => {
    loadUsers();
  }, []);

  const loadUsers = async () => {
    try {
      const allUsers = await api.getAllUsers();
      setUsers(allUsers);
    } catch (err: any) {
      setError('Failed to load users: ' + err.message);
    }
  };

  const handleLogin = async () => {
    if (!selectedUser) return;

    setIsLoading(true);
    setError('');

    try {
      const user = await api.loginUser(selectedUser);
      setCurrentUser(user);
    } catch (err: any) {
      setError('Login failed: ' + err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleCreateUser = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!newUsername || !newEmail) {
      setError('Please fill in all fields');
      return;
    }

    setIsLoading(true);
    setError('');

    try {
      const user = await api.createUser({
        username: newUsername,
        email: newEmail,
      });
      setCurrentUser(user);
    } catch (err: any) {
      setError('Failed to create user: ' + err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 flex items-center justify-center p-4">
      <div className="max-w-md w-full bg-gray-800 rounded-lg shadow-xl p-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-white mb-2">
            Interview Prep Platform
          </h1>
          <p className="text-gray-400">
            LeetCode & ML System Design Practice
          </p>
        </div>

        {error && (
          <div className="mb-4 p-3 bg-red-900/50 border border-red-500 rounded text-red-200 text-sm">
            {error}
          </div>
        )}

        {!showNewUserForm ? (
          <div className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-2">
                Select User
              </label>
              <select
                value={selectedUser}
                onChange={(e) => setSelectedUser(e.target.value)}
                className="w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                disabled={isLoading}
              >
                <option value="">Choose a user...</option>
                {users.map((user) => (
                  <option key={user.id} value={user.username}>
                    {user.username} ({user.email})
                  </option>
                ))}
              </select>
            </div>

            <button
              onClick={handleLogin}
              disabled={!selectedUser || isLoading}
              className="w-full py-2 px-4 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-medium rounded-md transition-colors"
            >
              {isLoading ? 'Logging in...' : 'Login'}
            </button>

            <div className="relative">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-gray-600"></div>
              </div>
              <div className="relative flex justify-center text-sm">
                <span className="px-2 bg-gray-800 text-gray-400">Or</span>
              </div>
            </div>

            <button
              onClick={() => setShowNewUserForm(true)}
              className="w-full py-2 px-4 bg-gray-700 hover:bg-gray-600 text-white font-medium rounded-md transition-colors"
            >
              Create New User
            </button>
          </div>
        ) : (
          <form onSubmit={handleCreateUser} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-2">
                Username
              </label>
              <input
                type="text"
                value={newUsername}
                onChange={(e) => setNewUsername(e.target.value)}
                className="w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Enter username"
                disabled={isLoading}
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-300 mb-2">
                Email
              </label>
              <input
                type="email"
                value={newEmail}
                onChange={(e) => setNewEmail(e.target.value)}
                className="w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Enter email"
                disabled={isLoading}
                required
              />
            </div>

            <div className="flex gap-3 pt-2">
              <button
                type="button"
                onClick={() => {
                  setShowNewUserForm(false);
                  setNewUsername('');
                  setNewEmail('');
                  setError('');
                }}
                className="flex-1 py-2 px-4 bg-gray-700 hover:bg-gray-600 text-white font-medium rounded-md transition-colors"
                disabled={isLoading}
              >
                Cancel
              </button>
              <button
                type="submit"
                className="flex-1 py-2 px-4 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-medium rounded-md transition-colors"
                disabled={isLoading}
              >
                {isLoading ? 'Creating...' : 'Create User'}
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
}
