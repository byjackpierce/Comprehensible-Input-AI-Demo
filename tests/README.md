# Tests

AI prompt engineering and parameter testing for the language learning game.

## Files

### `test_temperature.py`
Tests temperature effects on word generation (0.1-1.0).

**Results**: Temperature 0.7-0.8 gives best variety for learning vocabulary.

### Historical Tests

See `tests/archive/` for historical test files that demonstrate the evolution from single-sentence generation to the current progressive sentence generation system.

**Archived files:**
- `test_sentence_generation_diverse.py` - Original single sentence generation tests
- `test_sentence_temperature.py` - Original temperature testing for single sentences

**Evolution documented in:** `tests/archive/README.md`

### `test_progressive_sentence_generation.py`
Tests 5-sentence progressive difficulty sequences with strategic context planning.

**Words tested**: 10 diverse words (German, Spanish, English)
**Sentences per word**: 5 with progressive difficulty (subtle → obvious)
**Languages**: German, Spanish, English (rare words)

**Results**:
- ✅ **Excellent**: Progressive difficulty maintained across all words
- ✅ **Good**: Diverse contexts (work → home → social → nature → travel)
- ✅ **Good**: Natural sentence quality with strategic planning
- ✅ **Good**: No overly obvious final sentences
- 🔧 **Implemented**: Progressive sentence generation system in main app

### `test_presence_penalty_variations.py`
Tests presence penalty effects on context diversity across 4 configurations.

**Words tested**: 4 words (3 Spanish, 1 German)
**Configurations**: Low (0.0), Medium (0.3), High (0.6), Balanced (0.2 freq + 0.3 pres)
**Focus**: Context diversity analysis

**Results**:
- ✅ **High Presence Penalty (0.6)**: Maximum context diversity
- ✅ **Medium Presence Penalty (0.3)**: Good balance of diversity and quality
- ✅ **Low Presence Penalty (0.0)**: Repetitive contexts (work → work → work)
- 🔧 **Optimized**: Implemented presence penalty 0.4 for optimal balance
- 📊 **Analysis**: Context diversity dramatically improved with presence penalty

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
python tests/test_progressive_sentence_generation.py
python tests/test_presence_penalty_variations.py
python tests/test_scoring.py
```

## Historical Tests

```bash
# These are archived and will fail (for reference only):
python tests/archive/test_sentence_generation_diverse.py
python tests/archive/test_sentence_temperature.py
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

### Progressive Sentence Generation
- **Presence Penalty 0.4**: Optimal for context diversity
- **Progressive Difficulty**: Subtle → obvious maintained across all words
- **Context Diversity**: Work → home → social → nature → travel scenarios
- **Quality**: Natural sentences with strategic planning
- **Implementation**: Single API call generates all 5 sentences

### Sentence Generation Quality
- **Weather words**: Excellent context with rain/drizzle scenarios
- **Transportation**: Good context with riding/cycling activities  
- **Lighting tools**: Clear context with darkness/power outages
- **Household items**: Needs more varied scenarios (cooking, meal prep)
- **Clothing**: Inconsistent context (sports vs weather scenarios)

### Presence Penalty Analysis
- **Low (0.0)**: Repetitive contexts, poor diversity
- **Medium (0.3)**: Good balance, natural quality
- **High (0.6)**: Maximum diversity, slight quality trade-off
- **Optimal (0.4)**: Best balance of diversity and quality

### Scoring System Quality
- **Status**: **ARCHIVED** - Moved to archive/scoring-system branch
- **New approach**: Binary feedback (correct/incorrect) for cleaner user experience
- **Focus**: Nouns with one-to-one mapping for MVP
