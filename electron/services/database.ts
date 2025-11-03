import Database from 'better-sqlite3';
import * as fs from 'fs';
import * as path from 'path';

export class DatabaseService {
  private db!: Database.Database;
  private dbPath: string;

  constructor(dbPath: string) {
    this.dbPath = dbPath;
  }

  async initialize() {
    // Ensure directory exists
    const dir = path.dirname(this.dbPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    // Open database
    this.db = new Database(this.dbPath);
    this.db.pragma('journal_mode = WAL');

    // Read and execute schema
    const schemaPath = path.join(__dirname, '../../database/schema.sql');
    const schema = fs.readFileSync(schemaPath, 'utf-8');
    this.db.exec(schema);

    console.log('Database initialized at:', this.dbPath);
  }

  // User Management
  createUser(userData: { username: string; email: string; preferredLanguage?: string }) {
    const stmt = this.db.prepare(`
      INSERT INTO users (username, email, preferred_language)
      VALUES (?, ?, ?)
    `);
    const result = stmt.run(
      userData.username,
      userData.email,
      userData.preferredLanguage || 'python'
    );
    return { id: result.lastInsertRowid, ...userData };
  }

  loginUser(username: string) {
    const stmt = this.db.prepare(`
      UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE username = ?
    `);
    stmt.run(username);

    return this.db.prepare('SELECT * FROM users WHERE username = ?').get(username);
  }

  getAllUsers() {
    return this.db.prepare('SELECT * FROM users ORDER BY created_at DESC').all();
  }

  deleteUser(userId: number) {
    // Use transaction to ensure atomicity
    const deleteTransaction = this.db.transaction((userId: number) => {
      // The schema has ON DELETE CASCADE for most foreign keys, 
      // but we'll explicitly delete from tables that reference users
      // to ensure clean deletion
      
      // Delete from tables with foreign keys to users
      this.db.prepare('DELETE FROM code_submissions WHERE user_id = ?').run(userId);
      this.db.prepare('DELETE FROM design_submissions WHERE user_id = ?').run(userId);
      this.db.prepare('DELETE FROM feedback WHERE user_id = ?').run(userId);
      this.db.prepare('DELETE FROM user_progress WHERE user_id = ?').run(userId);
      this.db.prepare('DELETE FROM user_preferences WHERE user_id = ?').run(userId);
      this.db.prepare('DELETE FROM mock_interviews WHERE user_id = ?').run(userId);
      
      // Finally delete the user
      const stmt = this.db.prepare('DELETE FROM users WHERE id = ?');
      const result = stmt.run(userId);
      return result;
    });
    
    const result = deleteTransaction(userId);
    return { success: result.changes > 0, deletedId: userId };
  }

  updateUserPreferences(userId: number, preferences: any) {
    const stmt = this.db.prepare(`
      INSERT INTO user_preferences (user_id, theme, editor_font_size, editor_theme, auto_save, show_hints)
      VALUES (?, ?, ?, ?, ?, ?)
      ON CONFLICT(user_id) DO UPDATE SET
        theme = excluded.theme,
        editor_font_size = excluded.editor_font_size,
        editor_theme = excluded.editor_theme,
        auto_save = excluded.auto_save,
        show_hints = excluded.show_hints
    `);
    stmt.run(
      userId,
      preferences.theme,
      preferences.editorFontSize,
      preferences.editorTheme,
      preferences.autoSave ? 1 : 0,
      preferences.showHints ? 1 : 0
    );
  }

  // Questions
  getQuestions(category?: string, difficulty?: string) {
    let query = `
      SELECT q.*, qc.name as category_name
      FROM questions q
      JOIN question_categories qc ON q.category_id = qc.id
      WHERE 1=1
    `;
    const params: any[] = [];

    if (category) {
      query += ' AND qc.name = ?';
      params.push(category);
    }

    if (difficulty) {
      query += ' AND q.difficulty = ?';
      params.push(difficulty);
    }

    query += ' ORDER BY q.id';

    return this.db.prepare(query).all(...params);
  }

  getQuestionById(questionId: number) {
    return this.db.prepare(`
      SELECT q.*, qc.name as category_name
      FROM questions q
      JOIN question_categories qc ON q.category_id = qc.id
      WHERE q.id = ?
    `).get(questionId);
  }

  getLeetCodeQuestionDetails(questionId: number) {
    return this.db.prepare('SELECT * FROM leetcode_questions WHERE question_id = ?')
      .get(questionId);
  }

  getMLDesignQuestionDetails(questionId: number) {
    const result: any = this.db.prepare(`
      SELECT
        q.*,
        c.name as category_name,
        ml.*
      FROM questions q
      JOIN question_categories c ON q.category_id = c.id
      JOIN ml_design_questions ml ON q.id = ml.question_id
      WHERE q.id = ?
    `).get(questionId);

    if (!result) return null;

    // Parse JSON fields
    return {
      ...result,
      requirements: result.requirements ? JSON.parse(result.requirements) : [],
      evaluation_criteria: result.evaluation_criteria ? JSON.parse(result.evaluation_criteria) : {},
      key_components: result.key_components ? JSON.parse(result.key_components) : [],
    };
  }

  // Code Submissions
  createCodeSubmission(data: any) {
    const stmt = this.db.prepare(`
      INSERT INTO code_submissions 
      (user_id, question_id, language, code, custom_test_cases, 
       execution_time_ms, memory_used_kb, test_results, status)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    `);
    const result = stmt.run(
      data.userId,
      data.questionId,
      data.language,
      data.code,
      data.customTestCases,
      data.executionTimeMs,
      data.memoryUsedKb,
      data.testResults,
      data.status
    );
    return { id: result.lastInsertRowid, ...data };
  }

  getCodeSubmission(submissionId: number) {
    return this.db.prepare('SELECT * FROM code_submissions WHERE id = ?')
      .get(submissionId);
  }

  // Design Submissions
  createDesignSubmission(data: any) {
    const stmt = this.db.prepare(`
      INSERT INTO design_submissions 
      (user_id, question_id, diagram_data, written_explanation, time_spent_seconds)
      VALUES (?, ?, ?, ?, ?)
    `);
    const result = stmt.run(
      data.userId,
      data.questionId,
      data.diagramData,
      data.writtenExplanation,
      data.timeSpentSeconds
    );
    return { id: result.lastInsertRowid, ...data };
  }

  getDesignSubmission(submissionId: number) {
    return this.db.prepare('SELECT * FROM design_submissions WHERE id = ?')
      .get(submissionId);
  }

  // Mock Interviews
  createMockInterview(userId: number, interviewType: string) {
    const stmt = this.db.prepare(`
      INSERT INTO mock_interviews (user_id, interview_type)
      VALUES (?, ?)
    `);
    const result = stmt.run(userId, interviewType);
    return { id: result.lastInsertRowid, userId, interviewType };
  }

  completeMockInterview(mockId: number) {
    const stmt = this.db.prepare(`
      UPDATE mock_interviews 
      SET completed_at = CURRENT_TIMESTAMP,
          status = 'completed'
      WHERE id = ?
    `);
    stmt.run(mockId);
    return this.db.prepare('SELECT * FROM mock_interviews WHERE id = ?').get(mockId);
  }

  getMockInterviewQuestions(mockId: number) {
    return this.db.prepare(`
      SELECT miq.*, q.title, q.difficulty
      FROM mock_interview_questions miq
      JOIN questions q ON miq.question_id = q.id
      WHERE miq.mock_interview_id = ?
      ORDER BY miq.order_index
    `).all(mockId);
  }

  addQuestionToMockInterview(mockId: number, questionId: number, orderIndex: number) {
    const stmt = this.db.prepare(`
      INSERT INTO mock_interview_questions (mock_interview_id, question_id, order_index)
      VALUES (?, ?, ?)
    `);
    stmt.run(mockId, questionId, orderIndex);
  }

  // Feedback
  createFeedback(data: any) {
    const stmt = this.db.prepare(`
      INSERT INTO feedback 
      (user_id, submission_id, submission_type, mock_interview_id, 
       feedback_text, scores, strengths, improvements)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    `);
    const result = stmt.run(
      data.userId,
      data.submissionId,
      data.submissionType,
      data.mockInterviewId || null,
      data.feedbackText,
      data.scores,
      data.strengths,
      data.improvements
    );
    return { id: result.lastInsertRowid, ...data };
  }

  getUserFeedback(userId: number, limit: number = 10) {
    return this.db.prepare(`
      SELECT f.*, q.title as question_title
      FROM feedback f
      LEFT JOIN code_submissions cs ON f.submission_id = cs.id AND f.submission_type = 'code'
      LEFT JOIN design_submissions ds ON f.submission_id = ds.id AND f.submission_type = 'design'
      LEFT JOIN questions q ON COALESCE(cs.question_id, ds.question_id) = q.id
      WHERE f.user_id = ?
      ORDER BY f.generated_at DESC
      LIMIT ?
    `).all(userId, limit);
  }

  // Progress
  updateProgress(userId: number, questionId: number, solved: boolean) {
    const stmt = this.db.prepare(`
      INSERT INTO user_progress (user_id, question_id, attempts, solved, first_attempt_at, last_attempt_at)
      VALUES (?, ?, 1, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
      ON CONFLICT(user_id, question_id) DO UPDATE SET
        attempts = attempts + 1,
        solved = CASE WHEN solved = 1 THEN 1 ELSE ? END,
        last_attempt_at = CURRENT_TIMESTAMP
    `);
    stmt.run(userId, questionId, solved ? 1 : 0, solved ? 1 : 0);
  }

  getUserProgress(userId: number) {
    return this.db.prepare(`
      SELECT up.*, q.title, q.difficulty, qc.name as category
      FROM user_progress up
      JOIN questions q ON up.question_id = q.id
      JOIN question_categories qc ON q.category_id = qc.id
      WHERE up.user_id = ?
      ORDER BY up.last_attempt_at DESC
    `).all(userId);
  }

  getUserStats(userId: number) {
    const stats = this.db.prepare(`
      SELECT 
        COUNT(*) as total_attempts,
        SUM(CASE WHEN solved = 1 THEN 1 ELSE 0 END) as solved_count,
        SUM(total_time_spent_seconds) as total_time_spent
      FROM user_progress
      WHERE user_id = ?
    `).get(userId);

    const byDifficulty = this.db.prepare(`
      SELECT
        q.difficulty,
        COUNT(*) as attempts,
        SUM(CASE WHEN up.solved = 1 THEN 1 ELSE 0 END) as solved
      FROM user_progress up
      JOIN questions q ON up.question_id = q.id
      WHERE up.user_id = ?
      GROUP BY q.difficulty
    `).all(userId);

    return { ...(stats as object), byDifficulty };
  }

  getSubmissionHistory(userId: number, limit: number = 20) {
    const codeSubmissions = this.db.prepare(`
      SELECT 'code' as type, cs.*, q.title, q.difficulty
      FROM code_submissions cs
      JOIN questions q ON cs.question_id = q.id
      WHERE cs.user_id = ?
      ORDER BY cs.submitted_at DESC
      LIMIT ?
    `).all(userId, limit);

    const designSubmissions = this.db.prepare(`
      SELECT 'design' as type, ds.*, q.title, q.difficulty
      FROM design_submissions ds
      JOIN questions q ON ds.question_id = q.id
      WHERE ds.user_id = ?
      ORDER BY ds.submitted_at DESC
      LIMIT ?
    `).all(userId, limit);

    return [...codeSubmissions, ...designSubmissions]
      .sort((a: any, b: any) => 
        new Date(b.submitted_at).getTime() - new Date(a.submitted_at).getTime()
      )
      .slice(0, limit);
  }

  close() {
    this.db.close();
  }
}
