# ML Design Solutions Not Displaying - Issue Analysis & Fix

## Issue Description

ML System Design questions are not showing their full solutions when users click "View Solution" in the Practice page.

## Root Cause

The issue occurs when the database has not been properly initialized and seeded with the complete question data. The `ml_design_questions` table needs to be populated with `sample_solution` values, which contain comprehensive system design examples.

## Investigation Summary

### Data Flow Verification

I verified the complete data flow from source to display:

1. ✅ **Source Data** (`scripts/questions_data_full.py`): ML questions DO contain `sample_solution` field with 2-3KB of content per question
2. ✅ **SQL Generation** (`scripts/generate_seed_sql.py`): Script correctly includes `sample_solution` in INSERT statements
3. ✅ **Seed File** (`database/seed_complete.sql`): Generated SQL file contains full solution text (verified ~260KB file)
4. ✅ **Database Schema** (`database/schema.sql`): Table has `sample_solution TEXT` column
5. ✅ **Database Service** (`electron/services/database.ts:203`): Method fetches and returns `sample_solution`
6. ✅ **IPC Layer** (`electron/main.ts:184-186`): Properly exposes ML design details via IPC
7. ✅ **Preload Bridge** (`electron/preload.ts:21-22`): Correctly bridges to renderer process
8. ✅ **Frontend API** (`src/services/api.ts:69-71`): Correctly calls the IPC method
9. ✅ **React Component** (`src/pages/Practice.tsx:605-608`): Passes `sample_solution` to SolutionViewer
10. ✅ **UI Component** (`src/components/SolutionViewer.tsx:214-264`): Renders solution with markdown support

**All code is correct.** The issue is environmental - the database hasn't been seeded.

## Solution

### Option 1: Automated Setup (Recommended)

Run the new comprehensive setup script that handles both initialization and seeding:

```bash
# Install dependencies (if not already done)
npm install

# Run the complete database setup
npm run db:setup
```

This script:
- Creates the database directory if it doesn't exist
- Backs up existing database (if any)
- Initializes the schema
- Imports all 50 questions with solutions
- Verifies data integrity
- Reports statistics on imported data

### Option 2: Manual Setup

If you prefer the manual approach:

```bash
# 1. Install dependencies
npm install

# 2. Initialize database schema
npm run db:init

# 3. Import seed data (requires sqlite3 CLI)
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql

# Note: Database path varies by platform:
# - Linux: ~/.config/interview-prep-platform/interview-prep.db
# - macOS: ~/Library/Application Support/interview-prep-platform/interview-prep.db
# - Windows: %APPDATA%\interview-prep-platform\interview-prep.db
```

### Option 3: Using the Import Script

If you don't have sqlite3 CLI installed:

```bash
npm install
node scripts/importSeedData.js
```

## Verification

After running the setup, verify the data was imported correctly:

```bash
node -e "const Database = require('better-sqlite3'); const db = new Database(require('os').homedir() + '/.config/interview-prep-platform/interview-prep.db'); console.log('ML Design questions:', db.prepare('SELECT COUNT(*) as count FROM ml_design_questions').get()); console.log('With solutions:', db.prepare('SELECT COUNT(*) as count FROM ml_design_questions WHERE sample_solution IS NOT NULL AND sample_solution != \\\"\\\"').get());"
```

Expected output:
```
ML Design questions: { count: 10 }
With solutions: { count: 10 }
```

## Example Solution Content

Each ML design question includes a comprehensive sample solution with:

- System architecture diagrams (in markdown)
- Python code examples for key components
- Detailed explanations of:
  - Data collection pipelines
  - Feature engineering approaches
  - Model architectures
  - Serving infrastructure
  - Monitoring and evaluation
  - Scalability considerations

Example from "Facebook News Feed Ranking System":
- ~2.6KB of content
- Multiple code blocks
- Architecture sections
- Best practices

## Files Modified

### New Files Created

1. **scripts/setupDatabase.js** - Comprehensive database setup script
   - Combines initialization and seeding
   - Provides detailed logging
   - Verifies data integrity
   - Backs up existing data

2. **scripts/importSeedData.js** - Alternative import script
   - For environments without sqlite3 CLI
   - Imports seed_complete.sql using better-sqlite3

3. **ML_DESIGN_SOLUTIONS_FIX.md** - This documentation

### Modified Files

1. **package.json** - Added `db:setup` npm script for convenience

## Technical Details

### Database Schema

```sql
CREATE TABLE ml_design_questions (
    question_id INTEGER PRIMARY KEY,
    scenario TEXT NOT NULL,
    requirements TEXT NOT NULL,
    evaluation_criteria TEXT NOT NULL,
    sample_solution TEXT,  -- This field contains the solutions
    key_components TEXT,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);
```

### Solution Format

Solutions are stored as markdown text with embedded code blocks:

```markdown
# System Name

## System Architecture

### 1. Component Name
```python
class ComponentClass:
    def method(self):
        # Implementation
```

### 2. Next Component
...
```

The SolutionViewer component (`src/components/SolutionViewer.tsx`) automatically:
- Parses markdown code blocks (delimited by \`\`\`)
- Renders code with syntax highlighting
- Formats markdown headers, lists, and text

## Related Files Reference

- **Question Source**: `scripts/questions_data_full.py` (single source of truth)
- **SQL Generator**: `scripts/generate_seed_sql.py`
- **Seed Output**: `database/seed_complete.sql` (260KB, auto-generated)
- **Database Service**: `electron/services/database.ts:182-205` (getMLDesignQuestionDetails)
- **UI Component**: `src/components/SolutionViewer.tsx:214-264` (ML design rendering)
- **Practice Page**: `src/pages/Practice.tsx:605-608` (passes data to viewer)

## Troubleshooting

### Issue: "npm run db:setup" fails with module errors

**Solution**: Run `npm install` first to ensure all dependencies are installed.

### Issue: Permission denied writing to database directory

**Solution**: Ensure you have write permissions to the config directory:
```bash
mkdir -p ~/.config/interview-prep-platform
chmod 755 ~/.config/interview-prep-platform
```

### Issue: Solutions still not showing after setup

**Solution**: Check the browser console for errors:
1. Start the app: `npm run dev`
2. Open DevTools (Cmd+Option+I or F12)
3. Navigate to an ML design question
4. Check for errors when clicking "View Solution"

### Issue: Database file not found

**Solution**: The database is created in platform-specific locations. Verify:
```bash
# Linux
ls -l ~/.config/interview-prep-platform/interview-prep.db

# macOS
ls -l ~/Library/Application\ Support/interview-prep-platform/interview-prep.db
```

## Additional Notes

- The seed file (`seed_complete.sql`) is auto-generated from `questions_data_full.py`
- Never manually edit `seed_complete.sql` - regenerate it instead
- To modify questions: Edit `questions_data_full.py`, then run `python3 scripts/generate_seed_sql.py`
- All 10 ML design questions have sample solutions (each 1-3KB of content)
- Solutions include code examples in Python
- The SolutionViewer supports markdown with syntax highlighting

## Prevention

To avoid this issue in the future:

1. **After cloning the repo**: Always run `npm install && npm run db:setup`
2. **In documentation**: Update README.md setup instructions to include `db:setup`
3. **In CI/CD**: Add database setup to automated testing pipelines
4. **For new developers**: Include database setup in onboarding checklist

## Contact

If issues persist after following this guide, check:
- GitHub Issues for similar problems
- CLAUDE.md for project-specific guidance
- Database schema in `database/schema.sql`
