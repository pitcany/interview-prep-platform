import React, { useCallback, useState } from 'react';
import {
  ReactFlow,
  Node,
  Edge,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  addEdge,
  Connection,
  MarkerType,
  BackgroundVariant,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import { toPng } from 'html-to-image';
import {
  Database,
  GitBranch,
  Brain,
  Server,
  Wifi,
  Activity,
  Save,
  Download,
  Trash2,
  Plus,
  X,
} from 'lucide-react';

// Node types for ML systems
export const nodeTypes = {
  data: 'Data Source',
  processing: 'Data Processing',
  model: 'ML Model',
  service: 'Service',
  api: 'API',
  monitoring: 'Monitoring',
};

interface DiagramEditorProps {
  initialNodes?: Node[];
  initialEdges?: Edge[];
  onSave?: (nodes: Node[], edges: Edge[]) => void;
  readOnly?: boolean;
}

// Custom node style function
const getNodeStyle = (type: string) => {
  const baseStyle = {
    padding: '12px 16px',
    borderRadius: '8px',
    border: '2px solid',
    fontSize: '14px',
    fontWeight: '500',
    minWidth: '160px',
    textAlign: 'center' as const,
  };

  const styles: Record<string, any> = {
    data: {
      ...baseStyle,
      backgroundColor: '#1e40af',
      borderColor: '#3b82f6',
      color: '#fff',
    },
    processing: {
      ...baseStyle,
      backgroundColor: '#7c3aed',
      borderColor: '#a78bfa',
      color: '#fff',
    },
    model: {
      ...baseStyle,
      backgroundColor: '#dc2626',
      borderColor: '#f87171',
      color: '#fff',
    },
    service: {
      ...baseStyle,
      backgroundColor: '#059669',
      borderColor: '#34d399',
      color: '#fff',
    },
    api: {
      ...baseStyle,
      backgroundColor: '#d97706',
      borderColor: '#fbbf24',
      color: '#fff',
    },
    monitoring: {
      ...baseStyle,
      backgroundColor: '#7c2d12',
      borderColor: '#fb923c',
      color: '#fff',
    },
  };

  return styles[type] || baseStyle;
};

// Node icon component
const NodeIcon = ({ type }: { type: string }) => {
  const icons: Record<string, any> = {
    data: Database,
    processing: GitBranch,
    model: Brain,
    service: Server,
    api: Wifi,
    monitoring: Activity,
  };

  const Icon = icons[type] || Database;
  return <Icon size={20} className="inline mr-2" />;
};

export default function DiagramEditor({
  initialNodes = [],
  initialEdges = [],
  onSave,
  readOnly = false,
}: DiagramEditorProps) {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
  const [selectedNodeType, setSelectedNodeType] = useState<string>('data');
  const [nodeCounter, setNodeCounter] = useState(1);
  const [showInstructions, setShowInstructions] = useState(true);

  const onConnect = useCallback(
    (params: Connection) => {
      const edge = {
        ...params,
        type: 'smoothstep',
        animated: true,
        style: { stroke: '#6b7280', strokeWidth: 2 },
        markerEnd: {
          type: MarkerType.ArrowClosed,
          color: '#6b7280',
        },
      };
      setEdges((eds) => addEdge(edge, eds));
    },
    [setEdges]
  );

  const addNode = (type: string) => {
    const labelText = nodeTypes[type as keyof typeof nodeTypes] || 'Component';
    const newNode: Node = {
      id: `node_${nodeCounter}`,
      type: 'default',
      position: {
        x: Math.random() * 400 + 100,
        y: Math.random() * 300 + 100,
      },
      data: {
        label: (
          <div>
            <NodeIcon type={type} />
            {labelText}
          </div>
        ),
        typeKey: type,
        labelText,
      },
      style: getNodeStyle(type),
    };

    setNodes((nds) => [...nds, newNode]);
    setNodeCounter((c) => c + 1);
  };

  const handleSave = () => {
    if (onSave) {
      onSave(nodes, edges);
    }
  };

  const handleExportPNG = async () => {
    const element = document.querySelector('.react-flow') as HTMLElement;
    if (!element) return;

    try {
      const dataUrl = await toPng(element, {
        backgroundColor: '#111827',
        width: element.offsetWidth,
        height: element.offsetHeight,
      });

      const link = document.createElement('a');
      link.download = 'ml-system-diagram.png';
      link.href = dataUrl;
      link.click();
    } catch (error) {
      console.error('Failed to export diagram:', error);
    }
  };

  const handleClear = () => {
    if (window.confirm('Clear all nodes and edges?')) {
      setNodes([]);
      setEdges([]);
    }
  };

  return (
    <div className="h-full flex flex-col bg-gray-900">
      {/* Toolbar */}
      {!readOnly && (
        <div className="bg-gray-800 border-b border-gray-700 p-3">
          <div className="flex items-center justify-between">
            {/* Node Palette */}
            <div className="flex items-center gap-2">
              <span className="text-sm text-gray-400 mr-2">Add Node:</span>
              {Object.entries(nodeTypes).map(([type, label]) => (
                <button
                  key={type}
                  onClick={() => addNode(type)}
                  className="px-3 py-1.5 bg-gray-700 hover:bg-gray-600 rounded text-sm text-white transition-colors flex items-center gap-1"
                  title={`Add ${label}`}
                >
                  <NodeIcon type={type} />
                  <Plus size={14} />
                </button>
              ))}
            </div>

            {/* Actions */}
            <div className="flex items-center gap-2">
              {onSave && (
                <button
                  onClick={handleSave}
                  className="px-3 py-1.5 bg-blue-600 hover:bg-blue-700 rounded text-sm text-white transition-colors flex items-center gap-2"
                >
                  <Save size={16} />
                  Save
                </button>
              )}
              <button
                onClick={handleExportPNG}
                className="px-3 py-1.5 bg-green-600 hover:bg-green-700 rounded text-sm text-white transition-colors flex items-center gap-2"
              >
                <Download size={16} />
                Export PNG
              </button>
              <button
                onClick={handleClear}
                className="px-3 py-1.5 bg-red-600 hover:bg-red-700 rounded text-sm text-white transition-colors flex items-center gap-2"
              >
                <Trash2 size={16} />
                Clear
              </button>
            </div>
          </div>

          {/* Legend */}
          <div className="mt-3 pt-3 border-t border-gray-700 flex flex-wrap gap-3">
            {Object.entries(nodeTypes).map(([type, label]) => (
              <div key={type} className="flex items-center gap-2 text-xs">
                <div
                  className="w-4 h-4 rounded"
                  style={{ backgroundColor: getNodeStyle(type).backgroundColor }}
                />
                <span className="text-gray-400">{label}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* React Flow Canvas */}
      <div className="flex-1">
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          fitView
          attributionPosition="bottom-right"
          nodesDraggable={!readOnly}
          nodesConnectable={!readOnly}
          elementsSelectable={!readOnly}
        >
          <Background variant={BackgroundVariant.Dots} gap={16} size={1} color="#374151" />
          <Controls />
        </ReactFlow>
      </div>

      {/* Instructions */}
      {!readOnly && nodes.length === 0 && showInstructions && (
        <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
          <div className="bg-gray-800 border border-gray-700 rounded-lg p-6 text-center max-w-md pointer-events-auto relative">
            <button
              onClick={() => setShowInstructions(false)}
              className="absolute top-2 right-2 text-gray-400 hover:text-white transition-colors"
              title="Close instructions"
            >
              <X size={20} />
            </button>
            <Brain className="mx-auto mb-3 text-gray-500" size={48} />
            <h3 className="text-white font-semibold mb-2">
              Design Your ML System
            </h3>
            <p className="text-gray-400 text-sm">
              Click the buttons above to add components, then drag to position
              and connect them by dragging from one node to another.
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
