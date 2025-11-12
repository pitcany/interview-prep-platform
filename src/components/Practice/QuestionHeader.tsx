import { ChevronLeft, Lightbulb } from 'lucide-react';
import type { Question } from '../../types';

interface QuestionHeaderProps {
  question: Question;
  category: 'leetcode' | 'ml_system_design';
  showDescription: boolean;
  hints: string[];
  revealedHints: number;
  hintsLoaded: boolean;
  onBack: () => void;
  onToggleDescription: () => void;
  onGetHint: () => void;
}

export default function QuestionHeader({
  question,
  category,
  showDescription,
  hints,
  revealedHints,
  hintsLoaded,
  onBack,
  onToggleDescription,
  onGetHint,
}: QuestionHeaderProps) {
  return (
    <div className="flex items-center justify-between px-6 py-3 bg-gray-800 border-b border-gray-700">
      <div className="flex items-center gap-3">
        <button
          onClick={onBack}
          className="text-gray-400 hover:text-white transition-colors"
        >
          <ChevronLeft size={20} />
        </button>
        <div>
          <h1 className="text-lg font-bold text-white">
            {question.title}
          </h1>
          <div className="flex items-center gap-2 mt-1">
            <span className={`text-xs px-2 py-0.5 rounded font-medium ${
              question.difficulty === 'easy' ? 'bg-green-500/20 text-green-500' :
              question.difficulty === 'medium' ? 'bg-yellow-500/20 text-yellow-500' :
              'bg-red-500/20 text-red-500'
            }`}>
              {question.difficulty}
            </span>
            {question.tags && JSON.parse(question.tags).slice(0, 3).map((tag: string) => (
              <span key={tag} className="text-xs px-2 py-0.5 bg-gray-700 text-gray-400 rounded">
                {tag}
              </span>
            ))}
          </div>
        </div>
      </div>

      <div className="flex items-center gap-3">
        {(category === 'leetcode' || category === 'ml_system_design') && (
          <button
            onClick={onGetHint}
            disabled={hintsLoaded && (hints.length === 0 || revealedHints >= hints.length)}
            className="px-3 py-1.5 text-sm bg-yellow-600 hover:bg-yellow-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white rounded-lg transition-colors flex items-center gap-2"
            title={
              hintsLoaded && hints.length === 0 ? 'No hints available' :
              hintsLoaded && revealedHints >= hints.length ? 'All hints revealed' :
              'Get a hint'
            }
          >
            <Lightbulb size={16} />
            {hintsLoaded && hints.length === 0 ? 'No Hints Available' :
             hintsLoaded && revealedHints >= hints.length ? 'All Hints Revealed' :
             hintsLoaded ? `Get Hint (${revealedHints}/${hints.length})` :
             `Get Hint (0/?)`}
          </button>
        )}
        <button
          onClick={onToggleDescription}
          className="px-3 py-1 text-sm text-gray-400 hover:text-white transition-colors"
        >
          {showDescription ? 'Hide' : 'Show'} Description
        </button>
      </div>
    </div>
  );
}
