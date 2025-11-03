import React from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAppStore } from '../store';
import { Code, Brain, TrendingUp, Clock, LogOut, User } from 'lucide-react';

interface LayoutProps {
  children: React.ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  const navigate = useNavigate();
  const location = useLocation();
  const { currentUser, setCurrentUser } = useAppStore();

  const handleLogout = () => {
    setCurrentUser(null);
    navigate('/login');
  };

  const navItems = [
    { path: '/', icon: TrendingUp, label: 'Dashboard' },
    { path: '/practice', icon: Code, label: 'Practice' },
    { path: '/mock-interview', icon: Clock, label: 'Mock Interview' },
    { path: '/progress', icon: Brain, label: 'Progress' },
  ];

  return (
    <div className="min-h-screen bg-gray-900 flex">
      {/* Sidebar */}
      <aside className="w-64 bg-gray-800 border-r border-gray-700 flex flex-col">
        <div className="p-6 border-b border-gray-700">
          <h1 className="text-xl font-bold text-white">Interview Prep</h1>
        </div>

        <nav className="flex-1 p-4 space-y-2">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path ||
              (item.path !== '/' && location.pathname.startsWith(item.path));

            return (
              <Link
                key={item.path}
                to={item.path}
                className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                  isActive
                    ? 'bg-blue-600 text-white'
                    : 'text-gray-300 hover:bg-gray-700'
                }`}
              >
                <Icon size={20} />
                <span className="font-medium">{item.label}</span>
              </Link>
            );
          })}
        </nav>

        <div className="p-4 border-t border-gray-700">
          <div className="flex items-center gap-3 px-4 py-3 bg-gray-700 rounded-lg mb-2">
            <User size={20} className="text-gray-300" />
            <div className="flex-1 min-w-0">
              <p className="text-sm font-medium text-white truncate">
                {currentUser?.username}
              </p>
              <p className="text-xs text-gray-400 truncate">
                {currentUser?.email}
              </p>
            </div>
          </div>
          <button
            onClick={handleLogout}
            className="w-full flex items-center gap-3 px-4 py-3 text-gray-300 hover:bg-gray-700 rounded-lg transition-colors"
          >
            <LogOut size={20} />
            <span className="font-medium">Logout</span>
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-auto">
        {children}
      </main>
    </div>
  );
}
