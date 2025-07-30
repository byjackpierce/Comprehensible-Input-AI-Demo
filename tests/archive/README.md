# Archive - Historical Tests

This directory contains historical test files that demonstrate the evolution of the language learning system.

## Evolution Timeline

### Phase 1: Single Sentence Generation (Archived)
**Files:**
- `test_sentence_generation_diverse.py` - Tests single sentence generation across languages
- `test_sentence_temperature.py` - Tests temperature effects on single sentences

**Approach:**
- Generated one sentence at a time
- Used `generate_sentence_with_word()` method
- Called `/api/generate-sentence/` endpoint
- Progressive disclosure UX (wait between sentences)

**Issues Identified:**
- Repetitive contexts for specific words
- Slower UX (5 API calls instead of 1)
- No strategic planning of sentence sequence
- Limited context diversity

### Phase 2: Progressive Sentence Generation (Current)
**Files:**
- `test_progressive_sentence_generation.py` - Tests 5-sentence sequences
- `test_presence_penalty_variations.py` - Tests context diversity optimization

**Approach:**
- Generates all 5 sentences in one API call
- Uses `generate_progressive_sentence_sequence()` method
- Calls `/api/generate-sentence-sequence/` endpoint
- Strategic difficulty progression (subtle → obvious)
- Presence penalty (0.4) for context diversity

**Improvements:**
- ✅ Better context diversity (work → home → social → nature → travel)
- ✅ Faster UX (one API call)
- ✅ Strategic sentence planning
- ✅ Progressive difficulty maintained
- ✅ Enhanced learning experience

## Technical Changes

### Removed Methods
- `generate_sentence_with_word()` - Replaced by `generate_progressive_sentence_sequence()`
- `SENTENCE_GENERATION_PROMPT` - Replaced by `PROGRESSIVE_SENTENCE_SEQUENCE_PROMPT`

### Removed Endpoints
- `/api/generate-sentence/` - Replaced by `/api/generate-sentence-sequence/`

### Added Features
- Presence penalty (0.4) for context diversity
- Progressive difficulty structure
- Strategic sentence planning
- Enhanced fallback handling

## Running Historical Tests

⚠️ **Note:** These tests will fail because they reference removed methods.

```bash
# These will fail but show the historical approach:
python tests/archive/test_sentence_generation_diverse.py
python tests/archive/test_sentence_temperature.py
```

## Current Active Tests

```bash
# Current progressive sentence generation tests:
python tests/test_progressive_sentence_generation.py
python tests/test_presence_penalty_variations.py
```

## Lessons Learned

1. **Context Diversity**: Presence penalty dramatically improves learning experience
2. **Strategic Planning**: Generating all sentences at once enables better sequence design
3. **Progressive Difficulty**: Subtle → obvious progression enhances learning
4. **Performance**: Single API call is much faster than multiple calls
5. **User Experience**: Diverse contexts keep learners engaged

This archive serves as documentation of the system's evolution and the decision-making process behind the improvements. 