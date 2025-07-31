# Comprehensible Input Project - Skills Tracking

## Project Overview
Language learning game using progressive sentence sequences to teach foreign words.

## Skills Usage

### ✅ Heavy Usage
**API integration + prompt engineering (25%)**
- OpenAI API integration, sophisticated prompts
- Learned: Binary classification needs low temp (0.05), creative generation needs high temp (1.2-1.5)
- Next: Add few-shot learning, prompt versioning

**Full-stack integration (10%)**
- Flask backend, JavaScript frontend, async/await
- Learned: Loading states improve UX significantly
- Next: Migrate to FastAPI, add WebSocket support

### 🔄 Basic Usage
**Evaluation mindset (10%)**
- Basic error handling, fallback responses
- Learned: Graceful degradation is crucial
- Next: Add comprehensive logging, A/B testing

**Model literacy (7%)**
- Token limits, temperature/top_p tuning
- Learned: Different tasks need different settings
- Next: Study tokenization, optimize cost vs quality

### ❌ Not Yet Used
**RAG fundamentals (20%)** - Plan: Create word database with embeddings
**Tooling fluency (15%)** - Plan: Migrate to LangChain
**Open-source models (8%)** - Plan: Test with Ollama
**AI safety (5%)** - Plan: Add content filtering

## Key Learnings
- Prompt engineering is crucial - small changes have big impacts
- Error handling matters - users need clear feedback
- Parameter tuning is an art - different tasks need different settings

## Next Steps
1. Add RAG for word selection
2. Migrate to LangChain
3. Deploy to production
4. Add evaluation metrics 