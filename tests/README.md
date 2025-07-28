# Tests

AI prompt engineering and parameter testing for the language learning game.

## Files

### `test_temperature.py`
Tests temperature effects on word generation (0.1-1.0).

**Results**: Temperature 0.7-0.8 gives best variety for learning vocabulary.

### `test_sentence_temperature.py`
Tests temperature effects on sentence generation (1.2-1.8).

**Results**: Temperature 1.2 gives optimal balance of variety and reliability for sentence generation.

### `test_sentence_generation_diverse.py`
Tests sentence generation across multiple languages and word categories.

**Languages tested**: German, Spanish, French, Italian, Portuguese
**Word categories**: Household, Weather, Clothing, Transportation, Tools
**Words per language**: 5 common intermediate-level words
**Tests per word**: 3 sentences per word

**Results**: 
- ✅ **Good**: Weather words (umbrellas), transportation (bikes), lighting (flashlights) get clear context
- ⚠️ **Mixed**: Household items (refrigerators) get repetitive scenarios
- ❌ **Issues**: Inconsistent lowercase usage, some redundancy in scenarios
- 🔧 **Prompt updated**: Enhanced lowercase enforcement in sentence generation prompt

### `test_scoring.py`
Tests AI scoring system for user guesses across different difficulty levels.

**Status**: **ARCHIVED** - Scoring system moved to archive/scoring-system branch
**New approach**: Binary feedback system (correct/incorrect) for nouns MVP

**Language tested**: Spanish (for user comprehension)
**Word categories**: Weather, Household, Transportation, Lighting, Clothing
**Guess types**: Correct translations, close answers, right category/wrong item, wrong category, completely wrong
**Tests per case**: 2 tests per guess to check consistency

**Results**:
- ✅ **Good**: English translations now get 10/10 (umbrella, refrigerator, bicycle, flashlight, glove)
- ✅ **Good**: Abbreviations get proper credit (fridge 9.5/10, bike 9.5/10)
- ✅ **Good**: More generous scoring in 5-9 range with encouraging feedback
- ⚠️ **Issues**: Inconsistent scoring between tests (freezer: 9/10 vs 6/10)
- ❌ **Issues**: Feedback sometimes gives too obvious hints
- 🔧 **Prompt updated**: Enhanced with human teacher examples and comprehension focus

**Note**: Scoring system archived due to pivot to binary feedback approach for nouns MVP

## Run Tests

```bash
python tests/test_temperature.py
python tests/test_sentence_temperature.py
python tests/test_sentence_generation_diverse.py
python tests/test_scoring.py
```

## Notes

### Word Generation
- Temperature 0.1: Too predictable
- Temperature 0.7-0.8: Optimal for learning
- Temperature 1.0: Too random

### Sentence Generation
- Temperature 1.2: Optimal - good variety, reliable, coherent
- Temperature 1.4: Acceptable but some reliability issues
- Temperature 1.6+: Avoid - produces gibberish and nonsense

### Sentence Generation Quality
- **Weather words**: Excellent context with rain/drizzle scenarios
- **Transportation**: Good context with riding/cycling activities  
- **Lighting tools**: Clear context with darkness/power outages
- **Household items**: Needs more varied scenarios (cooking, meal prep)
- **Clothing**: Inconsistent context (sports vs weather scenarios)

### Scoring System Quality
- **Status**: **ARCHIVED** - Moved to archive/scoring-system branch
- **New approach**: Binary feedback (correct/incorrect) for cleaner user experience
- **Focus**: Nouns with one-to-one mapping for MVP
