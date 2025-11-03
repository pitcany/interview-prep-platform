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

    // Read and execute seed data
    const seedPath = path.join(__dirname, '../database/seed_sample.sql');
    const seed = fs.readFileSync(seedPath, 'utf-8');
    
    db.exec(seed);
    
    console.log('✓ Database seeded successfully');
    console.log('  - 3 LeetCode questions added');
    console.log('  - 3 ML System Design questions added');
    
    db.close();
  } catch (error) {
    console.error('Failed to seed database:', error);
    process.exit(1);
  }
}

seedDatabase();
