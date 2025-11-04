#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const Database = require('better-sqlite3');
const os = require('os');

// Get the database path (same as Electron uses)
const dbPath = path.join(
  os.homedir(),
  '.config',
  'interview-prep-platform',
  'interview-prep.db'
);

console.log('Importing seed data into database at:', dbPath);

try {
  // Read the SQL file
  const sqlContent = fs.readFileSync(
    path.join(__dirname, '..', 'database', 'seed_complete.sql'),
    'utf8'
  );

  // Connect to the database
  const db = new Database(dbPath);

  // Split SQL content by semicolons and execute each statement
  const statements = sqlContent
    .split(';')
    .map(s => s.trim())
    .filter(s => s.length > 0 && !s.startsWith('--'));

  // Begin transaction
  db.exec('BEGIN TRANSACTION');

  let successCount = 0;
  let errorCount = 0;

  for (const statement of statements) {
    try {
      db.exec(statement);
      successCount++;
    } catch (error) {
      console.error('Error executing statement:', error.message);
      console.error('Statement:', statement.substring(0, 100) + '...');
      errorCount++;
    }
  }

  // Commit transaction
  db.exec('COMMIT');

  console.log(`Successfully imported ${successCount} statements`);
  if (errorCount > 0) {
    console.log(`Failed to execute ${errorCount} statements`);
  }

  // Verify some data was imported
  const questionCount = db.prepare('SELECT COUNT(*) as count FROM questions').get();
  console.log(`Total questions in database: ${questionCount.count}`);

  const leetcodeCount = db.prepare('SELECT COUNT(*) as count FROM leetcode_questions').get();
  console.log(`Total LeetCode questions: ${leetcodeCount.count}`);

  db.close();
  console.log('Database seeding completed successfully!');
  process.exit(0);

} catch (error) {
  console.error('Failed to import seed data:', error);
  process.exit(1);
}