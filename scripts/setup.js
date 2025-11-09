const Database = require('better-sqlite3');
const fs = require('fs');
const path = require('path');
const os = require('os');

// Determine database location based on platform
function getDatabasePath() {
  const appName = 'interview-prep-platform';
  let configDir;

  if (process.platform === 'win32') {
    configDir = path.join(process.env.APPDATA || '', appName);
  } else if (process.platform === 'darwin') {
    configDir = path.join(os.homedir(), 'Library', 'Application Support', appName);
  } else {
    configDir = path.join(os.homedir(), '.config', appName);
  }

  if (!fs.existsSync(configDir)) {
    fs.mkdirSync(configDir, { recursive: true });
  }

  return path.join(configDir, 'interview-prep.db');
}

async function setupDatabase() {
  try {
    const dbPath = getDatabasePath();
    console.log('Setting up database at:', dbPath);
    console.log('Platform:', process.platform);
    console.log('');

    // Step 1: Initialize database schema
    console.log('Step 1: Initializing database schema...');
    const db = new Database(dbPath);
    db.pragma('journal_mode = WAL');

    const schemaPath = path.join(__dirname, '../database/schema.sql');
    const schema = fs.readFileSync(schemaPath, 'utf-8');
    db.exec(schema);
    console.log('✓ Database schema initialized');

    // Step 2: Import questions
    console.log('\nStep 2: Importing interview questions...');
    const seedPath = path.join(__dirname, '../database/seed_complete.sql');
    const seedData = fs.readFileSync(seedPath, 'utf-8');
    db.exec(seedData);
    console.log('✓ Questions imported successfully');

    // Step 3: Verify data
    console.log('\nStep 3: Verifying data...');
    const totalQuestions = db.prepare('SELECT COUNT(*) as count FROM questions').get();
    const leetcodeQuestions = db.prepare('SELECT COUNT(*) as count FROM leetcode_questions').get();
    const mlDesignQuestions = db.prepare('SELECT COUNT(*) as count FROM ml_design_questions').get();

    console.log(`✓ Total questions: ${totalQuestions.count}`);
    console.log(`  - LeetCode: ${leetcodeQuestions.count}`);
    console.log(`  - ML System Design: ${mlDesignQuestions.count}`);

    db.close();

    console.log('\n✅ Database setup complete!');
    console.log('\nYou can now run: npm start');
  } catch (error) {
    console.error('\n❌ Failed to setup database:', error.message);
    process.exit(1);
  }
}

setupDatabase();
