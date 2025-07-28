# Language Learning Game Prompts
# This file contains all prompts used in the application for easy management and iteration

# ============================================================================
# BINARY FEEDBACK PROMPTS
# ============================================================================

BINARY_FEEDBACK_PROMPT = """
Check if the user's guess is correct for the {language} word '{word}'.

User's guess: '{guess}'

Requirements:
- Return ONLY "correct" or "incorrect"
- "correct" if the guess means the same thing as the target word
- "incorrect" if the guess is wrong or only partially right
- Be generous with synonyms and common translations
- For nouns, accept the English translation as correct

Examples:
- "umbrella" for "paraguas" = correct
- "fridge" for "refrigerador" = correct  
- "bike" for "bicicleta" = correct
- "rain protection" for "paraguas" = incorrect
- "car" for "bicicleta" = incorrect

Return only: correct OR incorrect
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
