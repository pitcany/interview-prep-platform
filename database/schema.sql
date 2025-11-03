-- Interview Prep Platform Database Schema

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    preferred_language TEXT DEFAULT 'python' -- Default coding language
);

-- Question categories
CREATE TABLE IF NOT EXISTS question_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL, -- 'leetcode' or 'ml_system_design'
    description TEXT
);

-- Questions table
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    difficulty TEXT NOT NULL, -- 'easy', 'medium', 'hard'
    description TEXT NOT NULL,
    constraints TEXT, -- JSON string
    examples TEXT, -- JSON array of examples
    hints TEXT, -- JSON array of hints
    tags TEXT, -- JSON array of tags (e.g., ['arrays', 'dynamic-programming'])
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES question_categories(id)
);

-- LeetCode specific data
CREATE TABLE IF NOT EXISTS leetcode_questions (
    question_id INTEGER PRIMARY KEY,
    function_signature_python TEXT,
    function_signature_java TEXT,
    function_signature_cpp TEXT,
    test_cases TEXT NOT NULL, -- JSON array of test cases
    expected_time_complexity TEXT,
    expected_space_complexity TEXT,
    solution_python TEXT,
    solution_java TEXT,
    solution_cpp TEXT,
    solution_explanation TEXT,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);

-- ML System Design specific data
CREATE TABLE IF NOT EXISTS ml_design_questions (
    question_id INTEGER PRIMARY KEY,
    scenario TEXT NOT NULL, -- Detailed scenario description
    requirements TEXT NOT NULL, -- JSON array of requirements
    evaluation_criteria TEXT NOT NULL, -- JSON object with criteria
    sample_solution TEXT, -- Markdown/HTML reference solution
    key_components TEXT, -- JSON array of key components to cover
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);

-- User submissions for LeetCode
CREATE TABLE IF NOT EXISTS code_submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    language TEXT NOT NULL, -- 'python', 'java', 'cpp'
    code TEXT NOT NULL,
    custom_test_cases TEXT, -- JSON array of custom test cases
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    execution_time_ms INTEGER,
    memory_used_kb INTEGER,
    test_results TEXT, -- JSON object with test results
    status TEXT, -- 'passed', 'failed', 'error', 'timeout'
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);

-- User submissions for ML System Design
CREATE TABLE IF NOT EXISTS design_submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    diagram_data TEXT NOT NULL, -- JSON for React Flow diagram
    written_explanation TEXT, -- User's written approach
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    time_spent_seconds INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);

-- Mock interview sessions
CREATE TABLE IF NOT EXISTS mock_interviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    interview_type TEXT NOT NULL, -- 'leetcode' or 'ml_design'
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    duration_seconds INTEGER DEFAULT 1800, -- 30 minutes
    status TEXT DEFAULT 'in_progress', -- 'in_progress', 'completed', 'abandoned'
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Questions in mock interviews
CREATE TABLE IF NOT EXISTS mock_interview_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mock_interview_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    order_index INTEGER NOT NULL,
    submission_id INTEGER, -- Links to code_submissions or design_submissions
    submission_type TEXT, -- 'code' or 'design'
    FOREIGN KEY (mock_interview_id) REFERENCES mock_interviews(id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

-- AI-generated feedback
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    submission_id INTEGER NOT NULL,
    submission_type TEXT NOT NULL, -- 'code' or 'design'
    mock_interview_id INTEGER, -- NULL if not part of mock interview
    feedback_text TEXT NOT NULL, -- AI-generated feedback
    scores TEXT, -- JSON object with scores (e.g., {"correctness": 8, "efficiency": 7})
    strengths TEXT, -- JSON array of strengths
    improvements TEXT, -- JSON array of areas to improve
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (mock_interview_id) REFERENCES mock_interviews(id) ON DELETE CASCADE
);

-- Progress tracking
CREATE TABLE IF NOT EXISTS user_progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    attempts INTEGER DEFAULT 0,
    solved BOOLEAN DEFAULT 0,
    first_attempt_at TIMESTAMP,
    last_attempt_at TIMESTAMP,
    best_time_ms INTEGER, -- Best execution time for LeetCode
    total_time_spent_seconds INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE,
    UNIQUE(user_id, question_id)
);

-- User preferences
CREATE TABLE IF NOT EXISTS user_preferences (
    user_id INTEGER PRIMARY KEY,
    theme TEXT DEFAULT 'dark', -- 'dark' or 'light'
    editor_font_size INTEGER DEFAULT 14,
    editor_theme TEXT DEFAULT 'vs-dark',
    auto_save BOOLEAN DEFAULT 1,
    show_hints BOOLEAN DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_submissions_user ON code_submissions(user_id);
CREATE INDEX IF NOT EXISTS idx_submissions_question ON code_submissions(question_id);
CREATE INDEX IF NOT EXISTS idx_design_submissions_user ON design_submissions(user_id);
CREATE INDEX IF NOT EXISTS idx_design_submissions_question ON design_submissions(question_id);
CREATE INDEX IF NOT EXISTS idx_progress_user ON user_progress(user_id);
CREATE INDEX IF NOT EXISTS idx_progress_question ON user_progress(question_id);
CREATE INDEX IF NOT EXISTS idx_feedback_user ON feedback(user_id);
CREATE INDEX IF NOT EXISTS idx_mock_interview_user ON mock_interviews(user_id);
CREATE INDEX IF NOT EXISTS idx_questions_category ON questions(category_id);
CREATE INDEX IF NOT EXISTS idx_questions_difficulty ON questions(difficulty);

-- Insert default categories
INSERT OR IGNORE INTO question_categories (id, name, description) VALUES 
    (1, 'leetcode', 'LeetCode-style coding problems'),
    (2, 'ml_system_design', 'Machine Learning System Design questions');
