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
# PROGRESSIVE SENTENCE SEQUENCE PROMPTS
# ============================================================================

PROGRESSIVE_SENTENCE_SEQUENCE_PROMPT = """
Generate 5 English sentences that use the {language} word '{word}' in context, with PROGRESSIVE DIFFICULTY.

Requirements:
- Use '{word}' naturally in each sentence
- ALWAYS write the foreign word in lowercase
- Create PROGRESSIVE DIFFICULTY: start subtle/hard, end obvious/easy
- Each sentence should provide different context clues
- Make sentences progressively more obvious about what '{word}' means
- Return exactly 5 sentences, one per line, numbered 1-5

PROGRESSIVE DIFFICULTY STRUCTURE:
1. Sentence 1: Very subtle, minimal clues, requires deep thinking
2. Sentence 2: Slightly more context, but still challenging
3. Sentence 3: Moderate clues, getting clearer
4. Sentence 4: More obvious context, easier to guess
5. Sentence 5: Additional context, but still requires thinking (not obvious)

Examples for "kofferraum" (car trunk):
1. "The kofferraum was packed with camping gear for the weekend trip."
2. "She loaded the groceries into the kofferraum before driving home."
3. "The rental car's kofferraum was surprisingly spacious for all our luggage."
4. "He stored his suitcase in the kofferraum of the car before the airport trip."
5. "The kofferraum contained emergency supplies and a spare tire."

IMPORTANT: The foreign word must appear in lowercase in all sentences.
Return exactly 5 sentences, numbered 1-5, one per line.
"""
