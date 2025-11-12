import { Send, Loader2, Sparkles, FileText } from 'lucide-react';
import DiagramEditor from '../DiagramEditor';
import SolutionViewer from '../SolutionViewer';
import type { MLDesignQuestion, DiagramData } from '../../types';

interface MLDesignPracticeViewProps {
  mlDesignDetails: MLDesignQuestion;
  diagramData: DiagramData;
  explanation: string;
  isSubmitting: boolean;
  onSaveDiagram: (nodes: any[], edges: any[]) => void;
  onExplanationChange: (explanation: string) => void;
  onSubmitDesign: () => void;
  onViewFeedback: () => void;
}

export default function MLDesignPracticeView({
  mlDesignDetails,
  diagramData,
  explanation,
  isSubmitting,
  onSaveDiagram,
  onExplanationChange,
  onSubmitDesign,
  onViewFeedback,
}: MLDesignPracticeViewProps) {
  return (
    <div className="flex-1 flex flex-col min-w-0">
      {/* Diagram editor */}
      <div className="flex-1 min-h-0">
        <DiagramEditor
          initialNodes={diagramData.nodes}
          initialEdges={diagramData.edges}
          onSave={onSaveDiagram}
        />
      </div>

      {/* Written explanation */}
      <div className="h-80 border-t border-gray-700 bg-gray-900 flex flex-col">
        <div className="px-4 py-2 bg-gray-800 border-b border-gray-700 flex items-center gap-2">
          <FileText size={18} className="text-gray-400" />
          <span className="text-sm font-medium text-white">Written Explanation</span>
          <span className="text-xs text-gray-500 ml-auto">
            {explanation.length} characters
          </span>
        </div>
        <textarea
          value={explanation}
          onChange={(e) => onExplanationChange(e.target.value)}
          placeholder="Explain your system design here. Describe the components, data flow, scaling strategies, trade-offs, and how it meets the requirements..."
          className="flex-1 bg-gray-900 text-gray-300 px-4 py-3 resize-none focus:outline-none font-mono text-sm"
        />
      </div>

      {/* Solution viewer */}
      <SolutionViewer
        category="ml_system_design"
        sampleSolution={mlDesignDetails.sample_solution}
      />

      {/* Action bar */}
      <div className="px-6 py-3 bg-gray-800 border-t border-gray-700 flex items-center justify-between">
        <div className="flex items-center gap-3 text-sm text-gray-400">
          <span>Save your diagram and provide a written explanation</span>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={onSubmitDesign}
            disabled={isSubmitting}
            className="px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white rounded-lg transition-colors flex items-center gap-2"
          >
            {isSubmitting ? (
              <><Loader2 size={18} className="animate-spin" /> Submitting...</>
            ) : (
              <><Send size={18} /> Submit Design</>
            )}
          </button>

          <button
            onClick={onViewFeedback}
            className="px-3 py-1 bg-purple-600 hover:bg-purple-700 text-white text-sm rounded-lg transition-colors flex items-center gap-1"
          >
            <Sparkles size={16} />
            View Feedback
          </button>
        </div>
      </div>
    </div>
  );
}
