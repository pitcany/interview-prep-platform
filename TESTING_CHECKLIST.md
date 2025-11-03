# UI Testing Checklist

Use this checklist to verify everything works correctly.

## Pre-Testing Setup

- [ ] Docker is running (`docker ps` works)
- [ ] Containers are built
  ```bash
  docker images | grep interview-prep
  # Should show: interview-prep-python, interview-prep-java, interview-prep-cpp
  ```
- [ ] Database is initialized (`npm run db:init`)
- [ ] Sample questions are loaded (`npm run db:seed`)
- [ ] Claude API key is set in `.env` (optional for testing)

## Practice Page Testing

### Question List
- [ ] Question list loads on page load
- [ ] All 3 sample questions are visible
- [ ] Filter buttons work (All, Easy, Medium, Hard)
- [ ] Question count updates when filtering
- [ ] Tags display correctly under each question
- [ ] Difficulty badges show correct colors
- [ ] Clicking a question selects it (blue highlight)
- [ ] Selected question loads in main area

### Question Description
- [ ] Question title displays
- [ ] Difficulty badge shows
- [ ] Tags render below title
- [ ] Description text is readable
- [ ] Examples section shows
- [ ] Input/Output formatted correctly
- [ ] Constraints section displays
- [ ] "Hide Description" button works
- [ ] Can toggle description on/off

### Code Editor
- [ ] Monaco editor loads correctly
- [ ] Syntax highlighting works
- [ ] Language selector shows (Python, Java, C++)
- [ ] Switching languages updates code template
- [ ] Can type and edit code
- [ ] Line numbers display
- [ ] Keyboard shortcut hint shows (bottom right)
- [ ] Run button is enabled
- [ ] Submit button is enabled

### Language Switching
- [ ] Python: Shows correct function signature
- [ ] Java: Shows correct class structure  
- [ ] C++: Shows correct class/function
- [ ] Code persists when switching back to same language
- [ ] Template loads immediately on switch

### Code Execution (Run)
- [ ] Click "Run" button
- [ ] Button shows "Running..." state
- [ ] Test results appear in bottom panel
- [ ] Loading spinner shows while running
- [ ] Results display after execution

### Test Results Display
- [ ] Summary shows (X/Y tests passed)
- [ ] Overall status displays (PASSED/FAILED)
- [ ] Execution time shows
- [ ] Individual test cases listed
- [ ] Can click to expand test details
- [ ] Expanded test shows:
  - [ ] Input
  - [ ] Expected output
  - [ ] Actual output
  - [ ] Pass/fail icon
- [ ] Colors match status (green=pass, red=fail)

### Code Submission
- [ ] Click "Submit" button
- [ ] Runs all tests
- [ ] Saves to database
- [ ] Shows success message
- [ ] Can view in Progress page

### Keyboard Shortcuts
- [ ] Ctrl/Cmd + Enter runs code
- [ ] Works from any cursor position
- [ ] Doesn't run when already running

### Error Handling
- [ ] Invalid code shows error message
- [ ] Compilation errors display clearly
- [ ] Timeout errors show
- [ ] Network errors are caught
- [ ] Docker errors are handled

## Progress Page Testing

### Stats Cards
- [ ] Total Attempts shows correct number
- [ ] Problems Solved displays
- [ ] Success Rate calculates correctly
- [ ] Time Spent shows in minutes
- [ ] Icons render correctly
- [ ] Numbers update after submission

### Tabs
- [ ] Three tabs display (Overview, Submissions, Feedback)
- [ ] Active tab highlighted in blue
- [ ] Can switch between tabs
- [ ] Content changes per tab

### Overview Tab

**Performance by Difficulty Chart:**
- [ ] Bar chart renders
- [ ] Shows Easy, Medium, Hard
- [ ] Two bars per difficulty (Solved, Attempted)
- [ ] Colors are distinct
- [ ] Hover shows tooltip
- [ ] Data is accurate

**Problems by Category Chart:**
- [ ] Pie chart renders
- [ ] Shows LeetCode and ML Design
- [ ] Correct proportions
- [ ] Labels display
- [ ] Colors match theme

**Success Rate Line Chart:**
- [ ] Line chart renders
- [ ] Shows success rate by difficulty
- [ ] Line is smooth
- [ ] Y-axis shows percentage
- [ ] Data points visible

### Submissions Tab
- [ ] Shows "Recent Activity" header
- [ ] Lists recent attempts
- [ ] Each item shows:
  - [ ] Question title
  - [ ] Category icon
  - [ ] Difficulty badge
  - [ ] Attempt count
  - [ ] Status (solved/not solved)
  - [ ] Date
- [ ] Items sorted by date (newest first)
- [ ] Empty state shows if no data

### Feedback Tab
- [ ] Shows "AI Feedback History" header
- [ ] Lists feedback items
- [ ] Each feedback shows:
  - [ ] Question title
  - [ ] Date/time
  - [ ] Score breakdown
  - [ ] Strengths section
  - [ ] Improvements section
- [ ] Scores display as X/10
- [ ] Lists are readable
- [ ] Empty state shows if no feedback

### Empty States
- [ ] "No submissions yet" shows when appropriate
- [ ] "No feedback yet" shows when appropriate
- [ ] Helpful messages included

## Integration Testing

### Full User Flow
- [ ] Create new user
- [ ] Go to Practice page
- [ ] Select a question
- [ ] Write solution
- [ ] Run tests
- [ ] See results
- [ ] Submit solution
- [ ] Go to Progress page
- [ ] See updated stats
- [ ] View submission in history

### Multi-Question Flow
- [ ] Solve first question
- [ ] Check stats update
- [ ] Select second question
- [ ] Previous code doesn't carry over
- [ ] Solve second question
- [ ] Stats update again
- [ ] Both show in history

## Visual Polish Checks

### Responsiveness
- [ ] Works on wide screen (1920px+)
- [ ] Works on standard screen (1440px)
- [ ] Works on laptop screen (1280px)
- [ ] Sidebar doesn't overflow
- [ ] Charts resize properly

### Dark Theme
- [ ] Background is dark gray (#111827)
- [ ] Text is readable
- [ ] Contrast is good
- [ ] Code editor dark theme works
- [ ] Charts use appropriate colors

### Animations
- [ ] Smooth transitions between states
- [ ] Loading spinner spins
- [ ] Hover effects work
- [ ] Button states clear

### Typography
- [ ] Headers are bold and clear
- [ ] Body text is readable
- [ ] Code uses monospace font
- [ ] Sizes are appropriate

## Performance Checks

- [ ] Page loads quickly (<1s)
- [ ] No lag when typing code
- [ ] Charts render smoothly
- [ ] Switching tabs is instant
- [ ] Question selection is quick
- [ ] No memory leaks (check DevTools)

## Browser Console

Open browser console (F12) and check:
- [ ] No errors in console
- [ ] No warnings (or only expected ones)
- [ ] Network requests succeed
- [ ] No 404s or failed requests

## Database Verification

After testing, check database:
```bash
# Location varies by OS
sqlite3 ~/.config/interview-prep-platform/interview-prep.db

# Run queries
SELECT COUNT(*) FROM code_submissions;
SELECT COUNT(*) FROM user_progress;
SELECT * FROM users;
```

## Known Limitations

These are expected and OK:
- Docker execution requires Docker running
- AI feedback requires API key
- Only 3 sample questions included
- Some features marked TODO

## Report Issues

If you find any issues:
1. Check browser console for errors
2. Check terminal for backend errors
3. Verify Docker is running
4. Check database was initialized
5. Note the steps to reproduce

## Success Criteria

The implementation is successful if:
- ✅ Can browse and select questions
- ✅ Can write and edit code
- ✅ Code execution works (with Docker)
- ✅ Test results display correctly
- ✅ Progress page shows accurate stats
- ✅ Charts render properly
- ✅ No critical errors in console
- ✅ User flow is smooth

---

## Quick Test Script

Run through this 5-minute test:

1. **Start app** → Create user → See dashboard ✓
2. **Practice** → Click LeetCode Practice ✓
3. **Question** → Select "Two Sum" ✓
4. **Code** → Switch to Python → Type simple code ✓
5. **Run** → Click Run → See results ✓
6. **Submit** → Click Submit → Confirm saved ✓
7. **Progress** → Go to Progress page ✓
8. **Stats** → See 1 attempt, 1 solved (or not) ✓
9. **Charts** → Verify charts render ✓
10. **History** → See submission in list ✓

If all 10 steps work: **You're good to go!** 🎉
