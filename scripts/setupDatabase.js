#!/usr/bin/env node
/**
 * Database Setup Script
 *
 * This script:
 * 1. Initializes the database with the schema
 * 2. Seeds it with all question data (including ML design solutions)
 *
 * Usage: node scripts/setupDatabase.js
 */

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
    console.log('📦 Setting up database at:', dbPath);
    console.log('');

    // Check if database already exists
    const dbExists = fs.existsSync(dbPath);
    if (dbExists) {
      console.log('⚠️  Database already exists. This will overwrite existing data.');
      console.log('   Backing up existing database...');
      const backupPath = dbPath + '.backup.' + Date.now();
      fs.copyFileSync(dbPath, backupPath);
      console.log('   Backup created at:', backupPath);
      console.log('');
    }

    const db = new Database(dbPath);
    db.pragma('journal_mode = WAL');
    db.pragma('foreign_keys = ON');

    // Step 1: Initialize schema
    console.log('📋 Step 1: Initializing database schema...');
    const schemaPath = path.join(__dirname, '../database/schema.sql');
    const schema = fs.readFileSync(schemaPath, 'utf-8');
    db.exec(schema);
    console.log('   ✓ Schema initialized');
    console.log('');

    // Step 2: Import seed data
    console.log('📥 Step 2: Importing question data...');
    const seedPath = path.join(__dirname, '../database/seed_complete.sql');
    console.log('   Reading seed file:', seedPath);

    const seedData = fs.readFileSync(seedPath, 'utf-8');
    console.log('   Seed file size:', (seedData.length / 1024).toFixed(2), 'KB');
    console.log('   Executing SQL statements... (this may take a moment)');

    db.exec(seedData);
    console.log('   ✓ Seed data imported');
    console.log('');

    // Step 3: Verify data was imported correctly
    console.log('✅ Step 3: Verifying data import...');

    const questionCount = db.prepare('SELECT COUNT(*) as count FROM questions').get();
    const leetcodeCount = db.prepare('SELECT COUNT(*) as count FROM leetcode_questions').get();
    const mlDesignCount = db.prepare('SELECT COUNT(*) as count FROM ml_design_questions').get();

    console.log('   - Total questions:', questionCount.count);
    console.log('   - LeetCode questions:', leetcodeCount.count);
    console.log('   - ML Design questions:', mlDesignCount.count);

    // Check ML design questions with solutions
    const mlWithSolutions = db.prepare(`
      SELECT COUNT(*) as count
      FROM ml_design_questions
      WHERE sample_solution IS NOT NULL AND sample_solution != ''
    `).get();

    console.log('   - ML Design questions with solutions:', mlWithSolutions.count);

    // Show sample solution lengths
    const solutionLengths = db.prepare(`
      SELECT
        q.title,
        LENGTH(ml.sample_solution) as solution_length
      FROM ml_design_questions ml
      JOIN questions q ON ml.question_id = q.id
      WHERE ml.sample_solution IS NOT NULL AND ml.sample_solution != ''
      ORDER BY ml.question_id
      LIMIT 5
    `).all();

    if (solutionLengths.length > 0) {
      console.log('');
      console.log('   Sample solution lengths (first 5):');
      solutionLengths.forEach(s => {
        const lengthKB = (s.solution_length / 1024).toFixed(2);
        console.log(`   - ${s.title}: ${s.solution_length} chars (${lengthKB} KB)`);
      });
    }

    db.close();

    console.log('');
    console.log('🎉 Database setup complete!');
    console.log('');
    console.log('You can now run the application with: npm run dev');
    console.log('');

  } catch (error) {
    console.error('❌ Failed to set up database:', error);
    console.error('');
    console.error('Error details:', error.message);
    console.error('');
    console.error('Please ensure:');
    console.error('  1. You have run "npm install" to install dependencies');
    console.error('  2. The database/seed_complete.sql file exists');
    console.error('  3. You have write permissions to the database directory');
    console.error('');
    process.exit(1);
  }
}

setupDatabase();
