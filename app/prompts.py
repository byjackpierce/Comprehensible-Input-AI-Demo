# Language Learning Game Prompts
# This file contains all prompts used in the application for easy management and iteration

# ============================================================================
# SCORING PROMPTS
# ============================================================================

SCORING_SYSTEM_PROMPT = """
You are a supportive and encouraging language learning tutor. Score guesses fairly but generously, like a helpful human teacher would. Focus on understanding and comprehension rather than perfect word matching. Be warm and encouraging in your feedback.
"""

SCORING_USER_PROMPT_TEMPLATE = """
Score this guess for a {language} word on a 0-10 scale.

Target word: '{word}'
User's guess: '{guess}'

Think like a human teacher helping someone learn. The goal is comprehension - if they understand what the word means, that's success!

Scoring approach:
- 0-2: Completely wrong concept (e.g., guessing "banana" for a vehicle part)
- 3-4: Wrong category but some related concept or thinking
- 5-6: Right general area but missing the specific meaning
- 7-8: Very close - they understand the concept but might be missing a nuance
- 9-10: Correct or essentially correct (including English translations!)

Important: If they give the correct English translation, that's a 9-10! The goal is understanding, not memorizing the foreign word.

Be generous with partial credit. If they're in the right ballpark, give them credit. Think "how close are they to understanding this?"

Examples of good scoring:
- "cozy" for "gemütlich" = 9.5/10
Comment: "Cozy" captures the emotional and physical tone well. The only nuance missing is that gemütlich can also include social warmth and a feeling of shared comfort.

- "to notice" for "merken" = 9.5/10
Comment: Correct — that's the core meaning of merken in this context. It refers to mentally registering a change or detail.

- "pulled it" for "heben" = 7/10
Comment: Close — you're in the right domain of physical movement, but heben implies vertical lifting, not pulling horizontally.

- "to sense something" for "merken" = 7/10
Comment: A reasonable guess. "Sensing" gets the emotional feel, but merken is more about noticing or mentally registering something, not intuiting.

- "to feel something" for "merken" = 6.5/10
Comment: Off-target — "feel" implies physical sensation. Merken is about awareness or noticing, not tactile perception.

Provide a score and ONE SHORT encouraging sentence explaining why, without revealing the answer.

Format your response exactly like this:
SCORE: [number]/10
FEEDBACK: [one encouraging sentence]
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
- Use '{word}' naturally in an English sentence
- ALWAYS write the foreign word in lowercase, regardless of position in sentence
- Provide clear context clues about what '{word}' means
- Make it appropriate for language learning
- Return only the sentence, nothing else
- Ensure the sentence gives helpful context without being too obvious

IMPORTANT: The foreign word must appear in lowercase, even if it's at the beginning of a sentence or is normally capitalized in its original language.

Example format: "She opened the kofferraum and loaded her groceries."
Example format: "kofferraum is where we store our luggage in the car."
"""
