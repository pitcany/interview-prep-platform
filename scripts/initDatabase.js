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

async function initializeDatabase() {
  try {
    const dbPath = getDatabasePath();
    console.log('Initializing database at:', dbPath);

    const db = new Database(dbPath);
    db.pragma('journal_mode = WAL');

    // Read and execute schema
    const schemaPath = path.join(__dirname, '../database/schema.sql');
    const schema = fs.readFileSync(schemaPath, 'utf-8');
    
    db.exec(schema);
    
    console.log('✓ Database schema initialized successfully');
    
    db.close();
  } catch (error) {
    console.error('Failed to initialize database:', error);
    process.exit(1);
  }
}

initializeDatabase();
