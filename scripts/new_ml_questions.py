# Meta/Atlassian Senior ML Engineer - ML System Design Questions
# Replace the ML_QUESTIONS section in questions_data_full.py with this

ML_QUESTIONS = [
    {
        "title": "Design Facebook News Feed Ranking System",
        "difficulty": "hard",
        "description": "Design the ML ranking system for Facebook's News Feed that serves 3B+ users, deciding which posts to show and in what order to maximize meaningful user engagement.",
        "scenario": """Facebook's News Feed is the core product serving 3B+ users daily. The ML system must:
- Rank posts from friends, pages, groups, and ads
- Process millions of candidate posts per user
- Predict multiple engagement types (likes, comments, shares, time spent, hide/report)
- Optimize for "meaningful social interactions" not just clicks
- Handle diverse content types (text, photo, video, link, live)
- Serve feeds in <500ms while making complex ML predictions
- Combat engagement bait, clickbait, and misinformation
- Balance organic content with ads (revenue optimization)

The system processes billions of posts daily, makes trillions of predictions, and directly impacts Meta's $100B+ revenue.""",
        "requirements": [
            "Rank feeds for 3B+ users in real-time (<500ms latency)",
            "Multi-task prediction: likes, comments, shares, time spent, hide",
            "Multi-objective optimization (engagement + quality + revenue)",
            "Handle multiple content types with different engagement patterns",
            "Lightweight models for edge devices (mobile)",
            "Feature freshness (recent interactions matter)",
            "Virality modeling (predict shares/spread)",
            "Counter-abuse: clickbait, engagement bait, misinformation",
            "Personalization at scale with privacy constraints",
            "Seamless A/B testing infrastructure"
        ],
        "evaluation_criteria": {
            "architecture": "Two-stage: candidate generation + heavy ranking",
            "model_design": "Multi-task learning for different engagement types",
            "feature_engineering": "User features, post features, social graph, temporal",
            "training_pipeline": "Distributed training, online learning",
            "serving_infra": "Low-latency prediction serving at scale",
            "multi_objective": "Balancing engagement, quality, revenue, user satisfaction",
            "counter_abuse": "Strategies to detect and demote low-quality content",
            "evaluation": "Online metrics (time spent, DAU), offline metrics (AUC, calibration)"
        },
        "key_components": [
            "Candidate Generation (filter from millions to thousands)",
            "Heavy Ranker (GBDT or Deep Neural Network)",
            "Multi-task Head (predict likes, comments, shares, time, hide)",
            "Post-ranking Filters (diversity, freshness, ads insertion)",
            "Real-time Feature Store",
            "Online Learning Pipeline",
            "Counter-abuse Models (clickbait, misinformation)",
            "A/B Testing Platform",
            "Metrics Dashboard (time spent, meaningful interactions)"
        ],
        "tags": ["ranking", "multi-task-learning", "news-feed", "meta", "scale", "personalization"]
    },
    {
        "title": "Design Instagram Reels Recommendation System",
        "difficulty": "hard",
        "description": "Design the ML system powering Instagram Reels recommendations - a TikTok competitor serving short-form video to 2B+ users with multi-modal understanding.",
        "scenario": """Instagram Reels competes with TikTok by recommending engaging short-form videos. The system must:
- Understand video content (visual, audio, text, music)
- Cold start: recommend videos to new users and new videos to users
- Optimize for watch time and completion rate
- Handle the \"creator economy\" (help creators grow)
- Prevent filter bubbles while maximizing engagement
- Support audio trends (viral sounds)
- Real-time: new videos should surface quickly
- Multi-modal: video, audio, captions, hashtags, music

Key challenge: Unlike Feed (friends/following), Reels is discovery-based like TikTok.""",
        "requirements": [
            "Multi-modal understanding (video, audio, text, music)",
            "Real-time recommendations (<100ms)",
            "Cold start for new users and new content",
            "Optimize for watch time and completion rate",
            "Surface trending content quickly (viral detection)",
            "Creator growth (help small creators get discovered)",
            "Audio-based features (trending sounds)",
            "Prevent filter bubbles (content diversity)",
            "Handle billions of videos",
            "Mobile-first (lightweight models)"
        ],
        "evaluation_criteria": {
            "multi_modal": "How video, audio, text signals are combined",
            "cold_start": "Strategy for new users and new content",
            "viral_detection": "Identifying trending content early",
            "model_architecture": "Two-tower, transformers, or hybrid approach",
            "feature_engineering": "Video embeddings, audio features, engagement signals",
            "training": "Handling data skew (power law distribution)",
            "serving": "Low-latency multi-modal inference",
            "metrics": "Watch time, completion rate, user retention"
        },
        "key_components": [
            "Video Understanding (frame-level embeddings)",
            "Audio Understanding (music/sound embeddings)",
            "Text Understanding (captions, hashtags)",
            "Two-Tower Model (user tower + video tower)",
            "Candidate Retrieval (ANN search)",
            "Ranking Model (watch time prediction)",
            "Trending Detection System",
            "Creator Recommendation Engine",
            "Real-time Feature Pipeline",
            "A/B Testing for Reels"
        ],
        "tags": ["recommendation", "multi-modal", "video", "meta", "instagram", "reels", "cold-start"]
    },
    {
        "title": "Design Real-time Ad Targeting & Ranking System",
        "difficulty": "hard",
        "description": "Design Meta's ad targeting and ranking system that serves personalized ads to 3B+ users, generating $100B+ annual revenue while balancing user experience.",
        "scenario": """Meta's ad system is critical infrastructure generating $100B+ revenue. The ML system must:
- Target: Find right users for each ad campaign (audience selection)
- Rank: Order ads by expected value (bid × pCTR × pConversion)
- Auction: Run real-time ad auction for each impression
- Budget: Manage advertiser budgets and pacing
- Quality: Maintain user experience (not too many ads)
- Privacy: Work with limited data (iOS privacy, GDPR)
- Scale: Billions of users, millions of advertisers, trillions of impressions

Revenue equation: eCPM = bid × pCTR × pConversion
Goal: Maximize revenue while maintaining user satisfaction.""",
        "requirements": [
            "Real-time ad auction (<50ms per impression)",
            "Predict CTR (click-through rate)",
            "Predict conversion probability",
            "Budget pacing (spend advertiser budgets evenly)",
            "Audience targeting (find right users for ads)",
            "Frequency capping (don't show same ad too much)",
            "Ad quality scoring (prevent low-quality ads)",
            "Privacy-preserving (limited tracking)",
            "Handle billions of users, millions of advertisers",
            "Revenue optimization vs user experience"
        ],
        "evaluation_criteria": {
            "auction_mechanism": "Second-price auction, VCG, or generalized second price",
            "pCTR_model": "Model for click prediction",
            "pConversion_model": "Model for conversion prediction",
            "targeting": "How to match ads to users",
            "budget_pacing": "Algorithm to spend budgets over time",
            "calibration": "Are predicted probabilities accurate?",
            "privacy": "How to work with limited data",
            "revenue_metrics": "eCPM, revenue lift, advertiser ROI"
        },
        "key_components": [
            "Ad Retrieval (find candidate ads)",
            "CTR Prediction Model",
            "Conversion Prediction Model",
            "Ad Auction System",
            "Budget Pacing Algorithm",
            "Frequency Capping",
            "Ad Quality Classifier",
            "Targeting Engine (lookalike audiences)",
            "Attribution System (track conversions)",
            "Real-time Bidding Infrastructure"
        ],
        "tags": ["ads", "ranking", "auction", "revenue", "meta", "ctr-prediction", "conversion"]
    },
    {
        "title": "Design AI Content Moderation System for Meta",
        "difficulty": "hard",
        "description": "Design Meta's content moderation system that detects and removes harmful content (hate speech, violence, spam, misinformation) across Facebook, Instagram, WhatsApp at scale.",
        "scenario": """Meta's content moderation is critical for platform safety. The system must:
- Detect multiple violation types: hate speech, violence, nudity, spam, misinformation, bullying
- Multi-modal: text, images, videos, audio
- Real-time: flag content within seconds
- Multi-language: 100+ languages
- Precision is critical: false positives remove legitimate content
- Recall is critical: false negatives allow harmful content
- Human review: queue borderline content for human moderators
- Adversarial: bad actors constantly try to evade detection
- Scale: billions of posts/day

This is a high-stakes system with regulatory, legal, and ethical implications.""",
        "requirements": [
            "Multi-modal detection (text, image, video, audio)",
            "Real-time inference (<1s for text, <10s for video)",
            "Multi-class: hate speech, violence, nudity, spam, etc.",
            "Multi-language support (100+ languages)",
            "High precision (>95%) to avoid removing legitimate content",
            "High recall (>98%) for severe violations",
            "Human-in-the-loop for borderline cases",
            "Explainability for appeals",
            "Adversarial robustness",
            "Regional policy differences"
        ],
        "evaluation_criteria": {
            "model_architecture": "Multi-modal models (CLIP, ViT, transformers)",
            "data_pipeline": "How to get labeled data (human labeling, active learning)",
            "precision_recall": "Strategy to balance false positives vs false negatives",
            "adversarial": "Handling adversarial attacks (typos, obfuscation)",
            "human_loop": "Queue design, reviewer workflow",
            "explainability": "SHAP, attention, or rule-based explanations",
            "scaling": "Distributed inference for billions of items",
            "metrics": "Precision, recall, proactive rate, human review queue size"
        },
        "key_components": [
            "Text Classification (hate speech, spam)",
            "Image Classification (nudity, violence)",
            "Video Understanding (frame + audio analysis)",
            "Multi-modal Fusion",
            "Human Review Queue",
            "Active Learning Pipeline",
            "Adversarial Detection",
            "Explanation Generator",
            "Appeal System",
            "Policy Engine (region-specific rules)"
        ],
        "tags": ["content-moderation", "classification", "multi-modal", "safety", "meta", "nlp", "computer-vision"]
    },
    {
        "title": "Design Spam Detection System for Messaging",
        "difficulty": "medium",
        "description": "Design a real-time spam detection system for Meta Messenger/WhatsApp that identifies and blocks spam, scams, and phishing at scale while preserving user privacy.",
        "scenario": """Meta's messaging platforms (Messenger, WhatsApp, Instagram DMs) need spam detection:
- Billions of messages daily
- Real-time detection (<100ms)
- Privacy: End-to-end encrypted (WhatsApp)
- Multi-type: spam, scams, phishing, malware links
- Low false positive rate (legitimate messages blocked)
- Handle adversarial attackers (constantly evolving tactics)
- Multi-language support
- On-device ML (for encrypted messages)

Challenge: Balance spam detection with privacy (can't read WhatsApp messages).""",
        "requirements": [
            "Real-time detection (<100ms per message)",
            "Privacy-preserving (work with encrypted messages)",
            "Multi-type: spam, scams, phishing, malware",
            "Low false positive rate (<0.1%)",
            "High recall for dangerous scams (>95%)",
            "On-device models (for WhatsApp)",
            "Handle text, images, links, files",
            "Adversarial robustness",
            "Multi-language support",
            "Scale to billions of messages/day"
        ],
        "evaluation_criteria": {
            "privacy": "How to detect spam without reading content",
            "on_device": "Lightweight models for mobile devices",
            "features": "Metadata vs content features",
            "adversarial": "Handling typos, obfuscation, zero-day attacks",
            "false_positives": "Strategy to minimize blocking legitimate messages",
            "link_scanning": "Detecting malicious URLs",
            "user_reports": "Incorporating user feedback",
            "metrics": "Precision, recall, proactive detection rate"
        },
        "key_components": [
            "Message Classifier (spam vs ham)",
            "URL Scanner (malware/phishing detection)",
            "Image OCR + Classification",
            "Behavioral Signals (message patterns)",
            "On-device Model (for WhatsApp)",
            "Server-side Model (for Messenger)",
            "User Report System",
            "Challenge Flows (CAPTCHA for suspected spam)",
            "Adversarial Detection",
            "Feedback Loop"
        ],
        "tags": ["spam-detection", "classification", "privacy", "meta", "messaging", "adversarial"]
    },
    {
        "title": "Design A/B Testing Platform for ML Experiments",
        "difficulty": "medium",
        "description": "Design Meta/Atlassian's ML experimentation platform that enables safe, fast, statistically rigorous A/B testing of ML models in production.",
        "scenario": """Large tech companies run thousands of A/B tests. The platform must:
- Enable data scientists to run ML experiments easily
- Random assignment (users to treatment/control)
- Metric computation (online + offline metrics)
- Statistical testing (p-values, confidence intervals)
- Heterogeneous treatment effects (does it work for all users?)
- Interference handling (network effects, spillover)
- Multi-armed bandits (explore/exploit)
- Staged rollouts (1% → 10% → 100%)
- Automated monitoring (metric guardrails)

Meta runs 1000s of experiments concurrently. Atlassian tests product changes.""",
        "requirements": [
            "Support 1000s of concurrent experiments",
            "Random assignment with stratification",
            "Real-time metric computation",
            "Statistical testing (t-test, bootstrap)",
            "Heterogeneous treatment effects",
            "Network effect handling",
            "Multi-armed bandits",
            "Automated rollout (gradual)",
            "Metric guardrails (auto-disable bad experiments)",
            "Experiment analysis dashboard"
        ],
        "evaluation_criteria": {
            "randomization": "Proper random assignment, avoiding bias",
            "metrics": "How to compute online and offline metrics",
            "statistics": "Statistical rigor, multiple testing correction",
            "interference": "Handling network effects, spillover",
            "bandits": "Explore/exploit strategies",
            "infrastructure": "Scalable, low-latency",
            "usability": "Easy for data scientists to use",
            "safety": "Guardrails to prevent bad launches"
        },
        "key_components": [
            "Randomization Service",
            "Experiment Configuration System",
            "Metric Computation Pipeline",
            "Statistical Testing Engine",
            "Bandit Algorithm",
            "Staged Rollout Controller",
            "Metric Guardrails",
            "Experiment Dashboard",
            "Heterogeneous Treatment Effect Analysis",
            "Interference Detection"
        ],
        "tags": ["ab-testing", "experimentation", "infrastructure", "statistics", "meta", "atlassian"]
    },
    {
        "title": "Design Search Ranking for Atlassian Products",
        "difficulty": "medium",
        "description": "Design an ML-powered search system for Atlassian products (Jira, Confluence) that helps users find relevant issues, pages, and projects using natural language queries.",
        "scenario": """Atlassian's products (Jira, Confluence) have extensive search needs:
- Jira: Search issues, projects, filters, boards
- Confluence: Search pages, spaces, attachments, comments
- Cross-product search: Find related items across products
- Natural language: Understand user intent (\"bugs from last sprint about login\")
- Personalization: Rank based on user's role, projects, history
- Structured data (Jira fields) + unstructured data (Confluence pages)
- Enterprise scale: 100K+ issues, 50K+ pages per workspace
- Permission-aware (only show what user can access)

Key: Work with limited data (Atlassian is B2B, not consumer scale like Google).""",
        "requirements": [
            "Natural language query understanding",
            "Multi-source search (Jira, Confluence, comments, attachments)",
            "Semantic search (beyond keyword matching)",
            "Personalized ranking",
            "Permission-aware results",
            "Sub-second latency",
            "Handle structured + unstructured data",
            "Cross-product search",
            "Auto-complete and suggestions",
            "Work with limited data (B2B, not web-scale)"
        ],
        "evaluation_criteria": {
            "query_understanding": "NLP for intent extraction, entity recognition",
            "semantic_search": "Embeddings for semantic similarity",
            "ranking": "Learning-to-rank with personalization",
            "indexing": "Efficient indexing for mixed data types",
            "permissions": "Secure, fast permission filtering",
            "personalization": "User context, project access, search history",
            "limited_data": "How to work with limited training data",
            "metrics": "Search success rate, CTR, time to find"
        },
        "key_components": [
            "Query Parser (NLP, intent classification)",
            "Document Indexing (Elasticsearch)",
            "Semantic Embedding Models (sentence transformers)",
            "Hybrid Search (keyword + semantic)",
            "Ranking Model (LambdaMART or neural ranker)",
            "Permission Filter",
            "Personalization Layer",
            "Auto-complete Service",
            "Cross-product Aggregator",
            "Click-through Rate Tracker"
        ],
        "tags": ["search", "ranking", "nlp", "semantic-search", "atlassian", "enterprise", "jira", "confluence"]
    },
    {
        "title": "Design Real-time Fraud Detection System",
        "difficulty": "hard",
        "description": "Design a real-time fraud detection system for Meta's payment products (Meta Pay, WhatsApp Pay) that identifies fraudulent transactions with <100ms latency.",
        "scenario": """Meta's payment products need fraud detection:
- Real-time: Score transactions in <100ms
- Multi-type fraud: stolen cards, account takeover, fake accounts, money laundering
- Class imbalance: fraud rate <1%
- False positives are costly: block legitimate transactions
- False negatives are costly: allow fraud, chargebacks
- Adversarial: fraudsters constantly adapt
- Explainability: Why was this transaction blocked?
- Regulatory compliance: PCI-DSS, AML, KYC

The system processes millions of transactions daily, losing millions to fraud if ineffective.""",
        "requirements": [
            "Real-time scoring (<100ms per transaction)",
            "Multi-type fraud detection",
            "High recall for fraud (>90%)",
            "Low false positive rate (<2%)",
            "Handle severe class imbalance (<1% fraud)",
            "Adversarial robustness",
            "Explainability for compliance",
            "Online learning (adapt to new fraud patterns)",
            "Scale to millions of transactions/day",
            "Multi-stage: real-time → post-transaction analysis"
        ],
        "evaluation_criteria": {
            "model": "Gradient boosting, neural networks, or ensemble",
            "features": "Transaction, user, device, behavioral features",
            "imbalance": "Handling class imbalance (SMOTE, class weights)",
            "adversarial": "Detecting novel fraud patterns",
            "latency": "Sub-100ms inference",
            "explainability": "SHAP, rule-based explanations",
            "online_learning": "Continuous model updates",
            "metrics": "Precision, recall, F1, fraud loss, false positive rate"
        },
        "key_components": [
            "Real-time Transaction Scorer",
            "Feature Engineering Pipeline",
            "Fraud Detection Model (GBDT or NN)",
            "Rule Engine (known fraud patterns)",
            "Anomaly Detector (novel fraud)",
            "Device Fingerprinting",
            "Behavioral Analytics (velocity checks)",
            "Post-transaction Analysis",
            "Explainability Module",
            "Feedback Loop (confirmed fraud cases)"
        ],
        "tags": ["fraud-detection", "classification", "real-time", "payments", "meta", "imbalanced-data"]
    },
    {
        "title": "Design Video Understanding System for Meta",
        "difficulty": "hard",
        "description": "Design Meta's video understanding system that analyzes billions of videos to enable search, recommendations, content moderation, and monetization.",
        "scenario": """Meta processes billions of videos (Facebook, Instagram, Reels, Stories). The system must:
- Understand video content: objects, actions, scenes, audio, text
- Enable video search (\"find videos of surfing in Hawaii\")
- Power recommendations (similar videos)
- Content moderation (detect violations)
- Ad placement (find ad-safe content)
- Thumbnail selection (pick engaging frame)
- Auto-captions (accessibility)
- Copyright detection (match against known content)

Challenge: Video processing is expensive (compute, storage). Need efficient models.""",
        "requirements": [
            "Multi-modal understanding (visual, audio, text)",
            "Scale to billions of videos",
            "Real-time for short videos (<10s)",
            "Batch processing for long videos",
            "Frame-level analysis (scene detection)",
            "Audio understanding (speech, music, sounds)",
            "Text extraction (OCR on video)",
            "Efficient inference (cost-effective)",
            "Enable search, recommendations, moderation",
            "Copyright detection"
        ],
        "evaluation_criteria": {
            "model_architecture": "Video transformers, 3D CNNs, or frame sampling",
            "multi_modal": "How to fuse visual, audio, text signals",
            "efficiency": "Cost-effective processing at scale",
            "embeddings": "Quality of video embeddings for search/recommendations",
            "scene_detection": "Identifying scene boundaries",
            "audio_processing": "Speech recognition, music detection",
            "ocr": "Text extraction from video frames",
            "metrics": "Video search quality, recommendation CTR, moderation accuracy"
        },
        "key_components": [
            "Video Encoder (frame embeddings)",
            "Audio Encoder (audio embeddings)",
            "Text Encoder (captions, OCR)",
            "Multi-modal Fusion",
            "Scene Detection",
            "Object/Action Recognition",
            "Speech-to-Text",
            "Thumbnail Selector",
            "Copyright Matcher",
            "Video Search Index"
        ],
        "tags": ["video-understanding", "multi-modal", "computer-vision", "meta", "reels", "deep-learning"]
    },
    {
        "title": "Design Real-time Personalization Engine",
        "difficulty": "medium",
        "description": "Design a real-time personalization system that adapts Meta/Atlassian products to individual users based on their behavior, preferences, and context.",
        "scenario": """Modern products need personalization at scale:
- Meta: Personalize Feed, Reels, notifications, ads
- Atlassian: Personalize Jira dashboards, Confluence recommendations
- Real-time: Update preferences as user interacts
- Cold start: New users have no history
- Context: Time of day, device, location matter
- Privacy: Limited data collection
- Scale: Billions of users
- Latency: <50ms per request

Goal: Show the right content to the right user at the right time.""",
        "requirements": [
            "Real-time preference updates (<50ms)",
            "Handle billions of users",
            "Cold start for new users",
            "Context-aware (time, device, location)",
            "Privacy-preserving",
            "Multi-product personalization",
            "Efficient user representation (embeddings)",
            "Online learning (user preferences change)",
            "A/B testing integration",
            "Explainability (why this recommendation?)"
        ],
        "evaluation_criteria": {
            "user_modeling": "How to represent users (embeddings, features)",
            "real_time": "Low-latency updates and inference",
            "cold_start": "Strategy for new users",
            "context": "Incorporating temporal, device, location signals",
            "online_learning": "Continuous preference updates",
            "privacy": "Working with limited data",
            "scalability": "Handling billions of users efficiently",
            "metrics": "Engagement lift, user satisfaction, CTR"
        },
        "key_components": [
            "User Profile Store (preferences, embeddings)",
            "Real-time Event Stream (user actions)",
            "User Embedding Model",
            "Context Feature Service",
            "Personalization API",
            "Cold Start Solver",
            "Online Learning Pipeline",
            "A/B Testing Integration",
            "Privacy Controls",
            "Explainability Module"
        ],
        "tags": ["personalization", "user-modeling", "real-time", "meta", "atlassian", "recommendations"]
    }
]
