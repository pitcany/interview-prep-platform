import Anthropic from '@anthropic-ai/sdk';

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

export class ClaudeAPIService {
  private client: Anthropic | null = null;

  constructor(apiKey: string) {
    if (apiKey) {
      this.client = new Anthropic({ apiKey });
    } else {
      console.warn('Claude API key not provided. Feedback generation will be disabled.');
    }
  }

  async generateFeedback(
    submission: any,
    question: any,
    submissionType: 'code' | 'design'
  ): Promise<FeedbackResponse> {
    if (!this.client) {
      throw new Error('Claude API not configured');
    }

    const prompt = submissionType === 'code' 
      ? this.buildCodeFeedbackPrompt(submission, question)
      : this.buildDesignFeedbackPrompt(submission, question);

    try {
      const message = await this.client.messages.create({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 2000,
        messages: [
          {
            role: 'user',
            content: prompt,
          },
        ],
      });

      const responseText = message.content[0].type === 'text' 
        ? message.content[0].text 
        : '';

      return this.parseFeedbackResponse(responseText, submissionType);
    } catch (error: any) {
      console.error('Error generating feedback:', error);
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

Be constructive, specific, and educational in your feedback.`;
  }

  private buildDesignFeedbackPrompt(submission: any, question: any): string {
    const evaluationCriteria = JSON.parse(question.evaluation_criteria);
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

Be thorough, constructive, and specific. Consider this is for a senior-level position.`;
  }

  private extractDiagramSummary(diagramData: any): string {
    // Extract key info from React Flow diagram
    const nodes = diagramData.nodes || [];
    const edges = diagramData.edges || [];
    
    const nodeTypes = nodes.map((n: any) => n.type || 'default');
    const uniqueNodeTypes = [...new Set(nodeTypes)];
    
    return `${nodes.length} components (${uniqueNodeTypes.join(', ')}), ${edges.length} connections`;
  }

  private parseFeedbackResponse(responseText: string, submissionType: string): FeedbackResponse {
    try {
      // Try to extract JSON from markdown code blocks if present
      let jsonText = responseText;
      const jsonMatch = responseText.match(/```json\n([\s\S]*?)\n```/);
      if (jsonMatch) {
        jsonText = jsonMatch[1];
      }

      const parsed = JSON.parse(jsonText);

      // Build comprehensive feedback text
      const feedbackText = this.buildFeedbackText(parsed, submissionType);

      return {
        text: feedbackText,
        scores: parsed.scores || {},
        strengths: parsed.strengths || [],
        improvements: parsed.improvements || [],
      };
    } catch (error) {
      console.error('Error parsing feedback response:', error);
      
      // Fallback to using raw response
      return {
        text: responseText,
        scores: {},
        strengths: [],
        improvements: [],
      };
    }
  }

  private buildFeedbackText(parsed: any, submissionType: string): string {
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
