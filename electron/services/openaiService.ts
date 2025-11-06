import OpenAI from 'openai';

interface FeedbackResponse {
  text: string;
  scores: {
    correctness?: number;
    efficiency?: number;
    codeQuality?: number;
    problemUnderstanding?: number;
    systemDesign?: number;
    scalability?: number;
    communication?: number;
  };
  strengths: string[];
  improvements: string[];
}

function ensureArray<T = any>(value: any): T[] {
  if (Array.isArray(value)) return value as T[];
  if (typeof value === 'string') {
    try {
      const parsed = JSON.parse(value);
      return Array.isArray(parsed) ? (parsed as T[]) : [];
    } catch {
      return [];
    }
  }
  return [];
}

function ensureObject<T = Record<string, any>>(value: any): T {
  if (value && typeof value === 'object' && !Array.isArray(value)) return value as T;
  if (typeof value === 'string') {
    try {
      const parsed = JSON.parse(value);
      return parsed && typeof parsed === 'object' && !Array.isArray(parsed)
        ? (parsed as T)
        : ({} as T);
    } catch {
      return {} as T;
    }
  }
  return {} as T;
}

export class OpenAIService {
  private client: OpenAI | null = null;
  private model: string;

  constructor(apiKey: string, model: string = 'gpt-4o') {
    this.model = model;
    if (apiKey) {
      this.client = new OpenAI({ apiKey });
      console.log(`OpenAI configured with model: ${this.model}`);
    } else {
      console.warn('OpenAI API key not provided. Feedback generation will be disabled.');
    }
  }

  getProviderName(): string {
    return 'openai';
  }

  async generateFeedback(
    submission: any,
    question: any,
    submissionType: 'code' | 'design'
  ): Promise<FeedbackResponse> {
    if (!this.client) {
      throw new Error('OpenAI API not configured');
    }

    const prompt = submissionType === 'code'
      ? this.buildCodeFeedbackPrompt(submission, question)
      : this.buildDesignFeedbackPrompt(submission, question);

    try {
      const response = await this.client.chat.completions.create({
        model: this.model,
        messages: [
          {
            role: 'system',
            content: 'You are an expert technical interviewer providing detailed feedback on coding problems and system design. Always respond with valid JSON only.',
          },
          {
            role: 'user',
            content: prompt,
          },
        ],
        max_tokens: 2000,
        temperature: 0.7,
      });

      const responseText = response.choices[0].message.content || '';
      return this.parseFeedbackResponse(responseText);
    } catch (error: any) {
      console.error('Error generating feedback with OpenAI:', error);
      throw new Error(`Failed to generate feedback: ${error.message}`);
    }
  }

  private buildCodeFeedbackPrompt(submission: any, question: any): string {
    const testResults = JSON.parse(submission.test_results);
    const passedTests = testResults.filter((t: any) => t.passed).length;
    const totalTests = testResults.length;

    return `You are an expert technical interviewer providing feedback on a LeetCode-style coding problem solution.

**Problem:**
${question.description}

**Difficulty:** ${question.difficulty}

**Expected Complexity:**
- Time: ${question.expected_time_complexity || 'Not specified'}
- Space: ${question.expected_space_complexity || 'Not specified'}

**Candidate's Solution (${submission.language}):**
\`\`\`${submission.language}
${submission.code}
\`\`\`

**Test Results:**
- Passed: ${passedTests}/${totalTests} tests
- Execution Time: ${submission.execution_time_ms}ms
- Memory Used: ${submission.memory_used_kb}KB

Please provide comprehensive feedback in the following JSON format:

{
  "summary": "Brief 2-3 sentence overview of the solution",
  "scores": {
    "correctness": 0-10,
    "efficiency": 0-10,
    "codeQuality": 0-10
  },
  "strengths": ["strength 1", "strength 2", "..."],
  "improvements": ["improvement 1", "improvement 2", "..."],
  "detailedAnalysis": {
    "correctness": "Analysis of correctness",
    "timeComplexity": "Time complexity analysis with explanation",
    "spaceComplexity": "Space complexity analysis with explanation",
    "codeStyle": "Code quality and style feedback",
    "edgeCases": "Discussion of edge cases handled or missed"
  },
  "suggestions": "Specific actionable suggestions for improvement"
}

Focus on:
1. Correctness of the solution
2. Time and space complexity analysis
3. Code quality, readability, and style
4. Edge case handling
5. Alternative approaches if applicable

Be constructive, specific, and educational in your feedback. Respond ONLY with valid JSON, no markdown formatting.`;
  }

  private buildDesignFeedbackPrompt(submission: any, question: any): string {
    const keyComponents = ensureArray<string>(question.key_components);
    const requirements = ensureArray<string>(question.requirements);
    const evaluationCriteria = ensureObject<Record<string, string>>(question.evaluation_criteria);

    let diagramSummary = '';
    try {
      const parsedDiagram = typeof submission.diagram_data === 'string'
        ? JSON.parse(submission.diagram_data)
        : submission.diagram_data;
      diagramSummary = this.extractDiagramSummary(parsedDiagram);
    } catch {
      diagramSummary = 'Diagram data unavailable or invalid';
    }

    return `You are an expert ML system design interviewer at Meta providing feedback on a senior-level ML system design question.

**Problem:**
${question.scenario}

**Requirements:**
${requirements.map((r: string, i: number) => `${i + 1}. ${r}`).join('\n')}

**Key Components to Evaluate:**
${keyComponents.map((c: string, i: number) => `${i + 1}. ${c}`).join('\n')}

**Candidate's Written Explanation:**
${submission.written_explanation}

**Candidate's System Diagram:**
[Diagram includes: ${diagramSummary}]

**Time Spent:** ${Math.round(submission.time_spent_seconds / 60)} minutes

Please provide comprehensive feedback in the following JSON format:

{
  "summary": "Brief 2-3 sentence overview of the design",
  "scores": {
    "problemUnderstanding": 0-10,
    "systemDesign": 0-10,
    "scalability": 0-10,
    "communication": 0-10
  },
  "strengths": ["strength 1", "strength 2", "..."],
  "improvements": ["improvement 1", "improvement 2", "..."],
  "detailedAnalysis": {
    "problemUnderstanding": "How well they understood the problem",
    "dataDesign": "Data pipeline and feature engineering approach",
    "modelSelection": "Choice and justification of ML models",
    "scalability": "System scalability and performance considerations",
    "monitoring": "Monitoring, evaluation, and maintenance strategy",
    "tradeoffs": "Discussion of tradeoffs and alternatives",
    "communication": "Clarity and structure of explanation"
  },
  "missingComponents": ["component 1", "component 2", "..."],
  "suggestions": "Specific actionable suggestions for improvement"
}

Evaluate based on Meta's senior ML SWE standards:
1. Problem understanding and clarifying questions
2. Data pipeline design and feature engineering
3. Model selection and justification
4. System architecture and scalability
5. Monitoring, evaluation, and A/B testing strategy
6. Discussion of tradeoffs and alternatives
7. Communication clarity and structure

Be thorough, constructive, and specific. Consider this is for a senior-level position. Respond ONLY with valid JSON, no markdown formatting.`;
  }

  private extractDiagramSummary(diagramData: any): string {
    const nodes = diagramData?.nodes || [];
    const edges = diagramData?.edges || [];
    const nodeTypes = nodes.map((n: any) => n.type || n.typeKey || n?.data?.typeKey || 'component');
    const uniqueNodeTypes = [...new Set(nodeTypes)];
    return `${nodes.length} components (${uniqueNodeTypes.join(', ')}), ${edges.length} connections`;
  }

  private parseFeedbackResponse(responseText: string): FeedbackResponse {
    try {
      // Try to extract JSON from markdown code blocks if present
      let jsonText = responseText.trim();

      // Remove markdown code blocks
      const jsonMatch = responseText.match(/```(?:json)?\s*\n?([\s\S]*?)\n?```/);
      if (jsonMatch) {
        jsonText = jsonMatch[1].trim();
      }

      // Try to find JSON object in the text
      const jsonObjectMatch = jsonText.match(/\{[\s\S]*\}/);
      if (jsonObjectMatch) {
        jsonText = jsonObjectMatch[0];
      }

      const parsed = JSON.parse(jsonText);

      // Build comprehensive feedback text
      const feedbackText = this.buildFeedbackText(parsed);

      return {
        text: feedbackText,
        scores: parsed.scores || {},
        strengths: parsed.strengths || [],
        improvements: parsed.improvements || [],
      };
    } catch (error) {
      console.error('Error parsing feedback response:', error);
      console.error('Raw response:', responseText);

      // Fallback to using raw response
      return {
        text: responseText,
        scores: {},
        strengths: [],
        improvements: [],
      };
    }
  }

  private buildFeedbackText(parsed: any): string {
    let text = `## Summary\n${parsed.summary}\n\n`;

    // Scores
    text += `## Scores\n`;
    for (const [key, value] of Object.entries(parsed.scores || {})) {
      const label = key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
      text += `- **${label}:** ${value}/10\n`;
    }
    text += '\n';

    // Strengths
    if (parsed.strengths && parsed.strengths.length > 0) {
      text += `## Strengths\n`;
      parsed.strengths.forEach((s: string) => {
        text += `- ${s}\n`;
      });
      text += '\n';
    }

    // Areas for Improvement
    if (parsed.improvements && parsed.improvements.length > 0) {
      text += `## Areas for Improvement\n`;
      parsed.improvements.forEach((i: string) => {
        text += `- ${i}\n`;
      });
      text += '\n';
    }

    // Detailed Analysis
    if (parsed.detailedAnalysis) {
      text += `## Detailed Analysis\n`;
      for (const [key, value] of Object.entries(parsed.detailedAnalysis)) {
        const label = key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
        text += `\n### ${label}\n${value}\n`;
      }
      text += '\n';
    }

    // Missing Components (for design)
    if (parsed.missingComponents && parsed.missingComponents.length > 0) {
      text += `## Missing Components\n`;
      parsed.missingComponents.forEach((c: string) => {
        text += `- ${c}\n`;
      });
      text += '\n';
    }

    // Suggestions
    if (parsed.suggestions) {
      text += `## Suggestions\n${parsed.suggestions}\n`;
    }

    return text;
  }
}
