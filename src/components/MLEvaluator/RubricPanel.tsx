import React, { useMemo } from 'react';

interface SerializedNode {
  id: string;
  type?: string;
  label?: string;
  data?: any;
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
  requirements: string[];
  diagram: DiagramDataSerialized;
  explanation: string;
}

const KEY_SETS: Record<string, string[]> = {
  problemUnderstanding: ['goal', 'metric', 'kpi', 'requirement', 'constraint', 'tradeoff', 'assumption'],
  dataDesign: ['data', 'feature', 'ingest', 'batch', 'stream', 'kafka', 'kinesis', 'etl', 'airflow'],
  modelSelection: ['model', 'baseline', 'training', 'inference', 'offline', 'online', 'feature store'],
  scalability: ['cache', 'latency', 'throughput', 'scale', 'shard', 'partition', 'queue', 'autoscal'],
  monitoring: ['monitor', 'alert', 'eval', 'ab test', 'drift', 'logging', 'metrics'],
  communication: ['summary', 'tradeoff', 'clarify', 'iterate', 'roadmap'],
};

function containsAny(text: string, keywords: string[]) {
  const t = (text || '').toLowerCase();
  return keywords.some((k) => t.includes(k));
}

function tokenCoverage(labels: string[], expected: string[]) {
  const norm = (s: string) => (s || '').toLowerCase();
  const L = labels.map(norm);
  const E = expected.map(norm);
  const matched = E.filter((e) => L.some((l) => l.includes(e) || e.includes(l)));
  const percent = Math.round((matched.length / Math.max(E.length, 1)) * 100);
  const missing = E.filter((e) => !matched.includes(e));
  return { percent, missing };
}

export const RubricPanel: React.FC<Props> = ({ expectedComponents, requirements, diagram, explanation }) => {
  const result = useMemo(() => {
    const nodeLabels: string[] = (diagram.nodes || []).map((n) => n.data?.labelText || n.label || n.type || '');

    const coverage = tokenCoverage(nodeLabels, expectedComponents);

    const expText = (explanation || '').toLowerCase();
    const sectionScores: Record<string, number> = {};

    // Base on explanation keyword hits
    sectionScores.problemUnderstanding = containsAny(expText, KEY_SETS.problemUnderstanding) ? 7 : 4;
    sectionScores.dataDesign = (containsAny(expText, KEY_SETS.dataDesign) ? 6 : 3) + (coverage.percent > 50 ? 2 : 0);
    sectionScores.modelSelection = containsAny(expText, KEY_SETS.modelSelection) ? 6 : 3;
    sectionScores.scalability = containsAny(expText, KEY_SETS.scalability) ? 6 : 3;
    sectionScores.monitoring = containsAny(expText, KEY_SETS.monitoring) ? 6 : 3;
    sectionScores.communication = containsAny(expText, KEY_SETS.communication) ? 6 : 4;

    // Clamp 0-10
    Object.keys(sectionScores).forEach((k) => {
      sectionScores[k] = Math.max(0, Math.min(10, sectionScores[k]));
    });

    const overall = Math.round(
      (sectionScores.problemUnderstanding + sectionScores.dataDesign + sectionScores.modelSelection + sectionScores.scalability + sectionScores.monitoring + sectionScores.communication) / 6
    );

    return {
      coverage,
      sectionScores,
      overall,
    };
  }, [expectedComponents, diagram, explanation]);

  return (
    <div className="border-t border-gray-700 bg-gray-900">
      <div className="px-4 py-3 flex items-center justify-between">
        <div className="text-white font-semibold" data-testid="ml-rubric-title">Rubric Score</div>
        <div className="text-sm text-gray-400" data-testid="ml-rubric-overall">Overall: {result.overall}/10</div>
      </div>

      <div className="px-4 pb-3 grid grid-cols-1 md:grid-cols-3 gap-3">
        {Object.entries(result.sectionScores).map(([key, value]) => (
          <div key={key} className="bg-gray-800 border border-gray-700 rounded p-3">
            <div className="text-xs text-gray-400" data-testid={`ml-rubric-${key}-label`}>
              {key.replace(/([A-Z])/g, ' $1').replace(/^./, (s) => s.toUpperCase())}
            </div>
            <div className="text-lg font-semibold text-white" data-testid={`ml-rubric-${key}-score`}>
              {value}/10
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
