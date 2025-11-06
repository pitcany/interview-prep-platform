const Database = require('better-sqlite3');
const path = require('path');
const os = require('os');

// Get database path
const userDataPath = process.env.NODE_ENV === 'production'
  ? path.join(os.homedir(), '.config', 'interview-prep-platform')
  : path.join(os.homedir(), '.config', 'interview-prep-platform');

const dbPath = path.join(userDataPath, 'interview-prep.db');

console.log(`Checking database at: ${dbPath}\n`);

const db = new Database(dbPath);

// Check for orphaned code_submissions
console.log('=== Checking for orphaned code_submissions ===');
const orphanedCodeSubmissions = db.prepare(`
  SELECT cs.id, cs.question_id, cs.user_id, cs.submitted_at
  FROM code_submissions cs
  LEFT JOIN questions q ON cs.question_id = q.id
  WHERE q.id IS NULL
`).all();

if (orphanedCodeSubmissions.length > 0) {
  console.log(`Found ${orphanedCodeSubmissions.length} orphaned code_submissions:`);
  orphanedCodeSubmissions.forEach(row => {
    console.log(`  - Submission ID: ${row.id}, Question ID: ${row.question_id}, User ID: ${row.user_id}, Submitted: ${row.submitted_at}`);
  });
} else {
  console.log('✓ No orphaned code_submissions found');
}

// Check for orphaned design_submissions
console.log('\n=== Checking for orphaned design_submissions ===');
const orphanedDesignSubmissions = db.prepare(`
  SELECT ds.id, ds.question_id, ds.user_id, ds.submitted_at
  FROM design_submissions ds
  LEFT JOIN questions q ON ds.question_id = q.id
  WHERE q.id IS NULL
`).all();

if (orphanedDesignSubmissions.length > 0) {
  console.log(`Found ${orphanedDesignSubmissions.length} orphaned design_submissions:`);
  orphanedDesignSubmissions.forEach(row => {
    console.log(`  - Submission ID: ${row.id}, Question ID: ${row.question_id}, User ID: ${row.user_id}, Submitted: ${row.submitted_at}`);
  });
} else {
  console.log('✓ No orphaned design_submissions found');
}

// Check for orphaned feedback records
console.log('\n=== Checking for orphaned feedback records ===');
const orphanedFeedback = db.prepare(`
  SELECT f.id, f.submission_type, f.submission_id, f.generated_at
  FROM feedback f
  LEFT JOIN code_submissions cs ON f.submission_type = 'code' AND f.submission_id = cs.id
  LEFT JOIN design_submissions ds ON f.submission_type = 'design' AND f.submission_id = ds.id
  WHERE cs.id IS NULL AND ds.id IS NULL
`).all();

if (orphanedFeedback.length > 0) {
  console.log(`Found ${orphanedFeedback.length} orphaned feedback records:`);
  orphanedFeedback.forEach(row => {
    console.log(`  - Feedback ID: ${row.id}, Type: ${row.submission_type}, Submission ID: ${row.submission_id}, Generated: ${row.generated_at}`);
  });
} else {
  console.log('✓ No orphaned feedback records found');
}

// Check for code_submissions referencing questions without leetcode_questions details
console.log('\n=== Checking for code_submissions without leetcode_questions details ===');
const submissionsWithoutDetails = db.prepare(`
  SELECT cs.id, cs.question_id, q.title, cs.submitted_at
  FROM code_submissions cs
  JOIN questions q ON cs.question_id = q.id
  LEFT JOIN leetcode_questions lq ON cs.question_id = lq.question_id
  WHERE lq.question_id IS NULL
`).all();

if (submissionsWithoutDetails.length > 0) {
  console.log(`Found ${submissionsWithoutDetails.length} code_submissions referencing questions without leetcode_questions details:`);
  submissionsWithoutDetails.forEach(row => {
    console.log(`  - Submission ID: ${row.id}, Question ID: ${row.question_id}, Title: ${row.title}, Submitted: ${row.submitted_at}`);
  });
} else {
  console.log('✓ All code_submissions have corresponding leetcode_questions details');
}

// Summary statistics
console.log('\n=== Summary ===');
const totalCodeSubmissions = db.prepare('SELECT COUNT(*) as count FROM code_submissions').get();
const totalDesignSubmissions = db.prepare('SELECT COUNT(*) as count FROM design_submissions').get();
const totalFeedback = db.prepare('SELECT COUNT(*) as count FROM feedback').get();
const totalQuestions = db.prepare('SELECT COUNT(*) as count FROM questions').get();

console.log(`Total questions: ${totalQuestions.count}`);
console.log(`Total code_submissions: ${totalCodeSubmissions.count}`);
console.log(`Total design_submissions: ${totalDesignSubmissions.count}`);
console.log(`Total feedback records: ${totalFeedback.count}`);

db.close();
