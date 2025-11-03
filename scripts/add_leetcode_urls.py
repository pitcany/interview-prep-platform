#!/usr/bin/env python3
"""
Add LeetCode URLs to all questions

This script adds the leetcode_url field to each LeetCode question
based on the standard LeetCode problem URL format.
"""

def title_to_slug(title):
    """Convert question title to LeetCode URL slug"""
    # LeetCode uses lowercase with hyphens
    slug = title.lower()
    # Replace spaces and special characters with hyphens
    slug = slug.replace(' ', '-')
    slug = slug.replace('(', '')
    slug = slug.replace(')', '')
    slug = slug.replace('/', '-')
    slug = slug.replace("'", '')
    # Remove multiple consecutive hyphens
    while '--' in slug:
        slug = slug.replace('--', '-')
    return slug

# Map of question titles to their correct LeetCode slugs
# (Some titles don't match the URL exactly)
SLUG_OVERRIDES = {
    "3Sum": "3sum",
    "Remove Nth Node From End of List": "remove-nth-node-from-end-of-list",
    "Kth Smallest Element in a BST": "kth-smallest-element-in-a-bst",
    "Path Sum II": "path-sum-ii",
    "Reverse Linked List II": "reverse-linked-list-ii",
    "Binary Tree Right Side View": "binary-tree-right-side-view",
    "Buildings With an Ocean View": "buildings-with-an-ocean-view",
    "K Closest Points to Origin": "k-closest-points-to-origin",
}

def get_leetcode_url(title):
    """Get the full LeetCode URL for a question"""
    if title in SLUG_OVERRIDES:
        slug = SLUG_OVERRIDES[title]
    else:
        slug = title_to_slug(title)
    return f"https://leetcode.com/problems/{slug}/"

if __name__ == "__main__":
    # Test with some examples
    test_titles = [
        "Two Sum",
        "3Sum",
        "Longest Substring Without Repeating Characters",
        "Buildings With an Ocean View"
    ]
    
    print("Testing URL generation:")
    for title in test_titles:
        print(f"{title}")
        print(f"  → {get_leetcode_url(title)}")
        print()
