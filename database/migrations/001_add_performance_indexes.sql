-- Migration: Add performance indexes
-- Date: 2025-01-15
-- Description: Add missing composite indexes for better query performance

-- Composite index for submission history queries (sorted by time)
CREATE INDEX IF NOT EXISTS idx_submissions_user_time ON code_submissions(user_id, submitted_at DESC);
CREATE INDEX IF NOT EXISTS idx_design_submissions_user_time ON design_submissions(user_id, submitted_at DESC);

-- Composite index for progress lookups by user and question
-- (Note: UNIQUE constraint already creates an index, but explicit index helps query planner)
CREATE INDEX IF NOT EXISTS idx_progress_user_question ON user_progress(user_id, question_id);

-- Index for feedback lookups by submission
CREATE INDEX IF NOT EXISTS idx_feedback_submission ON feedback(submission_id, submission_type);

-- Index for feedback lookups by mock interview
CREATE INDEX IF NOT EXISTS idx_feedback_mock_interview ON feedback(mock_interview_id);

-- Composite index for mock interview filtering by user and status
CREATE INDEX IF NOT EXISTS idx_mock_interview_user_status ON mock_interviews(user_id, status);

-- Verify indexes were created
-- Run this query to check:
-- SELECT name, sql FROM sqlite_master WHERE type='index' AND tbl_name IN ('code_submissions', 'design_submissions', 'user_progress', 'feedback', 'mock_interviews');
