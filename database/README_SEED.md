# Meta & Atlassian Interview Prep – Canonical Seed

All questions now live in a single generated seed file: `database/seed_complete.sql` (created from the Python sources in `scripts/questions_data*.py`). The seed contains:

- **40 LeetCode questions** tailored to Meta/Atlassian interviews (5 easy, 27 medium, 8 hard)
- **10 ML system design scenarios** covering ranking, content integrity, experimentation, personalization, and fraud detection

For a topic-by-topic breakdown (data structures, ML domains, company focus) read `database/QUESTION_SUMMARY.md`.

## How to Seed the Database

### Option 1 – Run the SQL directly
```bash
cd interview-prep-platform
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql
```

### Option 2 – Use the Python helper
```bash
cd interview-prep-platform
python3 scripts/add_all_questions.py
```

### Option 3 – From the SQLite prompt
```bash
sqlite3 ~/.config/interview-prep-platform/interview-prep.db
sqlite> .read database/seed_complete.sql
sqlite> .quit
```

## Verification

```bash
# Question counts by category
sqlite3 ~/.config/interview-prep-platform/interview-prep.db \
  "SELECT category_id, COUNT(*) FROM questions WHERE category_id IN (1,2) GROUP BY category_id;"

# Difficulty distribution for LeetCode questions
sqlite3 ~/.config/interview-prep-platform/interview-prep.db \
  "SELECT difficulty, COUNT(*) FROM questions WHERE category_id = 1 GROUP BY difficulty;"
```

Expected results: 40 LeetCode (5/27/8) and 10 ML system design.

## What’s Inside the Seed

- **Coding coverage**: Sliding window, two pointers, graph traversal, union find, DP, interval scheduling, design problems (`LRU Cache`, `Implement Trie`).
- **ML design coverage**: Facebook News Feed, Instagram Reels Explore, Atlassian search ranking, content moderation, ad auction ranking, fraud detection, experimentation platforms, personalization, spam/abuse mitigation.
- **Interview realism**: Each entry includes constraints, examples/tests (LeetCode) or requirements/evaluation criteria (ML design).

## Suggested Study Plan (8 Weeks)

Week | Focus | What to practise
--- | --- | ---
1-2 | LeetCode foundations | Arrays, hash tables, two pointers (mix of easy/medium)
3-4 | Core algorithms | Trees/graphs traversal, DP patterns (`Number of Islands`, `Course Schedule`, `Word Break`)
5-6 | System design | Two ML scenarios per week, emphasise requirements, trade-offs, metrics
7-8 | Mock interviews | Alternate timed LeetCode and ML sessions, review solutions & complexity

## Interview Reminders

- **Coding rounds**: communicate trade-offs, start with brute-force, test with edge cases, highlight complexity.
- **ML system design**: clarify objectives (latency, metrics, scale), discuss data/feature pipelines, model choices, experimentation, monitoring, and responsible AI considerations.

Good luck with your preparation! 🚀
