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

async function importSeedData() {
  try {
    const dbPath = getDatabasePath();
    console.log('Importing seed data to database at:', dbPath);

    const db = new Database(dbPath);
    db.pragma('journal_mode = WAL');

    // Read and execute seed data
    const seedPath = path.join(__dirname, '../database/seed_complete.sql');
    console.log('Reading seed file from:', seedPath);

    const seedData = fs.readFileSync(seedPath, 'utf-8');

    console.log('Seed file size:', (seedData.length / 1024).toFixed(2), 'KB');
    console.log('Executing SQL statements...');

    // Execute the seed data
    db.exec(seedData);

    // Verify data was imported
    const questionCount = db.prepare('SELECT COUNT(*) as count FROM questions').get();
    const leetcodeCount = db.prepare('SELECT COUNT(*) as count FROM leetcode_questions').get();
    const mlDesignCount = db.prepare('SELECT COUNT(*) as count FROM ml_design_questions').get();

    console.log('\n✓ Seed data imported successfully');
    console.log('  - Total questions:', questionCount.count);
    console.log('  - LeetCode questions:', leetcodeCount.count);
    console.log('  - ML Design questions:', mlDesignCount.count);

    // Check if ML design questions have sample solutions
    const mlWithSolutions = db.prepare(`
      SELECT COUNT(*) as count
      FROM ml_design_questions
      WHERE sample_solution IS NOT NULL AND sample_solution != ''
    `).get();

    console.log('  - ML Design questions with solutions:', mlWithSolutions.count);

    db.close();
  } catch (error) {
    console.error('Failed to import seed data:', error);
    process.exit(1);
  }
}

importSeedData();
