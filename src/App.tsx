import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useAppStore } from './store';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Practice from './pages/Practice';
import MockInterview from './pages/MockInterview';
import Progress from './pages/Progress';
import Layout from './components/Layout';
import { ErrorBoundary } from './components/ErrorBoundary';
import './App.css';

function App() {
  const currentUser = useAppStore((state) => state.currentUser);

  if (!currentUser) {
    return (
      <ErrorBoundary>
        <Router>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="*" element={<Navigate to="/login" replace />} />
          </Routes>
        </Router>
      </ErrorBoundary>
    );
  }

  return (
    <ErrorBoundary>
      <Router>
        <Layout>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/practice/:category?" element={<Practice />} />
            <Route path="/mock-interview/:type?" element={<MockInterview />} />
            <Route path="/progress" element={<Progress />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </Layout>
      </Router>
    </ErrorBoundary>
  );
}

export default App;
