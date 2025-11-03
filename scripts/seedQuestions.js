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

  return path.join(configDir, 'interview-prep.db');
}

async function seedDatabase() {
  try {
    const dbPath = getDatabasePath();
    console.log('Seeding database at:', dbPath);

    if (!fs.existsSync(dbPath)) {
      console.error('Database not found. Please run "npm run db:init" first.');
      process.exit(1);
    }

    const db = new Database(dbPath);
    db.pragma('foreign_keys = ON');

    const seedPath = path.join(__dirname, '../database/seed_complete.sql');
    const seed = fs.readFileSync(seedPath, 'utf-8');

    const clearSql = `
      DELETE FROM leetcode_questions WHERE question_id IN (
        SELECT id FROM questions WHERE category_id IN (1, 2)
      );
      DELETE FROM ml_design_questions WHERE question_id IN (
        SELECT id FROM questions WHERE category_id IN (1, 2)
      );
      DELETE FROM questions WHERE category_id IN (1, 2);
    `;

    db.exec(clearSql);
    db.exec(seed);
    
    console.log('✓ Database seeded successfully');
    console.log('  - 40 LeetCode questions loaded');
    console.log('  - 10 ML System Design questions loaded');
    
    db.close();
  } catch (error) {
    console.error('Failed to seed database:', error);
    process.exit(1);
  }
}

seedDatabase();
