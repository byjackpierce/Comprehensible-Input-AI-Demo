# Language Learning Game Prompts
# This file contains all prompts used in the application for easy management and iteration

# ============================================================================
# SCORING PROMPTS
# ============================================================================

SCORING_SYSTEM_PROMPT = """You are a supportive language learning tutor. Score guesses fairly and provide encouraging, helpful feedback without revealing answers. Be consistent in your scoring and always encourage learning progress."""

SCORING_USER_PROMPT_TEMPLATE = """
Score this guess for a {language} word on a 0-10 scale.

Target word: '{word}'
User's guess: '{guess}'

Scoring criteria:
- 0-2: Completely wrong concept (e.g., guessing "banana" for a vehicle part)
- 3-4: Wrong category but some related concept
- 5-6: Right category, wrong specific item (e.g., guessing "cat" for "dog")
- 7-8: Very close, same concept but different word
- 9-10: Correct or essentially correct

Provide a score and ONE SHORT encouraging sentence explaining why, without revealing the answer.

Format your response exactly like this:
SCORE: [number]/10
FEEDBACK: [one sentence explanation]
"""

# ============================================================================
# WORD GENERATION PROMPTS
# ============================================================================

WORD_GENERATION_PROMPT = """
Generate {count} intermediate-level nouns in {language}.

Requirements:
- Choose words that are common but not super basic (avoid: Haus, Auto, Buch, Hund, Katze)
- Focus on more interesting vocabulary like: Kühlschrank, Regenschirm, Handschuh, Fahrrad
- Return ONLY the words, one per line, no numbers or punctuation
- No translations or explanations

Examples of good intermediate words:
- German: Kühlschrank, Regenschirm, Handschuh, Fahrrad, Taschenlampe
- Spanish: paraguas, refrigerador, guante, bicicleta, linterna
"""

# ============================================================================
# SENTENCE GENERATION PROMPTS
# ============================================================================

SENTENCE_GENERATION_PROMPT = """
Generate an English sentence that uses the {language} word '{word}' in context.

Requirements:
- Use '{word}' naturally in an English sentence (keep it lowercase)
- Provide clear context clues about what '{word}' means
- Make it appropriate for language learning
- Return only the sentence, nothing else
- Ensure the sentence gives helpful context without being too obvious
- The foreign word should appear in lowercase, even if it's at the beginning of a sentence

Example format: "She opened the kofferraum and loaded her groceries."
"""

# ============================================================================
# TEST CASES FOR PROMPT ITERATION
# ============================================================================

TEST_CASES = [
    {
        'word': 'Hund',
        'language': 'German', 
        'guess': 'cat',
        'expected_score_range': '5-7',
        'description': 'Right category (animal), wrong specific animal'
    },
    {
        'word': 'Kofferraum',
        'language': 'German',
        'guess': 'closet', 
        'expected_score_range': '4-6',
        'description': 'Right concept (storage), wrong location'
    },
    {
        'word': 'Hund',
        'language': 'German',
        'guess': 'car',
        'expected_score_range': '0-3',
        'description': 'Completely wrong category'
    },
    {
        'word': 'Kofferraum',
        'language': 'German',
        'guess': 'trunk',
        'expected_score_range': '9-10',
        'description': 'Correct answer'
    },
    {
        'word': 'Buch',
        'language': 'German',
        'guess': 'book',
        'expected_score_range': '9-10',
        'description': 'Correct answer'
    }
]

# ============================================================================
# PROMPT VERSIONS FOR A/B TESTING
# ============================================================================

# Alternative scoring prompt (more lenient)
SCORING_PROMPT_LENIENT = """
Score this guess for a {language} word on a 0-10 scale.

Target word: '{word}'
User's guess: '{guess}'

Be generous with partial credit. If they're in the right ballpark, give them credit.

Scoring criteria:
- 0-1: Completely wrong concept
- 2-3: Wrong category but some related concept
- 4-5: Right category, wrong specific item
- 6-7: Very close, same concept but different word
- 8-10: Correct or essentially correct

Format: SCORE: [number]/10\nFEEDBACK: [one encouraging sentence]
"""

# Alternative scoring prompt (more strict)
SCORING_PROMPT_STRICT = """
Score this guess for a {language} word on a 0-10 scale.

Target word: '{word}'
User's guess: '{guess}'

Be precise with scoring. Only give high scores for very close or correct answers.

Scoring criteria:
- 0-2: Completely wrong concept
- 3-4: Wrong category but some related concept
- 5-6: Right category, wrong specific item
- 7-8: Very close, same concept but different word
- 9-10: Correct or essentially correct

Format: SCORE: [number]/10\nFEEDBACK: [one sentence]
""" 