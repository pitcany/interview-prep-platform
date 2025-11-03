# UI Visual Guide

This document describes what each page looks like visually.

## Overall Layout

### Color Scheme
- **Background:** Dark gray (#111827, #1F2937)
- **Cards/Panels:** Medium gray (#1F2937, #374151)
- **Borders:** Light gray (#374151, #4B5563)
- **Text:** White (#FFFFFF) and gray (#9CA3AF, #6B7280)
- **Accents:**
  - Blue (#3B82F6) - Primary actions, links
  - Green (#10B981) - Success, "easy" difficulty
  - Yellow (#F59E0B) - Warning, "medium" difficulty
  - Red (#EF4444) - Error, "hard" difficulty
  - Purple (#8B5CF6) - ML Design category

## Login Page

```
┌─────────────────────────────────────────────┐
│                                             │
│         Interview Prep Platform             │
│     LeetCode & ML System Design Practice    │
│                                             │
│     ┌───────────────────────────────┐      │
│     │   Select User                 │      │
│     │   [Choose a user...        ▼] │      │
│     └───────────────────────────────┘      │
│                                             │
│     ┌───────────────────────────────┐      │
│     │         [Login]               │      │
│     └───────────────────────────────┘      │
│                                             │
│              ─── Or ───                     │
│                                             │
│     ┌───────────────────────────────┐      │
│     │    [Create New User]          │      │
│     └───────────────────────────────┘      │
│                                             │
└─────────────────────────────────────────────┘
```

## Dashboard

```
┌──────────┬─────────────────────────────────────────────────┐
│          │  Welcome back, username!                        │
│  Sidebar │  Ready to level up your interview skills?      │
│          │                                                 │
│ [🏠 Dash │  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐     │
│  Practice│  │   42  │ │   31  │ │  74%  │ │ 180m  │     │
│  Mock    │  │ Total │ │Solved │ │Success│ │ Time  │     │
│  Progress│  └───────┘ └───────┘ └───────┘ └───────┘     │
│          │                                                 │
│  ────────│  Quick Actions                                 │
│          │  ┌─────────────┐ ┌─────────────┐ ┌──────────┐│
│  @user   │  │  💻 LeetCode│ │  🧠 ML      │ │  ⏱️ Mock ││
│  Logout  │  │   Practice  │ │   Design    │ │ Interview││
│          │  └─────────────┘ └─────────────┘ └──────────┘│
│          │                                                 │
│          │  Recent Feedback                               │
│          │  ┌──────────────────────────────────────────┐ │
│          │  │ Two Sum                   Oct 28         │ │
│          │  │ correctness: 8  efficiency: 7            │ │
│          │  │ Good use of hash table...                │ │
│          │  └──────────────────────────────────────────┘ │
└──────────┴─────────────────────────────────────────────────┘
```

## Practice Page - LeetCode

```
┌──────────────────────────────────────────────────────────────────────┐
│ ← 💻 LeetCode Practice / Two Sum                                     │
├──────────┬──────────────────┬────────────────────────────────────────┤
│          │                  │                                        │
│ Question │  Two Sum         │  [Python] [Java] [C++]     [Run] [Submit]│
│  List    │  Easy   array... │  ────────────────────────────────────  │
│          │                  │                                        │
│ [All]... │  Given an array  │  def twoSum(self, nums, target):      │
│          │  of integers...  │      # Your code here                 │
│ • Two Sum│                  │      pass                             │
│   Easy   │  Example 1:      │                                        │
│   [array]│  Input: [2,7...]  │                                        │
│          │  Output: [0,1]   │  (Monaco Editor continues here...)    │
│ • String │                  │                                        │
│   Medium │  Constraints:    │                                        │
│   [str]  │  • 2 <= len...   │                                        │
│          │                  │                                        │
│ • Water  │  [Hint 1 ▶]     │────────────────────────────────────────│
│   Medium │                  │  Test Results                         │
│          │                  │  ✅ All Tests Passed! (3/3)           │
│          │                  │  Execution time: 42ms                 │
│          │                  │  ─────────────────────────────────    │
│          │                  │  ✓ Test Case 1        12ms           │
│          │                  │  ✓ Test Case 2        15ms           │
│          │                  │  ✓ Test Case 3        15ms           │
└──────────┴──────────────────┴────────────────────────────────────────┘
```

### Practice Page - Key Features

**Left Panel (Questions):**
- Filter buttons at top (All, Easy, Medium, Hard)
- Scrollable list of questions
- Each question card shows:
  - Circle icon (status)
  - Title
  - Difficulty badge (colored)
  - Tags below

**Middle Panel (Description):**
- Question title and difficulty
- Tags
- Full problem description
- Examples with input/output
- Constraints list
- Collapsible hints
- "Hide" button to maximize code space

**Right Panel (Editor + Results):**
- Top half: Code editor
  - Language selector
  - Run and Submit buttons
  - Monaco editor with syntax highlighting
  - Keyboard shortcut hint
- Bottom half: Test results
  - Summary (passed/failed count)
  - Individual test cases
  - Expandable to see details
  - Input/output comparison

## Progress Page

```
┌─────────────────────────────────────────────────────────────────────┐
│  Your Progress                                                      │
│  Track your performance and improvement over time                   │
│                                                                     │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐                         │
│  │   42  │ │   31  │ │  74%  │ │ 180m  │                         │
│  │ Total │ │Solved │ │Success│ │ Time  │                         │
│  └───────┘ └───────┘ └───────┘ └───────┘                         │
│                                                                     │
│  [Overview] [Submissions] [Feedback]                               │
│  ─────────────────────────────────────────────────────────────     │
│                                                                     │
│  ┌─────────────────────────┐ ┌─────────────────────────┐         │
│  │ Performance by Diff.    │ │ Problems by Category    │         │
│  │                         │ │                         │         │
│  │     Bar Chart           │ │      Pie Chart          │         │
│  │  ▄▄ ▄▄ ▄▄              │ │         🥧             │         │
│  │  ██ ██ ██              │ │      60% / 40%          │         │
│  │  ██ ██ ██              │ │                         │         │
│  │ Easy Med Hard           │ │  LeetCode | ML Design   │         │
│  └─────────────────────────┘ └─────────────────────────┘         │
│                                                                     │
│  ┌──────────────────────────────────────────────────────┐         │
│  │ Success Rate by Difficulty                            │         │
│  │                                                        │         │
│  │     Line Chart                                         │         │
│  │     ╱──╲                                              │         │
│  │    ╱    ╲___                                          │         │
│  │   Easy Med Hard                                        │         │
│  └──────────────────────────────────────────────────────┘         │
└─────────────────────────────────────────────────────────────────────┘
```

### Progress Page - Tabs

**Overview Tab:**
- 4 stat cards at top
- 2 charts in middle row (Bar, Pie)
- 1 line chart below (Success rate trend)

**Submissions Tab:**
```
Recent Activity
┌──────────────────────────────────────────────┐
│ 💻 Two Sum                        ✓ Oct 28   │
│    Easy    2 attempts                        │
├──────────────────────────────────────────────┤
│ 🧠 Design News Feed              ✗ Oct 27   │
│    Medium  1 attempt                         │
└──────────────────────────────────────────────┘
```

**Feedback Tab:**
```
AI Feedback History
┌──────────────────────────────────────────────┐
│ Two Sum                          Oct 28      │
│                                              │
│ 8/10  7/10  9/10  8/10                      │
│ Corr  Effi  Code  Style                     │
│                                              │
│ Strengths:                                   │
│ • Efficient hash table usage                │
│ • Clean, readable code                      │
│                                              │
│ Improvements:                                │
│ • Could handle edge cases better            │
│ • Add comments for clarity                  │
└──────────────────────────────────────────────┘
```

## Color Usage

### Status Colors
- **Green (#10B981):** Success, passed tests, "easy"
- **Yellow (#F59E0B):** Warning, "medium" difficulty
- **Red (#EF4444):** Failed, errors, "hard" difficulty
- **Blue (#3B82F6):** Active elements, primary actions
- **Purple (#8B5CF6):** ML Design category

### Difficulty Badges
```
[Easy]     - Green background, green text
[Medium]   - Yellow background, yellow text
[Hard]     - Red background, red text
```

### Icons
- 💻 / Code icon - LeetCode
- 🧠 / Brain icon - ML Design
- ⏱️ / Clock icon - Time/Timer
- 📊 / Chart icon - Progress
- ✓ / Check icon - Success
- ✗ / X icon - Failure
- ▶ / Play icon - Run
- 📤 / Send icon - Submit

## Responsive Behavior

### Wide Screen (1920px+)
- Sidebar: 256px
- Question list: 320px
- Description: ~33% of remaining
- Code editor: ~67% of remaining

### Standard Screen (1440px)
- All elements fit comfortably
- No horizontal scroll
- Charts stack in 2 columns

### Laptop Screen (1280px)
- Sidebar stays same width
- Content area adjusts
- Charts may stack vertically

## Interaction States

### Buttons
- **Default:** Medium gray background
- **Hover:** Lighter gray background
- **Active:** Blue background (primary actions)
- **Disabled:** Dark gray, 50% opacity

### Cards
- **Default:** Dark gray, subtle border
- **Hover:** Slightly lighter background
- **Selected:** Blue border (2px)

### Code Editor
- **Typing:** Cursor blinks
- **Running:** Disabled, shows "Running..."
- **Results:** Border pulses briefly on completion

## Typography

### Font Sizes
- **H1 (Page titles):** 30px, bold
- **H2 (Section headers):** 24px, semi-bold
- **H3 (Card headers):** 18px, semi-bold
- **Body:** 14px, regular
- **Small/Meta:** 12px, regular
- **Code:** 14px, monospace

### Font Weights
- Headers: 600-700 (semi-bold to bold)
- Body: 400 (regular)
- Emphasis: 500 (medium)

## Animations

### Transitions
- Button hover: 150ms ease
- Card hover: 200ms ease
- Tab switching: 300ms ease
- Panel collapse: 300ms ease-in-out

### Loading States
- Spinner: Infinite rotation
- Skeleton: Pulse animation
- Progress bar: Smooth fill

## Accessibility

### Contrast Ratios
- White on dark gray: > 7:1 (AAA)
- Blue on dark: > 4.5:1 (AA)
- All text meets WCAG 2.1 standards

### Interactive Elements
- All buttons have :focus states
- Keyboard navigation works
- Screen reader friendly
- ARIA labels on icons

---

This is what your application looks like! Clean, modern, and professional. 🎨
