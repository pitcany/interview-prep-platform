# Getting Started - Your First Coding Session

This guide will walk you through your first coding session to complete the Practice page.

## Before You Start

1. **Verify Installation**
```bash
cd interview-prep-platform
npm run dev
```

The app should launch. You should be able to:
- ✅ Create a user
- ✅ See the dashboard
- ✅ Navigate to Practice page (shows placeholder)

## Your First Feature: Complete the Practice Page

Let's build the LeetCode practice feature step by step.

### Step 1: Create the QuestionList Component (30 mins)

Create `src/components/QuestionList/index.tsx`:

```typescript
import React, { useEffect, useState } from 'react';
import { api } from '../../services/api';
import type { Question } from '../../types';

interface QuestionListProps {
  category: 'leetcode' | 'ml_system_design';
  onSelectQuestion: (question: Question) => void;
}

export default function QuestionList({ category, onSelectQuestion }: QuestionListProps) {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [filter, setFilter] = useState<'all' | 'easy' | 'medium' | 'hard'>('all');

  useEffect(() => {
    loadQuestions();
  }, [category, filter]);

  const loadQuestions = async () => {
    try {
      setIsLoading(true);
      const difficultyFilter = filter === 'all' ? undefined : filter;
      const data = await api.getQuestions(category, difficultyFilter);
      setQuestions(data);
    } catch (error) {
      console.error('Failed to load questions:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'easy': return 'text-green-500';
      case 'medium': return 'text-yellow-500';
      case 'hard': return 'text-red-500';
      default: return 'text-gray-500';
    }
  };

  if (isLoading) {
    return <div className="text-gray-400">Loading questions...</div>;
  }

  return (
    <div>
      {/* Filter buttons */}
      <div className="flex gap-2 mb-4">
        {(['all', 'easy', 'medium', 'hard'] as const).map((level) => (
          <button
            key={level}
            onClick={() => setFilter(level)}
            className={`px-4 py-2 rounded-lg transition-colors ${
              filter === level
                ? 'bg-blue-600 text-white'
                : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
            }`}
          >
            {level.charAt(0).toUpperCase() + level.slice(1)}
          </button>
        ))}
      </div>

      {/* Question list */}
      <div className="space-y-2">
        {questions.map((question) => (
          <button
            key={question.id}
            onClick={() => onSelectQuestion(question)}
            className="w-full text-left p-4 bg-gray-800 hover:bg-gray-750 border border-gray-700 rounded-lg transition-colors"
          >
            <div className="flex items-center justify-between mb-2">
              <h3 className="font-semibold text-white">{question.title}</h3>
              <span className={`text-sm font-medium ${getDifficultyColor(question.difficulty)}`}>
                {question.difficulty}
              </span>
            </div>
            {question.tags && (
              <div className="flex gap-2 flex-wrap">
                {JSON.parse(question.tags).map((tag: string) => (
                  <span
                    key={tag}
                    className="text-xs px-2 py-1 bg-gray-700 text-gray-300 rounded"
                  >
                    {tag}
                  </span>
                ))}
              </div>
            )}
          </button>
        ))}
      </div>
    </div>
  );
}
```

### Step 2: Create the CodeEditor Component (45 mins)

Create `src/components/CodeEditor/index.tsx`:

```typescript
import React from 'react';
import Editor from '@monaco-editor/react';

interface CodeEditorProps {
  code: string;
  language: 'python' | 'java' | 'cpp';
  onChange: (value: string) => void;
  onLanguageChange: (lang: 'python' | 'java' | 'cpp') => void;
}

export default function CodeEditor({
  code,
  language,
  onChange,
  onLanguageChange,
}: CodeEditorProps) {
  const languageMap = {
    python: 'python',
    java: 'java',
    cpp: 'cpp',
  };

  return (
    <div className="h-full flex flex-col">
      {/* Language selector */}
      <div className="flex items-center gap-2 p-3 bg-gray-800 border-b border-gray-700">
        <span className="text-sm text-gray-400">Language:</span>
        {(['python', 'java', 'cpp'] as const).map((lang) => (
          <button
            key={lang}
            onClick={() => onLanguageChange(lang)}
            className={`px-3 py-1 rounded transition-colors ${
              language === lang
                ? 'bg-blue-600 text-white'
                : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
            }`}
          >
            {lang === 'cpp' ? 'C++' : lang.charAt(0).toUpperCase() + lang.slice(1)}
          </button>
        ))}
      </div>

      {/* Monaco Editor */}
      <div className="flex-1">
        <Editor
          height="100%"
          language={languageMap[language]}
          value={code}
          onChange={(value) => onChange(value || '')}
          theme="vs-dark"
          options={{
            minimap: { enabled: false },
            fontSize: 14,
            lineNumbers: 'on',
            scrollBeyondLastLine: false,
            automaticLayout: true,
            tabSize: 4,
          }}
        />
      </div>
    </div>
  );
}
```

### Step 3: Update the Practice Page (1 hour)

Replace `src/pages/Practice.tsx` with:

```typescript
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useAppStore } from '../store';
import { api } from '../services/api';
import QuestionList from '../components/QuestionList';
import CodeEditor from '../components/CodeEditor';
import type { Question, LeetCodeQuestion } from '../types';

export default function Practice() {
  const { category = 'leetcode' } = useParams<{ category?: 'leetcode' | 'ml_system_design' }>();
  const currentUser = useAppStore((state) => state.currentUser);
  
  const [selectedQuestion, setSelectedQuestion] = useState<Question | null>(null);
  const [questionDetails, setQuestionDetails] = useState<LeetCodeQuestion | null>(null);
  const [code, setCode] = useState('');
  const [language, setLanguage] = useState<'python' | 'java' | 'cpp'>('python');
  const [isRunning, setIsRunning] = useState(false);
  const [results, setResults] = useState<any>(null);

  useEffect(() => {
    if (selectedQuestion) {
      loadQuestionDetails();
    }
  }, [selectedQuestion, language]);

  const loadQuestionDetails = async () => {
    if (!selectedQuestion) return;

    try {
      const details = await api.getLeetCodeDetails(selectedQuestion.id);
      setQuestionDetails(details);
      
      // Set initial code based on language
      const signatureKey = `function_signature_${language}` as keyof LeetCodeQuestion;
      setCode(details[signatureKey] as string || '');
    } catch (error) {
      console.error('Failed to load question details:', error);
    }
  };

  const handleRunCode = async () => {
    if (!currentUser || !selectedQuestion || !questionDetails) return;

    setIsRunning(true);
    try {
      const testCases = JSON.parse(questionDetails.test_cases);
      const result = await api.executeCode({
        code,
        language,
        testCases,
        questionId: selectedQuestion.id,
      });
      setResults(result);
    } catch (error) {
      console.error('Failed to run code:', error);
    } finally {
      setIsRunning(false);
    }
  };

  const handleSubmit = async () => {
    if (!currentUser || !selectedQuestion || !questionDetails) return;

    setIsRunning(true);
    try {
      const testCases = JSON.parse(questionDetails.test_cases);
      const result = await api.submitCode({
        userId: currentUser.id,
        questionId: selectedQuestion.id,
        code,
        language,
        customTestCases: testCases,
      });
      
      setResults(result.executionResult);
      
      // Generate feedback
      if (result.executionResult.status === 'passed') {
        await api.generateFeedback({
          userId: currentUser.id,
          submissionId: result.submission.id,
          submissionType: 'code',
        });
      }
    } catch (error) {
      console.error('Failed to submit code:', error);
    } finally {
      setIsRunning(false);
    }
  };

  return (
    <div className="h-screen flex">
      {/* Left sidebar - Question list */}
      <div className="w-80 border-r border-gray-700 p-4 overflow-y-auto">
        <h2 className="text-xl font-bold text-white mb-4">
          {category === 'leetcode' ? 'LeetCode' : 'ML Design'} Questions
        </h2>
        <QuestionList
          category={category}
          onSelectQuestion={setSelectedQuestion}
        />
      </div>

      {/* Main content */}
      {selectedQuestion ? (
        <div className="flex-1 flex flex-col">
          {/* Question description */}
          <div className="h-1/3 overflow-y-auto p-6 border-b border-gray-700">
            <h1 className="text-2xl font-bold text-white mb-2">
              {selectedQuestion.title}
            </h1>
            <span className={`inline-block px-3 py-1 rounded text-sm font-medium mb-4 ${
              selectedQuestion.difficulty === 'easy' ? 'bg-green-500/20 text-green-500' :
              selectedQuestion.difficulty === 'medium' ? 'bg-yellow-500/20 text-yellow-500' :
              'bg-red-500/20 text-red-500'
            }`}>
              {selectedQuestion.difficulty}
            </span>
            <div className="prose prose-invert max-w-none">
              {selectedQuestion.description}
            </div>
          </div>

          {/* Code editor */}
          <div className="h-2/3 flex flex-col">
            <div className="flex-1">
              <CodeEditor
                code={code}
                language={language}
                onChange={setCode}
                onLanguageChange={setLanguage}
              />
            </div>

            {/* Action buttons */}
            <div className="p-4 bg-gray-800 border-t border-gray-700 flex items-center gap-3">
              <button
                onClick={handleRunCode}
                disabled={isRunning}
                className="px-4 py-2 bg-green-600 hover:bg-green-700 disabled:bg-gray-600 text-white rounded-lg transition-colors"
              >
                {isRunning ? 'Running...' : 'Run Code'}
              </button>
              <button
                onClick={handleSubmit}
                disabled={isRunning}
                className="px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 text-white rounded-lg transition-colors"
              >
                {isRunning ? 'Submitting...' : 'Submit'}
              </button>

              {results && (
                <div className="ml-auto text-sm">
                  <span className={`font-medium ${
                    results.status === 'passed' ? 'text-green-500' :
                    results.status === 'failed' ? 'text-red-500' :
                    'text-yellow-500'
                  }`}>
                    {results.status.toUpperCase()}
                  </span>
                  <span className="text-gray-400 ml-2">
                    {results.testResults?.filter((t: any) => t.passed).length || 0}/
                    {results.testResults?.length || 0} tests passed
                  </span>
                </div>
              )}
            </div>
          </div>
        </div>
      ) : (
        <div className="flex-1 flex items-center justify-center">
          <div className="text-center">
            <p className="text-xl text-gray-400 mb-2">
              Select a question to get started
            </p>
            <p className="text-sm text-gray-500">
              Choose from the list on the left
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
```

### Step 4: Test Your Work

1. **Start the app**:
```bash
npm run dev
```

2. **Test the flow**:
   - Login/create user
   - Go to Dashboard
   - Click "LeetCode Practice"
   - Select a question
   - Switch languages
   - Write some code
   - Click "Run Code"
   - Check results

3. **Verify**:
   - [ ] Question list loads
   - [ ] Can filter by difficulty
   - [ ] Question details show
   - [ ] Editor works
   - [ ] Language switching works
   - [ ] Code execution works (requires Docker)

## Next Steps

After completing the Practice page:

1. **Add Test Results Display**
   - Show individual test case results
   - Display input/output/expected
   - Show execution time per test

2. **Add Custom Test Cases**
   - Allow users to add their own test cases
   - Validate input format
   - Run custom tests

3. **Mock Interview Page**
   - Create timer component
   - Implement interview session flow
   - Add feedback display

4. **Progress Page**
   - Add charts with Recharts
   - Show submission history
   - Display feedback

## Tips for Success

### Development Workflow
1. Make small, incremental changes
2. Test after each change
3. Use React DevTools for debugging
4. Check console for errors

### Common Issues
- **Monaco Editor not loading**: Check import path
- **API calls failing**: Check Electron main process logs
- **Docker errors**: Ensure Docker is running

### Best Practices
- Use TypeScript types
- Handle loading states
- Add error boundaries
- Write clean, commented code

## Resources

- **React Docs**: https://react.dev/
- **TypeScript**: https://www.typescriptlang.org/
- **Monaco Editor**: https://microsoft.github.io/monaco-editor/
- **Electron**: https://www.electronjs.org/
- **TailwindCSS**: https://tailwindcss.com/

## Need Help?

1. Check the existing code for patterns
2. Look at type definitions in `src/types/`
3. Review the API service in `src/services/api.ts`
4. Refer to the database schema

## Your Development Checklist

Day 1:
- [ ] Set up development environment
- [ ] Create QuestionList component
- [ ] Test question loading

Day 2:
- [ ] Create CodeEditor component
- [ ] Integrate Monaco Editor
- [ ] Test language switching

Day 3:
- [ ] Update Practice page
- [ ] Connect all components
- [ ] Test run/submit flow

Day 4:
- [ ] Add test results display
- [ ] Polish UI
- [ ] Fix bugs

You've got this! 🚀

Start with the QuestionList component and work your way through. The foundation is solid, you just need to build the UI on top of it.
