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
- Be STRICT: only accept exact translations or very close synonyms
- "correct" ONLY if the guess is a direct translation or very close synonym
- "incorrect" for partial matches, related words, or approximate translations
- For nouns, only accept the most common English translation

Examples:
- "umbrella" for "paraguas" = correct
- "rain protection" for "paraguas" = incorrect (too vague)
- "bike" for "bicicleta" = correct
- "vehicle" for "bicicleta" = incorrect (too general)
- "fridge" for "refrigerador" = correct
- "cooling device" for "refrigerador" = incorrect (too descriptive)

Return only: correct OR incorrect
"""

# ============================================================================
# WORD GENERATION PROMPTS
# ============================================================================

WORD_GENERATION_PROMPT = """
Generate {count} advanced-level nouns in {language} that are completely different from English equivalents.

Requirements:
- Choose words that have NO obvious English cognates or similarities
- Focus on words that require multiple contexts to understand their meaning
- Select words that are common in daily life but not immediately guessable
- Return ONLY the words, one per line, no numbers, no punctuation, no dashes
- No translations or explanations

Examples of good advanced words (completely different from English):
German: Wolldecke, Schreibtisch, Mikrowelle, Teelöffel, Büroklammer, Spiegel
Spanish: mantel, escritorio, microondas, cucharilla, clip, espejo

AVOID completely: Auto, Haus, Buch, Hund, Katze, Tisch, Stuhl - too obvious
PREFER words that: require context clues, have no English similarity, need multiple sentences to understand

FORMAT: Return only the words, one per line, no dashes, no bullets, no numbers.
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
