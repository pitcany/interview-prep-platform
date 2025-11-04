# Documentation Index

This directory contains comprehensive documentation about the Interview Prep Platform's test case implementation.

## Documents

### 1. **TEST_CASES_ANALYSIS.md** (24 KB)
**The Complete Reference Guide**

19 comprehensive sections covering:
- Database schema and data structures
- Questions data source and format
- SQL generation pipeline
- Frontend test case flow
- Code execution architecture
- Python execution service (test_runner, executor, sandbox)
- TypeScript type definitions
- Database service methods
- IPC communication patterns
- Flow diagrams and examples
- Test case output comparison
- Known limitations and edge cases
- End-to-end examples
- How to add hidden test cases

**Start here for**: Complete understanding of test case implementation

### 2. **KEY_FILES_REFERENCE.md** (9.3 KB)
**Quick Reference and Navigation**

6 sections providing:
- Critical file locations and their responsibilities
- File dependencies and module imports
- Critical code paths with ASCII flow diagrams
- Important constants and settings
- Test case data format examples
- Environment variables
- How to add/modify hidden test cases
- Debugging tips

**Start here for**: Finding specific files and understanding interactions

## Quick Navigation

### I need to understand...

**How test cases are stored**
→ TEST_CASES_ANALYSIS.md, Section 1-3

**How test cases are loaded**
→ TEST_CASES_ANALYSIS.md, Section 4-5

**How code is executed**
→ TEST_CASES_ANALYSIS.md, Section 6-7

**How visible vs hidden tests are used**
→ TEST_CASES_ANALYSIS.md, Section 4 (Test Case Flow)

**Type hints and imports**
→ TEST_CASES_ANALYSIS.md, Section 13

**Method name extraction**
→ TEST_CASES_ANALYSIS.md, Section 6 & 7

**How to activate hidden test cases**
→ TEST_CASES_ANALYSIS.md, Section 15

**Which files to modify**
→ KEY_FILES_REFERENCE.md, "Questions Data" section

**How the system works end-to-end**
→ TEST_CASES_ANALYSIS.md, Section 16 (Flow Diagrams) & Section 19 (Examples)

## Key Findings Summary

✅ **Working Perfectly**
- Database schema with hidden_test_cases column
- Frontend test case loading and parsing
- Python code execution with method introspection
- Test result comparison and storage
- Submission tracking and progress updates

❌ **Not Yet Implemented**
- Hidden test cases not populated in questions_data_full.py
- Java/C++ execution (Docker only)
- Type hints auto-importing

⚠️ **Edge Cases**
- Type hints must be imported by user code
- Method extraction uses regex + introspection
- All-or-nothing scoring (no partial credit)

## Critical Files Locations

```
/database/schema.sql                    - Database schema
/scripts/questions_data_full.py         - SOURCE OF TRUTH for test cases
/scripts/generate_seed_sql.py           - Converts Python to SQL
/electron/main.ts                       - IPC handlers (code:execute, code:submit)
/electron/services/codeExecutor.ts     - Code execution orchestration
/python-service/test_runner.py         - Main test runner
/src/pages/Practice.tsx                - Frontend test case logic
/src/components/TestRunner/index.tsx   - Display test results
```

## Getting Started

### For Understanding the System
1. Read: TEST_CASES_ANALYSIS.md sections 1-5
2. Review: Flow diagrams in section 16
3. Study: Examples in section 19

### For Modifying Code
1. Find the file in: KEY_FILES_REFERENCE.md
2. Check: File dependencies section
3. Reference: Critical code paths section

### For Debugging
1. Use: Debugging tips in KEY_FILES_REFERENCE.md
2. Check: Known limitations in TEST_CASES_ANALYSIS.md
3. Find: Environment variables in KEY_FILES_REFERENCE.md

### For Adding Hidden Test Cases
1. Follow: TEST_CASES_ANALYSIS.md section 15
2. Or use: KEY_FILES_REFERENCE.md "How to Add/Modify" section
3. Verify: By checking database query examples

## Document Maintenance

These documents are auto-generated from thorough code analysis and represent
the complete state of test case implementation as of the latest exploration.

- **Last Updated**: November 4, 2025
- **Coverage**: Complete (all test case related code)
- **Accuracy**: High (based on actual code analysis)

## How the Platform Works (30-second summary)

1. Questions with test cases are stored in `questions_data_full.py` (Python source)
2. A script (`generate_seed_sql.py`) converts them to SQL
3. SQL is imported into SQLite database
4. Frontend loads questions and shows visible test cases
5. When user clicks "Run Code": only visible tests run
6. When user clicks "Submit": visible + hidden tests run
7. Python code is executed with method introspection
8. Results are compared (exact JSON match)
9. Submission is saved with all test results
10. User progress is updated

The system is ready for hidden test cases - just needs the data!

---

For more details, see the individual documentation files above.
