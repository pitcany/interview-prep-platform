import { useState } from 'react';
import { ChevronDown, ChevronUp, Code, FileText, Copy, Check } from 'lucide-react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism';

interface SolutionViewerProps {
  category: 'leetcode' | 'ml_system_design';
  solutionPython?: string;
  solutionJava?: string;
  solutionCpp?: string;
  solutionExplanation?: string;
  sampleSolution?: string;
}

export default function SolutionViewer({
  category,
  solutionPython,
  solutionJava,
  solutionCpp,
  solutionExplanation,
  sampleSolution
}: SolutionViewerProps) {
  const [isExpanded, setIsExpanded] = useState(false);
  const [selectedLanguage, setSelectedLanguage] = useState<'python' | 'java' | 'cpp'>('python');
  const [showExplanation, setShowExplanation] = useState(true);
  const [copiedCode, setCopiedCode] = useState<string | null>(null);

  const handleCopyCode = (code: string, language: string) => {
    navigator.clipboard.writeText(code);
    setCopiedCode(language);
    setTimeout(() => setCopiedCode(null), 2000);
  };

  const getCurrentSolution = () => {
    switch (selectedLanguage) {
      case 'python':
        return solutionPython || '';
      case 'java':
        return solutionJava || '';
      case 'cpp':
        return solutionCpp || '';
      default:
        return '';
    }
  };

  const getLanguageSyntax = (language: string) => {
    switch (language) {
      case 'java':
        return 'java';
      case 'cpp':
        return 'cpp';
      case 'python':
      default:
        return 'python';
    }
  };

  const formatExplanation = (text: string) => {
    // Convert markdown-style headers and lists to HTML
    const lines = text.split('\n');
    const formatted = lines.map(line => {
      // Headers
      if (line.startsWith('### ')) {
        return `<h4 class="text-white font-semibold mt-4 mb-2">${line.substring(4)}</h4>`;
      }
      if (line.startsWith('## ')) {
        return `<h3 class="text-white font-bold text-lg mt-6 mb-3">${line.substring(3)}</h3>`;
      }
      if (line.startsWith('# ')) {
        return `<h2 class="text-white font-bold text-xl mt-6 mb-4">${line.substring(2)}</h2>`;
      }
      // Bold text
      line = line.replace(/\*\*(.*?)\*\*/g, '<strong class="text-white">$1</strong>');
      // Lists
      if (line.startsWith('- ')) {
        return `<li class="ml-4 text-gray-300">${line.substring(2)}</li>`;
      }
      // Code blocks
      if (line.includes('`')) {
        line = line.replace(/`([^`]+)`/g, '<code class="px-1 py-0.5 bg-gray-800 text-green-400 rounded text-sm">$1</code>');
      }
      // Regular paragraphs
      if (line.trim()) {
        return `<p class="text-gray-300 mb-2">${line}</p>`;
      }
      return '<br/>';
    });

    return formatted.join('');
  };

  if (category === 'ml_system_design' && !sampleSolution) {
    return null;
  }

  if (category === 'leetcode' && !solutionPython && !solutionJava && !solutionCpp) {
    return null;
  }

  return (
    <div className="border-t border-gray-700">
      {/* Solution Header */}
      <button
        onClick={() => setIsExpanded(!isExpanded)}
        className="w-full flex items-center justify-between px-6 py-3 bg-gray-800 hover:bg-gray-750 transition-colors"
      >
        <div className="flex items-center gap-2">
          <Code className="w-5 h-5 text-blue-500" />
          <span className="font-medium text-white">View Solution</span>
        </div>
        {isExpanded ? (
          <ChevronUp className="w-5 h-5 text-gray-400" />
        ) : (
          <ChevronDown className="w-5 h-5 text-gray-400" />
        )}
      </button>

      {/* Solution Content */}
      {isExpanded && (
        <div className="bg-gray-850 max-h-[600px] overflow-y-auto">
          {category === 'leetcode' ? (
            <>
              {/* Language Tabs and Explanation Toggle */}
              <div className="flex items-center justify-between px-6 py-3 border-b border-gray-700">
                <div className="flex gap-2">
                  <button
                    onClick={() => setSelectedLanguage('python')}
                    className={`px-3 py-1.5 text-sm font-medium rounded transition-colors ${
                      selectedLanguage === 'python'
                        ? 'bg-blue-500 text-white'
                        : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                    }`}
                  >
                    Python
                  </button>
                  <button
                    onClick={() => setSelectedLanguage('java')}
                    className={`px-3 py-1.5 text-sm font-medium rounded transition-colors ${
                      selectedLanguage === 'java'
                        ? 'bg-blue-500 text-white'
                        : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                    }`}
                  >
                    Java
                  </button>
                  <button
                    onClick={() => setSelectedLanguage('cpp')}
                    className={`px-3 py-1.5 text-sm font-medium rounded transition-colors ${
                      selectedLanguage === 'cpp'
                        ? 'bg-blue-500 text-white'
                        : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                    }`}
                  >
                    C++
                  </button>
                </div>
                <button
                  onClick={() => setShowExplanation(!showExplanation)}
                  className="flex items-center gap-2 px-3 py-1.5 text-sm bg-gray-700 text-gray-300 rounded hover:bg-gray-600 transition-colors"
                >
                  <FileText className="w-4 h-4" />
                  {showExplanation ? 'Hide' : 'Show'} Explanation
                </button>
              </div>

              {/* Code Display */}
              <div className="relative">
                <div className="absolute top-4 right-4 z-10">
                  <button
                    onClick={() => handleCopyCode(getCurrentSolution(), selectedLanguage)}
                    className="flex items-center gap-1 px-2 py-1 text-xs bg-gray-700 text-gray-300 rounded hover:bg-gray-600 transition-colors"
                  >
                    {copiedCode === selectedLanguage ? (
                      <>
                        <Check className="w-3 h-3" />
                        Copied!
                      </>
                    ) : (
                      <>
                        <Copy className="w-3 h-3" />
                        Copy
                      </>
                    )}
                  </button>
                </div>
                <div>
                  <SyntaxHighlighter
                    language={getLanguageSyntax(selectedLanguage)}
                    style={oneDark}
                    customStyle={{
                      margin: 0,
                      padding: '1.5rem',
                      background: 'transparent',
                      fontSize: '0.875rem',
                    }}
                  >
                    {getCurrentSolution()}
                  </SyntaxHighlighter>
                </div>
              </div>

              {/* Explanation */}
              {showExplanation && solutionExplanation && (
                <div className="px-6 py-4 border-t border-gray-700">
                  <div
                    className="prose prose-invert max-w-none"
                    dangerouslySetInnerHTML={{ __html: formatExplanation(solutionExplanation) }}
                  />
                </div>
              )}
            </>
          ) : (
            /* ML System Design Solution */
            <div className="px-6 py-4">
              <div className="prose prose-invert max-w-none">
                {sampleSolution && (
                  <div>
                    {/* Check if it's markdown with code blocks */}
                    {sampleSolution.includes('```') ? (
                      <div>
                        {sampleSolution.split('```').map((section, index) => {
                          if (index % 2 === 0) {
                            // Regular text section
                            return (
                              <div
                                key={index}
                                dangerouslySetInnerHTML={{ __html: formatExplanation(section) }}
                              />
                            );
                          } else {
                            // Code block
                            const lines = section.split('\n');
                            const language = lines[0] || 'python';
                            const code = lines.slice(1).join('\n');
                            return (
                              <div key={index} className="my-4">
                                <SyntaxHighlighter
                                  language={language}
                                  style={oneDark}
                                  customStyle={{
                                    margin: 0,
                                    padding: '1rem',
                                    borderRadius: '0.5rem',
                                    fontSize: '0.875rem',
                                  }}
                                >
                                  {code}
                                </SyntaxHighlighter>
                              </div>
                            );
                          }
                        })}
                      </div>
                    ) : (
                      <div
                        dangerouslySetInnerHTML={{ __html: formatExplanation(sampleSolution) }}
                      />
                    )}
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}