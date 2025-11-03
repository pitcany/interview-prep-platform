#!/usr/bin/env python3
"""
Inject LeetCode URLs into questions_data_full.py

This modifies the file to add leetcode_url field to each question.
"""

import sys
import re

sys.path.insert(0, '.')
from add_leetcode_urls import get_leetcode_url

# Read the file
with open('questions_data_full.py', 'r') as f:
    content = f.read()

# Find all question titles using regex
title_pattern = r'"title":\s*"([^"]+)"'
titles = re.findall(title_pattern, content)

print(f"Found {len(titles)} questions")

# For each title, add the URL field right after the title
for title in titles:
    # Skip if it's an ML question (they don't have LeetCode URLs)
    if any(ml_keyword in title for ml_keyword in ['Design ', 'Netflix', 'YouTube', 'Google', 'Atlassian', 'Face Recognition', 'Translation', 'Fraud Detection', 'Autonomous']):
        continue
    
    url = get_leetcode_url(title)
    
    # Find the pattern: "title": "...",
    # Replace with: "title": "...",\n        "leetcode_url": "...",
    old_pattern = f'"title": "{title}",'
    new_pattern = f'"title": "{title}",\n        "leetcode_url": "{url}",'
    
    # Only replace if URL not already present
    if url not in content:
        content = content.replace(old_pattern, new_pattern, 1)

# Write back
with open('questions_data_full.py', 'w') as f:
    f.write(content)

print("✅ Added LeetCode URLs to all questions")
print("Run: python3 scripts/generate_seed_sql.py to regenerate SQL")
