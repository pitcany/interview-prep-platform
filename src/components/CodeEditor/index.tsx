import React, { useRef, useEffect } from 'react';
import Editor from '@monaco-editor/react';
import { Code2, Download, RotateCcw } from 'lucide-react';

interface CodeEditorProps {
  code: string;
  language: 'python' | 'java' | 'cpp';
  onChange: (value: string) => void;
  onLanguageChange: (lang: 'python' | 'java' | 'cpp') => void;
  onReset?: () => void;
  isReadOnly?: boolean;
}

export default function CodeEditor({
  code,
  language,
  onChange,
  onLanguageChange,
  onReset,
  isReadOnly = false,
}: CodeEditorProps) {
  const editorRef = useRef<any>(null);

  const languageMap = {
    python: 'python',
    java: 'java',
    cpp: 'cpp',
  };

  const languageLabels = {
    python: 'Python',
    java: 'Java',
    cpp: 'C++',
  };

  const handleEditorDidMount = (editor: any) => {
    editorRef.current = editor;
    
    // Add keyboard shortcuts
    editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyS, () => {
      // Save action (could trigger auto-save)
      console.log('Save shortcut triggered');
    });

    editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, () => {
      // Run code shortcut
      console.log('Run shortcut triggered');
    });
  };

  const handleFormatCode = () => {
    if (editorRef.current) {
      editorRef.current.getAction('editor.action.formatDocument')?.run();
    }
  };

  const handleDownloadCode = () => {
    const extensions = { python: 'py', java: 'java', cpp: 'cpp' };
    const blob = new Blob([code], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `solution.${extensions[language]}`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <div className="h-full flex flex-col bg-gray-900">
      {/* Toolbar */}
      <div className="flex items-center justify-between px-4 py-2 bg-gray-800 border-b border-gray-700">
        <div className="flex items-center gap-2">
          <Code2 size={18} className="text-gray-400" />
          <span className="text-sm text-gray-400">Language:</span>
          {(['python', 'java', 'cpp'] as const).map((lang) => (
            <button
              key={lang}
              onClick={() => onLanguageChange(lang)}
              disabled={isReadOnly}
              className={`px-3 py-1 rounded text-sm transition-colors ${
                language === lang
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-700 text-gray-300 hover:bg-gray-600 disabled:opacity-50'
              }`}
            >
              {languageLabels[lang]}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-2">
          {onReset && (
            <button
              onClick={onReset}
              className="p-1.5 text-gray-400 hover:text-white hover:bg-gray-700 rounded transition-colors"
              title="Reset to template"
            >
              <RotateCcw size={18} />
            </button>
          )}
          <button
            onClick={handleDownloadCode}
            className="p-1.5 text-gray-400 hover:text-white hover:bg-gray-700 rounded transition-colors"
            title="Download code"
          >
            <Download size={18} />
          </button>
        </div>
      </div>

      {/* Monaco Editor */}
      <div className="flex-1 overflow-hidden">
        <Editor
          height="100%"
          language={languageMap[language]}
          value={code}
          onChange={(value) => onChange(value || '')}
          onMount={handleEditorDidMount}
          theme="vs-dark"
          options={{
            minimap: { enabled: true },
            fontSize: 14,
            lineNumbers: 'on',
            scrollBeyondLastLine: false,
            automaticLayout: true,
            tabSize: language === 'python' ? 4 : 2,
            insertSpaces: true,
            wordWrap: 'on',
            formatOnPaste: true,
            formatOnType: true,
            readOnly: isReadOnly,
            scrollbar: {
              vertical: 'visible',
              horizontal: 'visible',
              useShadows: false,
              verticalScrollbarSize: 10,
              horizontalScrollbarSize: 10,
            },
            padding: {
              top: 16,
              bottom: 16,
            },
          }}
        />
      </div>

      {/* Footer with hints */}
      <div className="px-4 py-2 bg-gray-800 border-t border-gray-700">
        <div className="flex items-center justify-between text-xs text-gray-500">
          <div className="flex gap-4">
            <span>⌘/Ctrl + S to save</span>
            <span>⌘/Ctrl + Enter to run</span>
            <span>⌘/Ctrl + / to comment</span>
          </div>
          <div>
            {code.split('\n').length} lines • {code.length} characters
          </div>
        </div>
      </div>
    </div>
  );
}

// Add Monaco global type declaration
declare global {
  const monaco: any;
}
