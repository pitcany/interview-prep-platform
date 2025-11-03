-- Sample LeetCode Questions

-- Easy: Two Sum
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Two Sum', 'easy', 
'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.',
'["2 <= nums.length <= 10^4", "-10^9 <= nums[i] <= 10^9", "-10^9 <= target <= 10^9", "Only one valid answer exists"]',
'[{"input": {"nums": [2,7,11,15], "target": 9}, "output": [0,1], "explanation": "Because nums[0] + nums[1] == 9, we return [0, 1]."}]',
'["array", "hash-table"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(1, 
'class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        pass',
'class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        \n    }\n};',
'[{"input": [[2,7,11,15], 9], "expectedOutput": [0,1]}, {"input": [[3,2,4], 6], "expectedOutput": [1,2]}, {"input": [[3,3], 6], "expectedOutput": [0,1]}]',
'O(n)', 'O(n)');

-- Medium: Longest Substring Without Repeating Characters
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Longest Substring Without Repeating Characters', 'medium',
'Given a string s, find the length of the longest substring without repeating characters.',
'["0 <= s.length <= 5 * 10^4", "s consists of English letters, digits, symbols and spaces"]',
'[{"input": {"s": "abcabcbb"}, "output": 3, "explanation": "The answer is \"abc\", with the length of 3."}, {"input": {"s": "bbbbb"}, "output": 1, "explanation": "The answer is \"b\", with the length of 1."}]',
'["string", "sliding-window", "hash-table"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(2,
'class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        pass',
'class Solution {\n    public int lengthOfLongestSubstring(String s) {\n        \n    }\n}',
'class Solution {\npublic:\n    int lengthOfLongestSubstring(string s) {\n        \n    }\n};',
'[{"input": ["abcabcbb"], "expectedOutput": 3}, {"input": ["bbbbb"], "expectedOutput": 1}, {"input": ["pwwkew"], "expectedOutput": 3}]',
'O(n)', 'O(min(m,n))');

-- Medium: Container With Most Water
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Container With Most Water', 'medium',
'You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.',
'["n == height.length", "2 <= n <= 10^5", "0 <= height[i] <= 10^4"]',
'[{"input": {"height": [1,8,6,2,5,4,8,3,7]}, "output": 49, "explanation": "The max area is between index 1 and 8."}]',
'["array", "two-pointers", "greedy"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(3,
'class Solution:\n    def maxArea(self, height: List[int]) -> int:\n        pass',
'class Solution {\n    public int maxArea(int[] height) {\n        \n    }\n}',
'class Solution {\npublic:\n    int maxArea(vector<int>& height) {\n        \n    }\n};',
'[{"input": [[1,8,6,2,5,4,8,3,7]], "expectedOutput": 49}, {"input": [[1,1]], "expectedOutput": 1}]',
'O(n)', 'O(1)');

-- Sample ML System Design Questions

-- Design a News Feed Ranking System
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design a News Feed Ranking System', 'medium',
'You are tasked with designing a personalized news feed ranking system for a social media platform similar to Facebook or Instagram.

Context:
- Platform has 2 billion monthly active users
- Users see a feed of posts from friends, pages they follow, and recommended content
- Need to rank posts to show most relevant content first
- System must handle real-time updates and be highly scalable

Your Task:
Design an ML system that ranks posts in a user''s news feed. Consider data collection, feature engineering, model selection, training pipeline, serving infrastructure, and evaluation metrics.',
'["ml-system-design", "recommendation", "ranking", "distributed-systems"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(4,
'Design an ML system for ranking posts in a social media news feed with 2B+ users.',
'["Real-time ranking (< 100ms latency)", "Personalized for each user", "Handle billions of posts daily", "Incorporate engagement signals (likes, comments, shares)", "Balance relevance, recency, and diversity"]',
'{"problem_understanding": "Clarified requirements, constraints, and success metrics", "data_pipeline": "Comprehensive data collection and feature engineering approach", "model_design": "Appropriate model choice with justification", "scalability": "System handles scale with proper architecture", "evaluation": "Clear metrics and A/B testing strategy", "trade_offs": "Discussion of trade-offs and alternative approaches"}',
'["Data Collection & Features", "Model Architecture", "Training Pipeline", "Serving Infrastructure", "Ranking Logic", "Evaluation & Monitoring", "A/B Testing"]');

-- Design a Fraud Detection System
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design a Real-time Fraud Detection System', 'hard',
'Design a real-time fraud detection system for an e-commerce platform like Amazon or eBay.

Context:
- Platform processes millions of transactions per day
- Need to detect fraudulent transactions in real-time (< 50ms)
- Must minimize false positives while catching fraud
- Fraud patterns evolve over time
- System must be explainable for compliance

Your Task:
Design an ML system that detects fraudulent transactions in real-time. Consider feature engineering, model selection, real-time inference, model updates, and handling imbalanced data.',
'["ml-system-design", "fraud-detection", "real-time", "anomaly-detection", "imbalanced-data"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(5,
'Design a real-time fraud detection system for e-commerce transactions.',
'["Real-time inference (< 50ms)", "Handle millions of transactions/day", "Minimize false positives", "Catch evolving fraud patterns", "Provide explainability", "Handle class imbalance"]',
'{"problem_understanding": "Understood fraud detection challenges and constraints", "feature_engineering": "Thoughtful features for fraud detection", "model_selection": "Appropriate models with rationale", "real_time_serving": "Low-latency inference architecture", "handling_imbalance": "Strategies for imbalanced data", "monitoring": "Detection of model drift and fraud pattern changes", "explainability": "Model interpretability for compliance"}',
'["Feature Engineering", "Model Architecture", "Real-time Inference", "Data Imbalance Handling", "Model Updating", "Monitoring & Alerting", "Explainability"]');

-- Design a Search Ranking System
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design a Search Ranking System', 'hard',
'Design a search ranking system for an e-commerce platform.

Context:
- Platform has millions of products
- Users search with natural language queries
- Need to return relevant results quickly (< 200ms)
- Consider personalization based on user history
- Must handle spelling errors, synonyms
- Support filtering and sorting

Your Task:
Design an ML-powered search ranking system. Consider query understanding, candidate generation, ranking models, personalization, and evaluation metrics.',
'["ml-system-design", "search", "ranking", "nlp", "information-retrieval"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(6,
'Design an ML-powered search ranking system for e-commerce.',
'["Return results in < 200ms", "Handle millions of products", "Natural language understanding", "Personalization", "Handle typos and synonyms", "Support filters"]',
'{"problem_understanding": "Understood search ranking requirements", "query_processing": "Query understanding and expansion", "candidate_generation": "Efficient retrieval from large catalog", "ranking_model": "Appropriate ranking approach", "personalization": "User-specific ranking signals", "evaluation": "Comprehensive offline and online metrics", "system_design": "Scalable architecture"}',
'["Query Understanding", "Candidate Generation", "Ranking Model", "Personalization", "Feature Engineering", "Evaluation Metrics", "Serving Architecture"]');
