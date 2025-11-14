import fetch from 'node-fetch';
import type { SubmissionForFeedback, QuestionForFeedback } from './llmProviderFactory';
import { retryWithBackoff } from '../utils/retry';

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

export class LocalLLMService {
  private baseUrl: string;
  private model: string;

  constructor(baseUrl: string = 'http://localhost:8000', model: string = 'gpt-oss-20b') {
    this.baseUrl = baseUrl;
    this.model = model;
  }

  getProviderName(): string {
    return 'local';
  }

  async generateFeedback(
    submission: SubmissionForFeedback,
    question: QuestionForFeedback,
    submissionType: 'code' | 'design'
  ): Promise<FeedbackResponse> {
    const prompt = submissionType === 'code'
      ? this.buildCodeFeedbackPrompt(submission, question)
      : this.buildDesignFeedbackPrompt(submission, question);

    // Wrap API call with retry logic
    return retryWithBackoff(async () => {
      try {
        // OpenAI-compatible API call
        const response = await fetch(`${this.baseUrl}/v1/chat/completions`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model: this.model,
            messages: [
              {
                role: 'system',
                content: 'You are an expert technical interviewer providing detailed feedback on coding problems and system design. Always respond with valid JSON only.'
              },
              {
                role: 'user',
                content: prompt,
              },
            ],
            max_tokens: 2000,
            temperature: 0.7,
          }),
        });

        if (!response.ok) {
          const errorText = await response.text();
          throw new Error(`LLM API error: ${response.status} ${response.statusText} - ${errorText}`);
        }

        const data = await response.json() as any;
        const responseText = data.choices[0].message.content;

        return this.parseFeedbackResponse(responseText);
      } catch (error: any) {
        throw new Error(`Failed to generate feedback: ${error.message}`);
      }
    }, {
      maxRetries: 3,
      baseDelay: 2000, // Start with 2s delay for LLM APIs
      maxDelay: 15000, // Max 15s delay
    });
  }

  private buildCodeFeedbackPrompt(submission: SubmissionForFeedback, question: QuestionForFeedback): string {
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

  private buildDesignFeedbackPrompt(submission: SubmissionForFeedback, question: QuestionForFeedback): string {
    const keyComponents = JSON.parse(question.key_components);

    return `You are an expert ML system design interviewer at Meta providing feedback on a senior-level ML system design question.

**Problem:**
${question.scenario}

**Requirements:**
${JSON.parse(question.requirements).map((r: string, i: number) => `${i + 1}. ${r}`).join('\n')}

**Key Components to Evaluate:**
${keyComponents.map((c: string, i: number) => `${i + 1}. ${c}`).join('\n')}

**Candidate's Written Explanation:**
${submission.written_explanation}

**Candidate's System Diagram:**
[Diagram includes: ${this.extractDiagramSummary(JSON.parse(submission.diagram_data))}]

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

  private extractDiagramSummary(diagramData: { nodes?: Array<{ type?: string; [key: string]: unknown }>; edges?: unknown[] }): string {
    const nodes = diagramData.nodes || [];
    const edges = diagramData.edges || [];
    const nodeTypes = nodes.map((n: any) => n.type || 'default');
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
      // Fallback to using raw response if parsing fails
      return {
        text: responseText,
        scores: {},
        strengths: [],
        improvements: [],
      };
    }
  }

  private buildFeedbackText(parsed: Record<string, unknown>): string {
    let text = `## Summary\n${parsed.summary}\n\n`;

    // Scores
    text += `## Scores\n`;
    for (const [key, value] of Object.entries(parsed.scores)) {
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
