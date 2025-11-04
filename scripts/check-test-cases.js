#!/usr/bin/env electron

const Database = require('better-sqlite3');
const path = require('path');
const os = require('os');

const dbPath = path.join(
  os.homedir(),
  '.config',
  'interview-prep-platform',
  'interview-prep.db'
);

console.log('Checking test cases in database at:', dbPath);

try {
  const db = new Database(dbPath);

  // Check a few questions for test cases
  const questions = db.prepare(`
    SELECT
      q.id,
      q.title,
      lq.test_cases,
      lq.hidden_test_cases
    FROM questions q
    JOIN leetcode_questions lq ON q.id = lq.question_id
    LIMIT 5
  `).all();

  console.log('\nSample questions and their test cases:');
  console.log('==================================================');

  for (const q of questions) {
    console.log(`\nQuestion ${q.id}: ${q.title}`);

    // Check test cases
    if (q.test_cases) {
      try {
        const testCases = JSON.parse(q.test_cases);
        console.log(`  ✓ Has ${testCases.length} visible test cases`);
      } catch (e) {
        console.log(`  ✗ Invalid test_cases JSON: ${q.test_cases.substring(0, 50)}...`);
      }
    } else {
      console.log('  ✗ No test cases');
    }

    // Check hidden test cases
    if (q.hidden_test_cases) {
      try {
        const hiddenTestCases = JSON.parse(q.hidden_test_cases);
        console.log(`  ✓ Has ${hiddenTestCases.length} hidden test cases`);
      } catch (e) {
        console.log(`  ✗ Invalid hidden_test_cases JSON: ${q.hidden_test_cases.substring(0, 50)}...`);
      }
    } else {
      console.log('  ✗ No hidden test cases');
    }

  }

  // Count total questions with/without test cases
  const stats = db.prepare(`
    SELECT
      COUNT(*) as total,
      SUM(CASE WHEN test_cases IS NOT NULL AND test_cases != '' THEN 1 ELSE 0 END) as with_test_cases,
      SUM(CASE WHEN hidden_test_cases IS NOT NULL AND hidden_test_cases != '' THEN 1 ELSE 0 END) as with_hidden_test_cases
    FROM leetcode_questions
  `).get();

  console.log('\n\nOverall Statistics:');
  console.log('==================================================');
  console.log(`Total LeetCode questions: ${stats.total}`);
  console.log(`Questions with test cases: ${stats.with_test_cases}`);
  console.log(`Questions with hidden test cases: ${stats.with_hidden_test_cases}`);

  db.close();

} catch (error) {
  console.error('Error checking database:', error);
  process.exit(1);
}

process.exit(0);