import React, { useMemo } from 'react';

interface SerializedNode {
  id: string;
  type?: string;
  label?: string;
  position?: { x: number; y: number };
  [key: string]: any;
}

interface SerializedEdge {
  id?: string;
  source: string;
  target: string;
}

interface DiagramDataSerialized {
  nodes: SerializedNode[];
  edges: SerializedEdge[];
}

interface Props {
  expectedComponents: string[];
  diagram: DiagramDataSerialized;
}

function normalize(s: string) {
  return (s || '').toLowerCase();
}

function isMatch(expected: string, nodeLabel: string) {
  const a = normalize(expected);
  const b = normalize(nodeLabel);
  if (!a || !b) return false;
  // Match by token overlap (length > 3 to avoid stopwords)
  const tokens = a.split(/[^a-z0-9]+/).filter((t) => t.length > 3);
  return tokens.some((t) => b.includes(t)) || b.split(/[^a-z0-9]+/).some((t) => t.length > 3 && a.includes(t));
}

export const CoveragePanel: React.FC<Props> = ({ expectedComponents, diagram }) => {
  const { coverage, percent, missing } = useMemo(() => {
    const labels: string[] = (diagram?.nodes || []).map((n) => n.label || n.type || '');

    const coverage = expectedComponents.map((c) => ({
      component: c,
      covered: labels.some((lbl) => isMatch(c, lbl)),
    }));

    const coveredCount = coverage.filter((c) => c.covered).length;
    const total = Math.max(expectedComponents.length, 1);
    const percent = Math.round((coveredCount / total) * 100);
    const missing = coverage.filter((c) => !c.covered).map((c) => c.component);

    return { coverage, percent, missing };
  }, [expectedComponents, diagram]);

  return (
    <div className="border-t border-gray-700 bg-gray-900">
      <div className="px-4 py-3 flex items-center justify-between">
        <div className="text-white font-semibold" data-testid="ml-coverage-title">Design Coverage</div>
        <div className="text-sm text-gray-400" data-testid="ml-coverage-percent">{percent}% covered</div>
      </div>
      <div className="px-4 pb-3">
        {missing.length === 0 ? (
          <div className="text-sm text-green-400" data-testid="ml-coverage-complete">All key components covered</div>
        ) : (
          <div>
            <div className="text-sm text-gray-300 mb-2">Missing components:</div>
            <ul className="list-disc list-inside space-y-1">
              {missing.map((m) => (
                <li key={m} className="text-sm text-orange-300" data-testid="ml-coverage-missing-item">{m}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
};
