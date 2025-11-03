import React, { useState } from 'react';
import { CheckCircle2, XCircle, Clock, AlertCircle, Plus, X } from 'lucide-react';
import type { TestResult, TestCase } from '../../types';

interface TestRunnerProps {
  testCases: TestCase[];
  results?: TestResult[];
  onAddTestCase?: (testCase: TestCase) => void;
  onRemoveTestCase?: (index: number) => void;
}

export default function TestRunner({
  testCases,
  results,
  onAddTestCase,
  onRemoveTestCase,
}: TestRunnerProps) {
  const [showAddTest, setShowAddTest] = useState(false);
  const [newTestInput, setNewTestInput] = useState('');
  const [newTestOutput, setNewTestOutput] = useState('');
  const [expandedTests, setExpandedTests] = useState<Set<number>>(new Set());

  const toggleTestExpansion = (index: number) => {
    const newExpanded = new Set(expandedTests);
    if (newExpanded.has(index)) {
      newExpanded.delete(index);
    } else {
      newExpanded.add(index);
    }
    setExpandedTests(newExpanded);
  };

  const handleAddTest = () => {
    if (!newTestInput || !newTestOutput || !onAddTestCase) return;

    try {
      const input = JSON.parse(newTestInput);
      const output = JSON.parse(newTestOutput);
      onAddTestCase({ input, expectedOutput: output });
      setNewTestInput('');
      setNewTestOutput('');
      setShowAddTest(false);
    } catch (error) {
      alert('Invalid JSON format');
    }
  };

  const getStatusIcon = (result?: TestResult) => {
    if (!result) return <Clock size={18} className="text-gray-500" />;
    if (result.passed) return <CheckCircle2 size={18} className="text-green-500" />;
    if (result.error) return <AlertCircle size={18} className="text-orange-500" />;
    return <XCircle size={18} className="text-red-500" />;
  };

  const getStatusColor = (result?: TestResult) => {
    if (!result) return 'border-gray-700';
    if (result.passed) return 'border-green-500/50 bg-green-500/5';
    if (result.error) return 'border-orange-500/50 bg-orange-500/5';
    return 'border-red-500/50 bg-red-500/5';
  };

  return (
    <div className="h-full flex flex-col bg-gray-900">
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 bg-gray-800 border-b border-gray-700">
        <div>
          <h3 className="font-semibold text-white">Test Cases</h3>
          {results && (
            <p className="text-sm text-gray-400 mt-1">
              {results.filter((r) => r.passed).length} / {results.length} passed
            </p>
          )}
        </div>
        {onAddTestCase && (
          <button
            onClick={() => setShowAddTest(!showAddTest)}
            className="px-3 py-1 bg-blue-600 hover:bg-blue-700 text-white text-sm rounded transition-colors flex items-center gap-1"
          >
            <Plus size={16} />
            Add Test
          </button>
        )}
      </div>

      {/* Add test form */}
      {showAddTest && (
        <div className="p-4 bg-gray-800 border-b border-gray-700">
          <div className="space-y-3">
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-1">
                Input (JSON)
              </label>
              <textarea
                value={newTestInput}
                onChange={(e) => setNewTestInput(e.target.value)}
                placeholder='[1, 2, 3]'
                className="w-full px-3 py-2 bg-gray-900 border border-gray-700 rounded text-white text-sm font-mono"
                rows={2}
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-1">
                Expected Output (JSON)
              </label>
              <textarea
                value={newTestOutput}
                onChange={(e) => setNewTestOutput(e.target.value)}
                placeholder='6'
                className="w-full px-3 py-2 bg-gray-900 border border-gray-700 rounded text-white text-sm font-mono"
                rows={2}
              />
            </div>
            <div className="flex gap-2">
              <button
                onClick={handleAddTest}
                className="px-3 py-1 bg-green-600 hover:bg-green-700 text-white text-sm rounded transition-colors"
              >
                Add
              </button>
              <button
                onClick={() => setShowAddTest(false)}
                className="px-3 py-1 bg-gray-700 hover:bg-gray-600 text-white text-sm rounded transition-colors"
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Test cases list */}
      <div className="flex-1 overflow-y-auto p-4 space-y-3">
        {testCases.map((testCase, index) => {
          const result = results?.[index];
          const isExpanded = expandedTests.has(index);

          return (
            <div
              key={index}
              className={`border rounded-lg transition-colors ${getStatusColor(result)}`}
            >
              <button
                onClick={() => toggleTestExpansion(index)}
                className="w-full px-4 py-3 flex items-start gap-3 hover:bg-white/5 transition-colors"
              >
                {getStatusIcon(result)}
                <div className="flex-1 text-left">
                  <div className="flex items-center justify-between mb-1">
                    <span className="text-sm font-medium text-white">
                      Test Case {index + 1}
                    </span>
                    {result && (
                      <span className="text-xs text-gray-400">
                        {result.executionTime}ms
                      </span>
                    )}
                  </div>
                  <div className="text-xs font-mono text-gray-400">
                    Input: {JSON.stringify(testCase.input)}
                  </div>
                </div>
                {onRemoveTestCase && index >= 3 && (
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      onRemoveTestCase(index);
                    }}
                    className="text-gray-500 hover:text-red-500 transition-colors"
                  >
                    <X size={16} />
                  </button>
                )}
              </button>

              {/* Expanded details */}
              {isExpanded && (
                <div className="px-4 pb-3 space-y-2 border-t border-gray-700">
                  <div>
                    <div className="text-xs font-semibold text-gray-400 mb-1">
                      Input:
                    </div>
                    <div className="text-sm font-mono text-white bg-gray-800 p-2 rounded">
                      {JSON.stringify(testCase.input, null, 2)}
                    </div>
                  </div>

                  <div>
                    <div className="text-xs font-semibold text-gray-400 mb-1">
                      Expected Output:
                    </div>
                    <div className="text-sm font-mono text-white bg-gray-800 p-2 rounded">
                      {JSON.stringify(testCase.expectedOutput, null, 2)}
                    </div>
                  </div>

                  {result && (
                    <>
                      <div>
                        <div className="text-xs font-semibold text-gray-400 mb-1">
                          Actual Output:
                        </div>
                        <div
                          className={`text-sm font-mono p-2 rounded ${
                            result.passed
                              ? 'text-green-400 bg-green-500/10'
                              : 'text-red-400 bg-red-500/10'
                          }`}
                        >
                          {JSON.stringify(result.actualOutput, null, 2)}
                        </div>
                      </div>

                      {result.error && (
                        <div>
                          <div className="text-xs font-semibold text-red-400 mb-1">
                            Error:
                          </div>
                          <div className="text-sm font-mono text-red-400 bg-red-500/10 p-2 rounded">
                            {result.error}
                          </div>
                        </div>
                      )}
                    </>
                  )}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
