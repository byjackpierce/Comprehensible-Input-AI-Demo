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
# ENHANCED FEEDBACK PROMPTS
# ============================================================================

NATURAL_TRANSLATION_PROMPT = """
Provide a natural, detailed translation for the {language} word '{word}'.

Requirements:
- Give the most common, natural English translation
- Include additional context or explanation if helpful
- Make it sound natural and conversational
- Focus on the most accurate translation, not the user's guess
- Do NOT repeat the original word in the response

Examples:
- "Schlüsselbund" → "keychain" (a ring or chain that holds keys together)
- "Regenschirm" → "umbrella" (for protection from rain)
- "Zahnarzt" → "dentist" (a doctor who specializes in teeth)
- "Schlafmütze" → "sleepyhead" (a playful term for someone who is often sleepy)

Return only the natural translation and brief explanation.
"""

DETAILED_FEEDBACK_PROMPT = """
Generate detailed feedback for a language learning game.

Context:
- Language: {language}
- Target word: '{word}'
- User's final guess: '{final_guess}'
- All user guesses: {all_guesses}
- Number of sentences used: {sentence_count}
- Sentences: {sentences}

Requirements:
- Provide encouraging feedback about their learning process
- Comment on their guessing strategy (if they made multiple guesses)
- Give a brief insight about the word or language learning
- Keep it positive and educational
- Make it conversational and engaging
- Include 1-2 sentences maximum

Examples:
- "Great job using context clues! You narrowed it down from 'container' to 'trunk' - that's exactly how native speakers learn new words."
- "You got it in just 2 sentences! This shows how multiple contexts help build understanding quickly."
- "Nice persistence! You went from 'box' to 'storage' to 'trunk' - each guess got closer. That's the learning process in action!"

Return only the feedback message.
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
