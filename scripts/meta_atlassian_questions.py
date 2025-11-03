#!/usr/bin/env python3
"""
Optimized dataset for Meta & Atlassian Senior ML Engineer Interviews
40 LeetCode + 10 ML System Design questions
Distribution: 5 Easy, 27 Medium, 8 Hard LeetCode questions

Based on 2025 interview patterns:
- Meta: Heavy focus on arrays/strings (38%), trees, graphs, sparse operations
- Atlassian: ML coding, system design, practical implementations
"""

# Import the original questions
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from complete_questions_data import LEETCODE_QUESTIONS as ORIGINAL_LC, ML_QUESTIONS as ORIGINAL_ML

# Meta/Atlassian specific questions to add
META_ATLASSIAN_ADDITIONS = [
    # MEDIUM - Meta favorites
    {
        "title": "Dot Product of Two Sparse Vectors",
        "difficulty": "medium",
        "description": """Given two sparse vectors, compute their dot product.

Implement class SparseVector:
- SparseVector(nums) Initializes the object with the vector nums
- dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.""",
        "constraints": ["n == nums1.length == nums2.length", "1 <= n <= 10^5", "0 <= nums1[i], nums2[i] <= 100"],
        "examples": [
            {"input": {"nums1": [1,0,0,2,3], "nums2": [0,3,0,4,0]}, "output": 8, "explanation": "Dot product: 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8"},
            {"input": {"nums1": [0,1,0,0,0], "nums2": [0,0,0,0,2]}, "output": 0, "explanation": "No common non-zero indices"}
        ],
        "tags": ["array", "hash-table", "design", "two-pointers"],
        "test_cases": [
            {"input": [[1,0,0,2,3], [0,3,0,4,0]], "expectedOutput": 8},
            {"input": [[0,1,0,0,0], [0,0,0,0,2]], "expectedOutput": 0},
            {"input": [[1,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,1]], "expectedOutput": 1}
        ],
        "time_complexity": "O(n) for constructor, O(min(L1, L2)) for dot product",
        "space_complexity": "O(L) where L is number of non-zero elements",
        "python_sig": "class SparseVector:\n    def __init__(self, nums: List[int]):\n        pass\n    \n    def dotProduct(self, vec: 'SparseVector') -> int:\n        pass",
        "java_sig": "class SparseVector {\n    SparseVector(int[] nums) {\n    }\n    \n    public int dotProduct(SparseVector vec) {\n    }\n}",
        "cpp_sig": "class SparseVector {\npublic:\n    SparseVector(vector<int>& nums) {\n    }\n    \n    int dotProduct(SparseVector& vec) {\n    }\n};"
    },
    {
        "title": "K Closest Points to Origin",
        "difficulty": "medium",
        "description": """Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order.""",
        "constraints": ["1 <= k <= points.length <= 10^4", "-10^4 <= xi, yi <= 10^4"],
        "examples": [
            {"input": {"points": [[1,3],[-2,2]], "k": 1}, "output": [[-2,2]], "explanation": "Distance from origin: (1,3) = sqrt(10), (-2,2) = sqrt(8). (-2,2) is closer."},
            {"input": {"points": [[3,3],[5,-1],[-2,4]], "k": 2}, "output": [[3,3],[-2,4]], "explanation": "Two closest points."}
        ],
        "tags": ["array", "math", "divide-and-conquer", "geometry", "sorting", "heap", "quickselect"],
        "test_cases": [
            {"input": [[[1,3],[-2,2]], 1], "expectedOutput": [[-2,2]]},
            {"input": [[[3,3],[5,-1],[-2,4]], 2], "expectedOutput": [[3,3],[-2,4]]}
        ],
        "time_complexity": "O(n log k) with heap, O(n) average with quickselect",
        "space_complexity": "O(k)",
        "python_sig": "class Solution:\n    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:\n        pass",
        "java_sig": "class Solution {\n    public int[][] kClosest(int[][] points, int k) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {\n        \n    }\n};"
    },
    {
        "title": "Buildings With an Ocean View",
        "difficulty": "medium",
        "description": """There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.""",
        "constraints": ["1 <= heights.length <= 10^5", "1 <= heights[i] <= 10^9"],
        "examples": [
            {"input": {"heights": [4,2,3,1]}, "output": [0,2,3], "explanation": "Building 0, 2, and 3 can see the ocean. Building 1 cannot."},
            {"input": {"heights": [4,3,2,1]}, "output": [0,1,2,3], "explanation": "All buildings have ocean view."}
        ],
        "tags": ["array", "stack", "monotonic-stack"],
        "test_cases": [
            {"input": [[4,2,3,1]], "expectedOutput": [0,2,3]},
            {"input": [[4,3,2,1]], "expectedOutput": [0,1,2,3]},
            {"input": [[1,3,2,4]], "expectedOutput": [3]}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def findBuildings(self, heights: List[int]) -> List[int]:\n        pass",
        "java_sig": "class Solution {\n    public int[] findBuildings(int[] heights) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<int> findBuildings(vector<int>& heights) {\n        \n    }\n};"
    },
    {
        "title": "Minimum Remove to Make Valid Parentheses",
        "difficulty": "medium",
        "description": """Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

A parentheses string is valid if:
- It is the empty string, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.""",
        "constraints": ["1 <= s.length <= 10^5", "s[i] is either '(' , ')', or lowercase English letter"],
        "examples": [
            {"input": {"s": "lee(t(c)o)de)"}, "output": "lee(t(c)o)de", "explanation": "Remove the ')' at index 9."},
            {"input": {"s": "a)b(c)d"}, "output": "ab(c)d", "explanation": "Remove ')' at index 1."},
            {"input": {"s": "))(("}, "output": "", "explanation": "Remove all parentheses."}
        ],
        "tags": ["string", "stack"],
        "test_cases": [
            {"input": ["lee(t(c)o)de)"], "expectedOutput": "lee(t(c)o)de"},
            {"input": ["a)b(c)d"], "expectedOutput": "ab(c)d"},
            {"input": ["))(("], "expectedOutput": ""}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def minRemoveToMakeValid(self, s: str) -> str:\n        pass",
        "java_sig": "class Solution {\n    public String minRemoveToMakeValid(String s) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    string minRemoveToMakeValid(string s) {\n        \n    }\n};"
    },
    {
        "title": "Valid Parenthesis String",
        "difficulty": "medium",
        "description": """Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".""",
        "constraints": ["1 <= s.length <= 100", "s[i] is '(', ')' or '*'"],
        "examples": [
            {"input": {"s": "()"}, "output": True},
            {"input": {"s": "(*)"}, "output": True},
            {"input": {"s": "(*))"}, "output": True},
            {"input": {"s": "(((*"}, "output": False}
        ],
        "tags": ["string", "dynamic-programming", "stack", "greedy"],
        "test_cases": [
            {"input": ["()"], "expectedOutput": True},
            {"input": ["(*)"], "expectedOutput": True},
            {"input": ["(*))"], "expectedOutput": True},
            {"input": ["(((*"], "expectedOutput": False}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def checkValidString(self, s: str) -> bool:\n        pass",
        "java_sig": "class Solution {\n    public boolean checkValidString(String s) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    bool checkValidString(string s) {\n        \n    }\n};"
    },
    # HARD - Meta specific
    {
        "title": "Expression Add Operators",
        "difficulty": "hard",
        "description": """Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.""",
        "constraints": ["1 <= num.length <= 10", "num consists of only digits", "-2^31 <= target <= 2^31 - 1"],
        "examples": [
            {"input": {"num": "123", "target": 6}, "output": ["1*2*3","1+2+3"], "explanation": "Both expressions evaluate to 6."},
            {"input": {"num": "232", "target": 8}, "output": ["2*3+2","2+3*2"], "explanation": "Both evaluate to 8."},
            {"input": {"num": "3456237490", "target": 9191}, "output": [], "explanation": "No valid expressions."}
        ],
        "tags": ["math", "string", "backtracking"],
        "test_cases": [
            {"input": ["123", 6], "expectedOutput": ["1*2*3","1+2+3"]},
            {"input": ["232", 8], "expectedOutput": ["2*3+2","2+3*2"]},
            {"input": ["00", 0], "expectedOutput": ["0*0","0+0","0-0"]}
        ],
        "time_complexity": "O(4^n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def addOperators(self, num: str, target: int) -> List[str]:\n        pass",
        "java_sig": "class Solution {\n    public List<String> addOperators(String num, int target) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<string> addOperators(string num, int target) {\n        \n    }\n};"
    },
]

# Questions to remove (3 easy questions for senior level)
QUESTIONS_TO_REMOVE = [
    "Merge Two Sorted Lists",
    "Valid Palindrome", 
    "Binary Tree Inorder Traversal"
]

# Filter and rebuild LeetCode questions
def get_optimized_leetcode_questions():
    """Get optimized question set for Meta/Atlassian - exactly 40 questions"""
    # Remove specified easy questions
    filtered = [q for q in ORIGINAL_LC if q['title'] not in QUESTIONS_TO_REMOVE]
    
    # Add Meta/Atlassian specific questions
    filtered.extend(META_ATLASSIAN_ADDITIONS)
    
    # Now we have 47 questions (50 - 3 + 6)
    # We need exactly 40: 5 Easy, 27 Medium, 8 Hard
    
    easy_qs = [q for q in filtered if q['difficulty'] == 'easy']  # Should be 5
    medium_qs = [q for q in filtered if q['difficulty'] == 'medium'][:27]  # Take first 27
    hard_qs = [q for q in filtered if q['difficulty'] == 'hard']  # Should be 8
    
    return easy_qs + medium_qs + hard_qs

# Optimized ML questions for Meta/Atlassian
OPTIMIZED_ML_QUESTIONS = [
    {
        "title": "Design Content Moderation System (Meta)",
        "difficulty": "hard",
        "description": "Design a real-time content moderation system for Meta/Facebook that automatically detects and filters inappropriate content (hate speech, violence, spam, misinformation) across billions of posts, comments, and media.",
        "scenario": """Meta needs a content moderation system that:
- Processes billions of posts/comments/images/videos daily
- Detects multiple violation types: hate speech, violence, spam, nudity, misinformation
- Works in real-time (<1 second for text, <10 seconds for media)
- Handles 100+ languages
- Balances false positives (removing legitimate content) with false negatives (missing violations)
- Provides human review queue for borderline cases
- Adapts to new violation patterns quickly
- Maintains user privacy and handles appeals

The system must scale globally while meeting regulatory requirements in different regions.""",
        "requirements": [
            "Real-time detection (<1s for text, <10s for media)",
            "Multi-modal: text, images, videos, audio",
            "Multi-class classification (hate speech, violence, spam, etc.)",
            "Multi-language support (100+ languages)",
            "Handle billions of items daily",
            "Low false positive rate (precision >95%)",
            "High recall for severe violations (>98%)",
            "Human-in-the-loop for borderline cases",
            "Explainable decisions for appeals",
            "Quick adaptation to new violation patterns",
            "Region-specific policies"
        ],
        "evaluation_criteria": {
            "problem_understanding": "Understood multi-modal, multi-class, multi-language complexity",
            "model_architecture": "Appropriate models for text (transformers), images (CNNs), video",
            "data_pipeline": "Handling labeled data, active learning, human labeling",
            "scalability": "Distributed inference, model serving at Meta scale",
            "precision_recall_tradeoff": "Strategy for balancing false positives vs negatives",
            "human_in_loop": "Queue management, reviewer workflow, feedback loop",
            "adaptation": "Online learning, handling emerging patterns",
            "explainability": "LIME/SHAP for appeals, policy alignment"
        },
        "key_components": [
            "Multi-modal Feature Extraction",
            "Text Classification (BERT/RoBERTa for hate speech)",
            "Image/Video Classification (ResNet/EfficientNet)",
            "Audio Analysis (for video content)",
            "Ensemble Models for final decision",
            "Real-time Serving Infrastructure",
            "Human Review Queue & Workflow",
            "Active Learning Pipeline",
            "Appeal & Explanation System",
            "A/B Testing Framework",
            "Regional Policy Engine"
        ],
        "tags": ["content-moderation", "multi-modal", "classification", "real-time", "human-in-loop", "meta"]
    },
    {
        "title": "Design Search/Discovery System for Atlassian Products",
        "difficulty": "medium",
        "description": "Design an intelligent search and discovery system for Atlassian products (Jira, Confluence) that helps users find relevant issues, pages, and projects across their workspace using natural language queries.",
        "scenario": """Atlassian needs a unified search system across Jira and Confluence that:
- Understands natural language queries ('bug reports from last sprint about login')
- Searches across multiple data types: Jira issues, Confluence pages, comments, attachments
- Provides personalized results based on user's role, projects, and history
- Handles large workspaces (100K+ issues, 50K+ pages)
- Works with structured data (Jira fields) and unstructured data (Confluence content)
- Supports semantic search beyond keyword matching
- Ranks results by relevance, recency, and user context
- Provides faceted filtering and auto-complete

The system must work efficiently for both small teams and enterprise customers.""",
        "requirements": [
            "Natural language query understanding",
            "Multi-source search (Jira issues, Confluence pages, comments)",
            "Semantic search with embeddings",
            "Personalized ranking based on user context",
            "Sub-second query latency",
            "Handle 100K+ issues per workspace",
            "Faceted search and filtering",
            "Auto-complete and query suggestions",
            "Permission-aware results",
            "Cross-product search integration"
        ],
        "evaluation_criteria": {
            "query_understanding": "NLP for intent and entity extraction from queries",
            "semantic_search": "Embedding models for semantic similarity",
            "ranking_model": "Learning-to-rank with personalization signals",
            "indexing_strategy": "Efficient indexing for structured and unstructured data",
            "personalization": "User context, project access, search history",
            "latency": "Optimization for sub-second response",
            "scalability": "Handle enterprise workspaces efficiently"
        },
        "key_components": [
            "Query Understanding (NLP, Entity Extraction)",
            "Document Indexing (Elasticsearch)",
            "Semantic Embedding Models",
            "Hybrid Search (keyword + semantic)",
            "Ranking Model with Personalization",
            "Permission & Access Control",
            "Query Auto-complete",
            "Result Aggregation across products",
            "Click-through Rate tracking",
            "A/B Testing for ranking improvements"
        ],
        "tags": ["search", "nlp", "semantic-search", "enterprise", "atlassian", "personalization"]
    },
    # Keep these from original
    {
        "title": "Design Netflix Movie Recommendation System",
        "difficulty": "medium",
        "description": "Design a personalized movie/TV show recommendation system for Netflix with 200M+ subscribers. The system should provide real-time, personalized content recommendations while handling cold start problems for new users and content.",
        "scenario": """Netflix wants to improve user engagement and content discovery by building a sophisticated recommendation system. The platform has:
- 200M+ active subscribers globally
- 10,000+ movies and TV shows
- User interactions: watch history, ratings, search queries, browsing behavior
- Content metadata: genre, cast, director, release year, language
- Real-time viewing patterns and completion rates

The system must balance personalization with content diversity, handle the cold start problem for new users/content, and provide explainable recommendations.""",
        "requirements": [
            "Handle 200M+ active users with real-time recommendations",
            "Provide personalized recommendations based on viewing history and preferences",
            "Handle cold start problem for new users and new content",
            "Support multiple recommendation strategies (collaborative filtering, content-based, hybrid)",
            "Implement A/B testing framework for new recommendation algorithms",
            "Provide explainability for recommendations",
            "Scale to handle peak traffic during new content releases",
            "Optimize for user engagement metrics (watch time, completion rate)"
        ],
        "evaluation_criteria": {
            "problem_understanding": "Clarified requirements, success metrics, and constraints",
            "data_pipeline": "Comprehensive feature engineering and data processing approach",
            "model_design": "Appropriate model architecture for recommendations (collaborative filtering, neural networks, etc.)",
            "scalability": "System handles 200M users efficiently with low latency",
            "evaluation_metrics": "Clear offline (RMSE, precision@k) and online (CTR, watch time) metrics",
            "cold_start_strategy": "Effective approach for new users/items",
            "explainability": "Method to explain why content was recommended"
        },
        "key_components": [
            "Data Collection & Feature Engineering",
            "Candidate Generation (retrieve top-k items)",
            "Ranking Model (score and rank candidates)",
            "Serving Infrastructure (low-latency API)",
            "Offline & Online Evaluation Metrics",
            "A/B Testing Framework",
            "Cold Start Strategy",
            "Explainability Module"
        ],
        "tags": ["recommendation", "ranking", "collaborative-filtering", "cold-start", "scalability"]
    },
    {
        "title": "Design News Feed Ranking (Facebook/Instagram)",
        "difficulty": "medium",
        "description": "Design the machine learning system that ranks posts in social media news feeds to maximize user engagement.",
        "scenario": """A social media platform with 2B+ users needs to rank posts in personalized news feeds. The system must:
- Rank posts from friends, pages, and groups
- Predict user engagement (likes, comments, shares, watch time)
- Balance different content types (text, image, video, links)
- Consider recency and virality
- Optimize for meaningful interactions (not just clicks)
- Handle diverse user preferences and contexts

The system processes millions of candidate posts per user and must serve feeds with low latency.""",
        "requirements": [
            "Rank feeds for 2B+ users in real-time",
            "Predict multiple engagement types (likes, comments, shares)",
            "Multi-objective optimization (engagement vs quality)",
            "Handle different content types with different engagement patterns",
            "Consider recency, virality, and social connections",
            "Personalization based on user preferences and history",
            "Low-latency serving (<500ms)",
            "Combat clickbait and low-quality content"
        ],
        "evaluation_criteria": {
            "prediction_model": "Multi-task learning for different engagement types",
            "feature_engineering": "User, post, and social graph features",
            "ranking_strategy": "Multi-objective optimization approach",
            "scalability": "Efficient candidate retrieval and ranking",
            "quality_control": "Mechanisms to reduce low-quality content",
            "evaluation_metrics": "Time spent, meaningful interactions, user satisfaction"
        },
        "key_components": [
            "Candidate Generation (retrieve relevant posts)",
            "Feature Engineering (user, post, context)",
            "Multi-task Prediction Model (engagement types)",
            "Ranking with Multi-objective Optimization",
            "Quality Scoring & Clickbait Detection",
            "Real-time Feature Computation",
            "Distributed Serving Infrastructure",
            "Online Learning & Feedback Loops",
            "A/B Testing Framework"
        ],
        "tags": ["ranking", "social-media", "multi-task-learning", "personalization", "engagement", "meta"]
    },
    {
        "title": "Design Google Search Ranking System",
        "difficulty": "hard",
        "description": "Design the machine learning system behind Google Search that ranks web pages for a given search query.",
        "scenario": """Google Search processes billions of queries daily and must rank billions of web pages. The system needs to:
- Understand user intent from short queries
- Rank pages based on relevance, authority, freshness, and user experience
- Handle different query types (informational, navigational, transactional)
- Provide personalized results based on user context
- Combat spam and low-quality content
- Serve results with <200ms latency

The system uses signals from page content, link structure, user behavior, and contextual factors.""",
        "requirements": [
            "Process billions of queries with <200ms latency",
            "Rank billions of web pages for relevance",
            "Understand query intent and context",
            "Personalization based on user history and location",
            "Quality signals to combat spam",
            "Handle different query types and domains",
            "Real-time indexing of new content",
            "Multi-language and multi-region support"
        ],
        "evaluation_criteria": {
            "query_understanding": "NLP techniques for intent classification",
            "ranking_model": "Learning-to-rank approach with hundreds of features",
            "scalability": "Distributed architecture for billions of pages",
            "latency": "Sub-200ms response time",
            "relevance_signals": "Page content, links, user behavior signals",
            "quality_filtering": "Spam detection and quality assessment",
            "personalization": "Context-aware ranking adjustments",
            "evaluation": "NDCG, MRR, and online metrics (CTR, long clicks)"
        },
        "key_components": [
            "Query Understanding (NLP, Intent Classification)",
            "Document Indexing & Retrieval",
            "Feature Engineering (500+ ranking signals)",
            "Learning-to-Rank Model (GBDT or Neural)",
            "Quality & Spam Detection",
            "Personalization Layer",
            "Distributed Serving Infrastructure",
            "Online Learning & Feedback Loops",
            "A/B Testing Framework"
        ],
        "tags": ["search", "ranking", "nlp", "learning-to-rank", "scalability"]
    },
    {
        "title": "Design E-commerce Product Recommendation System",
        "difficulty": "medium",
        "description": "Design a product recommendation system for an e-commerce platform like Amazon that personalizes product suggestions across various touchpoints.",
        "scenario": """An e-commerce platform with 100M+ products and 500M+ users needs a recommendation system for:
- Homepage personalized recommendations
- Product detail page (frequently bought together, similar items)
- Shopping cart recommendations
- Email campaigns
- Search result ranking

The system must handle diverse product catalog, seasonal trends, inventory constraints, and optimize for conversion rate and revenue.""",
        "requirements": [
            "Handle 100M+ products and 500M+ users",
            "Multiple recommendation types (similar items, complementary products, personalized)",
            "Real-time recommendations based on current session",
            "Consider inventory levels and business rules",
            "Optimize for conversion rate and revenue",
            "Handle seasonal trends and promotional events",
            "Support different channels (web, mobile, email)",
            "Cold start for new products and users"
        ],
        "evaluation_criteria": {
            "business_understanding": "Optimization for revenue and conversion",
            "recommendation_types": "Multiple recommendation strategies",
            "real_time_capability": "Session-based recommendations",
            "inventory_awareness": "Integration with inventory system",
            "personalization": "User-specific recommendations",
            "scalability": "Handles large product catalog efficiently",
            "evaluation_metrics": "CTR, conversion rate, revenue per user"
        },
        "key_components": [
            "User Behavior Tracking",
            "Product Catalog Feature Engineering",
            "Session-based Recommendations",
            "Collaborative Filtering Models",
            "Content-based Filtering",
            "Business Rules Engine (inventory, promotions)",
            "Multi-arm Bandit for Exploration",
            "Real-time Serving Layer",
            "A/B Testing & Revenue Attribution"
        ],
        "tags": ["recommendation", "e-commerce", "personalization", "real-time", "conversion-optimization"]
    },
    {
        "title": "Design Face Recognition System",
        "difficulty": "medium",
        "description": "Design a scalable face recognition system for authentication or identification in applications like security, photo tagging, or access control.",
        "scenario": """Build a face recognition system that:
- Enrolls users by capturing and storing face embeddings
- Authenticates users in real-time from camera input
- Handles variations in lighting, pose, and aging
- Works across different devices and camera qualities
- Maintains privacy and security of biometric data
- Scales to millions of enrolled users

The system is used for authentication (1:1 matching) and identification (1:N search).""",
        "requirements": [
            "High accuracy (>99% verification accuracy)",
            "Low false positive rate for security",
            "Real-time processing (<1 second per verification)",
            "Handle variations (lighting, pose, expressions, aging)",
            "Scale to millions of enrolled users",
            "Privacy-preserving (store embeddings, not raw images)",
            "Work with different camera qualities",
            "Support both 1:1 verification and 1:N identification",
            "Anti-spoofing (detect fake faces, photos)"
        ],
        "evaluation_criteria": {
            "model_architecture": "Deep learning model for face embedding",
            "accuracy_metrics": "FAR, FRR, verification accuracy",
            "robustness": "Handle real-world variations",
            "scalability": "Efficient 1:N search in large databases",
            "privacy": "Secure storage and processing of biometric data",
            "anti_spoofing": "Liveness detection techniques",
            "deployment": "Edge vs cloud deployment considerations"
        },
        "key_components": [
            "Face Detection & Alignment",
            "Face Embedding Model (ResNet, FaceNet, ArcFace)",
            "Embedding Storage & Indexing (Vector DB)",
            "Similarity Matching (Cosine Distance)",
            "Liveness Detection (Anti-spoofing)",
            "Enrollment Pipeline",
            "Real-time Verification API",
            "Model Retraining with New Data",
            "Privacy & Security Measures"
        ],
        "tags": ["computer-vision", "face-recognition", "biometrics", "deep-learning", "security"]
    },
    {
        "title": "Design Object Detection System for Autonomous Vehicles",
        "difficulty": "hard",
        "description": "Design a real-time object detection system for autonomous vehicles that identifies and tracks pedestrians, vehicles, traffic signs, and obstacles.",
        "scenario": """An autonomous vehicle system needs real-time object detection that:
- Detects multiple object types (cars, pedestrians, cyclists, signs)
- Runs in real-time (30+ FPS) on vehicle hardware
- Provides accurate bounding boxes and classifications
- Handles various weather and lighting conditions
- Maintains high recall (cannot miss critical objects)
- Integrates with sensor fusion (cameras, LiDAR, radar)
- Provides distance estimation and tracking

Safety is critical - false negatives can be catastrophic.""",
        "requirements": [
            "Real-time processing (30+ FPS) with low latency (<50ms)",
            "High recall (>99% for critical objects like pedestrians)",
            "Detect multiple object classes simultaneously",
            "Handle challenging conditions (night, rain, fog)",
            "3D bounding boxes with distance estimation",
            "Object tracking across frames",
            "Sensor fusion (camera + LiDAR + radar)",
            "Run on edge hardware (GPUs in vehicle)",
            "Safety validation and redundancy"
        ],
        "evaluation_criteria": {
            "model_architecture": "Efficient real-time detection model (YOLO, SSD, etc.)",
            "accuracy_metrics": "mAP, recall for safety-critical classes",
            "real_time_performance": "Latency and throughput on edge hardware",
            "robustness": "Performance in adverse conditions",
            "sensor_fusion": "Integration of multiple sensor modalities",
            "tracking": "Multi-object tracking accuracy",
            "safety": "Fail-safe mechanisms and redundancy"
        },
        "key_components": [
            "Multi-sensor Data Collection (Camera, LiDAR, Radar)",
            "Real-time Object Detection Model (YOLO, Faster R-CNN)",
            "3D Bounding Box Estimation",
            "Sensor Fusion Algorithm",
            "Multi-object Tracking (Kalman Filter, DeepSORT)",
            "Edge Deployment (TensorRT, ONNX optimization)",
            "Safety Validation & Testing",
            "Continuous Learning from Fleet Data",
            "Redundancy & Fail-safe Mechanisms"
        ],
        "tags": ["computer-vision", "object-detection", "autonomous-vehicles", "real-time", "safety-critical"]
    },
    {
        "title": "Design Machine Translation System",
        "difficulty": "hard",
        "description": "Design a neural machine translation system like Google Translate that translates text between multiple languages with high quality.",
        "scenario": """Build a machine translation system that:
- Supports 100+ language pairs
- Provides high-quality, fluent translations
- Handles domain-specific terminology
- Maintains context across sentences
- Works in real-time for web and mobile apps
- Handles informal language, slang, and idioms
- Preserves formatting and special characters

The system serves millions of translation requests per day across diverse domains.""",
        "requirements": [
            "Support 100+ languages (10,000+ language pairs)",
            "High translation quality (BLEU score >30 for major pairs)",
            "Real-time translation (<1 second for typical sentences)",
            "Context-aware (consider previous sentences)",
            "Handle domain-specific terminology",
            "Low-resource language support",
            "Preserve formatting, punctuation, numbers",
            "API for high-throughput batch translation",
            "Continuous improvement from user feedback"
        ],
        "evaluation_criteria": {
            "model_architecture": "Transformer-based seq2seq model",
            "training_data": "Parallel corpus collection and preprocessing",
            "multilingual_strategy": "Multilingual vs bilingual models",
            "quality_metrics": "BLEU, METEOR, human evaluation",
            "contextual_understanding": "Document-level translation",
            "domain_adaptation": "Fine-tuning for specific domains",
            "serving_infrastructure": "Low-latency, high-throughput API",
            "feedback_loop": "Learning from user corrections"
        },
        "key_components": [
            "Parallel Corpus Collection & Cleaning",
            "Tokenization & Subword Segmentation (BPE, SentencePiece)",
            "Transformer Model (Encoder-Decoder)",
            "Multilingual Training Strategy",
            "Beam Search Decoding",
            "Domain Adaptation Fine-tuning",
            "Quality Estimation Model",
            "Real-time Serving Infrastructure",
            "Human Feedback Integration",
            "Model Distillation for Efficiency"
        ],
        "tags": ["nlp", "machine-translation", "transformers", "multilingual", "seq2seq"]
    },
    {
        "title": "Design Credit Card Fraud Detection System",
        "difficulty": "medium",
        "description": "Design a real-time fraud detection system for credit card transactions that identifies fraudulent activities while minimizing false positives.",
        "scenario": """A payment processor handles millions of credit card transactions daily and needs a fraud detection system that:
- Analyzes transactions in real-time (<100ms)
- Detects various fraud patterns (stolen cards, account takeover, synthetic fraud)
- Minimizes false positives (legitimate transactions blocked)
- Adapts to new fraud tactics quickly
- Provides explainability for blocked transactions
- Handles imbalanced data (fraud rate <1%)

The system must balance security with user experience.""",
        "requirements": [
            "Real-time scoring (<100ms per transaction)",
            "High fraud detection rate (>90% recall)",
            "Low false positive rate (<2%)",
            "Handle class imbalance (fraud <1% of transactions)",
            "Detect emerging fraud patterns quickly",
            "Explainable predictions for compliance",
            "Scale to millions of transactions per day",
            "Support multiple fraud types",
            "Feedback loop from fraud investigations"
        ],
        "evaluation_criteria": {
            "model_design": "Appropriate models for imbalanced classification",
            "feature_engineering": "Transaction, user, and behavioral features",
            "real_time_processing": "Streaming architecture for low latency",
            "handling_imbalance": "Sampling, weighting, or specialized algorithms",
            "adaptability": "Online learning or frequent retraining",
            "explainability": "SHAP values or rule-based explanations",
            "evaluation_metrics": "Precision, recall, F1, ROC-AUC for imbalanced data"
        },
        "key_components": [
            "Real-time Transaction Feature Engineering",
            "Behavioral Analytics (velocity, patterns)",
            "Fraud Detection Model (Gradient Boosting, Neural Networks)",
            "Handling Class Imbalance (SMOTE, class weighting)",
            "Rule-based Detection for Known Patterns",
            "Anomaly Detection for Novel Fraud",
            "Real-time Scoring Infrastructure",
            "Explainability Module (SHAP, LIME)",
            "Feedback Loop from Fraud Investigations",
            "Model Monitoring & Retraining"
        ],
        "tags": ["fraud-detection", "classification", "real-time", "imbalanced-data", "anomaly-detection"]
    }
]

# Export optimized questions
LEETCODE_QUESTIONS = get_optimized_leetcode_questions()
ML_QUESTIONS = OPTIMIZED_ML_QUESTIONS

if __name__ == "__main__":
    print(f"Optimized for Meta & Atlassian Senior ML Engineer")
    print(f"LeetCode: {len(LEETCODE_QUESTIONS)} questions")
    
    easy = len([q for q in LEETCODE_QUESTIONS if q['difficulty'] == 'easy'])
    medium = len([q for q in LEETCODE_QUESTIONS if q['difficulty'] == 'medium'])
    hard = len([q for q in LEETCODE_QUESTIONS if q['difficulty'] == 'hard'])
    
    print(f"  Easy: {easy}, Medium: {medium}, Hard: {hard}")
    print(f"ML System Design: {len(ML_QUESTIONS)} questions")
    print(f"\nMeta-specific additions:")
    print(f"  - Dot Product of Sparse Vectors")
    print(f"  - K Closest Points to Origin")
    print(f"  - Buildings With Ocean View")
    print(f"  - Minimum Remove to Make Valid Parentheses")
    print(f"  - Valid Parenthesis String")
    print(f"  - Expression Add Operators")
    print(f"\nML additions:")
    print(f"  - Content Moderation System (Meta)")
    print(f"  - Search System for Atlassian Products")
