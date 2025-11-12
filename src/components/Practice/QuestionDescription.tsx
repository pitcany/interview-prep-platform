import { Lightbulb } from 'lucide-react';
import type { Question, LeetCodeQuestion, MLDesignQuestion } from '../../types';

interface QuestionDescriptionProps {
  question: Question;
  category: 'leetcode' | 'ml_system_design';
  questionDetails: LeetCodeQuestion | null;
  mlDesignDetails: MLDesignQuestion | null;
  hints: string[];
  revealedHints: number;
}

export default function QuestionDescription({
  question,
  category,
  questionDetails,
  mlDesignDetails,
  hints,
  revealedHints,
}: QuestionDescriptionProps) {
  return (
    <div className="w-1/3 border-r border-gray-700 overflow-y-auto p-6">
      <div className="prose prose-invert max-w-none">
        <div className="whitespace-pre-wrap text-gray-300">
          {question.description}
        </div>

        {category === 'leetcode' && question.examples && (
          <div className="mt-6">
            <h3 className="text-white font-semibold mb-3">Examples</h3>
            {JSON.parse(question.examples).map((example: any, i: number) => (
              <div key={i} className="mb-4 p-4 bg-gray-800 rounded-lg">
                <div className="text-sm">
                  <div className="mb-2">
                    <span className="text-gray-400">Input:</span>
                    <div className="font-mono text-white mt-1">
                      {JSON.stringify(example.input)}
                    </div>
                  </div>
                  <div className="mb-2">
                    <span className="text-gray-400">Output:</span>
                    <div className="font-mono text-white mt-1">
                      {JSON.stringify(example.output)}
                    </div>
                  </div>
                  {example.explanation && (
                    <div>
                      <span className="text-gray-400">Explanation:</span>
                      <div className="text-gray-300 mt-1">{example.explanation}</div>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}

        {category === 'leetcode' && questionDetails?.expected_time_complexity && (
          <div className="mt-6">
            <h3 className="text-white font-semibold mb-2">Constraints</h3>
            <div className="text-sm text-gray-400">
              <p>Time Complexity: {questionDetails.expected_time_complexity}</p>
              <p>Space Complexity: {questionDetails.expected_space_complexity}</p>
            </div>
          </div>
        )}

        {/* Hints Section */}
        {revealedHints > 0 && (
          <div className="mt-6">
            <h3 className="text-white font-semibold mb-3 flex items-center gap-2">
              <Lightbulb className="text-yellow-500" size={20} />
              Hints
            </h3>
            <div className="space-y-3">
              {hints.slice(0, revealedHints).map((hint, index) => (
                <div key={index} className="p-4 bg-yellow-500/10 border border-yellow-500/20 rounded-lg">
                  <div className="flex items-start gap-3">
                    <span className="text-yellow-500 font-semibold text-sm mt-0.5">
                      Hint {index + 1}:
                    </span>
                    <p className="text-sm text-gray-300 flex-1">{hint}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {category === 'ml_system_design' && mlDesignDetails && (
          <>
            {mlDesignDetails.scenario && (
              <div className="mt-6">
                <h3 className="text-white font-semibold mb-3">Scenario</h3>
                <div className="text-sm text-gray-300 whitespace-pre-wrap">
                  {mlDesignDetails.scenario}
                </div>
              </div>
            )}

            {mlDesignDetails.requirements && (
              <div className="mt-6">
                <h3 className="text-white font-semibold mb-3">Requirements</h3>
                <ul className="text-sm text-gray-300 space-y-2 list-disc list-inside">
                  {mlDesignDetails.requirements.map((req: string, i: number) => (
                    <li key={i}>{req}</li>
                  ))}
                </ul>
              </div>
            )}

            {mlDesignDetails.key_components && mlDesignDetails.key_components.length > 0 && (
              <div className="mt-6">
                <h3 className="text-white font-semibold mb-3">Key Components</h3>
                <div className="flex flex-wrap gap-2">
                  {mlDesignDetails.key_components.map((component: string, i: number) => (
                    <span key={i} className="text-xs px-2 py-1 bg-blue-600/20 text-blue-400 rounded">
                      {component}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {mlDesignDetails.evaluation_criteria && (
              <div className="mt-6">
                <h3 className="text-white font-semibold mb-3">Evaluation Criteria</h3>
                <div className="text-sm text-gray-300 space-y-2">
                  {Object.entries(mlDesignDetails.evaluation_criteria).map(([key, value]) => (
                    <div key={key}>
                      <span className="font-medium text-blue-400">{key}:</span> {value}
                    </div>
                  ))}
                </div>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}
