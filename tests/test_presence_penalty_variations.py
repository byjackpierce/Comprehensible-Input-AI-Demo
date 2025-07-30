import sys
import os
# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.ai_service import AIService

def test_presence_penalty_variations():
    ai_service = AIService()

    # Test words: 3 Spanish, 1 German
    test_words = [
        {"word": "pantano", "language": "Spanish"},
        {"word": "colina", "language": "Spanish"},
        {"word": "zancudo", "language": "Spanish"},
        {"word": "Schlafmütze", "language": "German"},
    ]

    # Test configurations focusing on presence penalty
    configurations = [
        {
            "name": "Low Presence Penalty (Baseline)",
            "temp": 1.2,
            "top_p": 0.9,
            "freq_penalty": 0.0,
            "presence_penalty": 0.0
        },
        {
            "name": "Medium Presence Penalty (Target)",
            "temp": 1.2,
            "top_p": 0.9,
            "freq_penalty": 0.0,
            "presence_penalty": 0.3
        },
        {
            "name": "High Presence Penalty (Max Diversity)",
            "temp": 1.2,
            "top_p": 0.9,
            "freq_penalty": 0.0,
            "presence_penalty": 0.6
        },
        {
            "name": "Balanced with Frequency Penalty",
            "temp": 1.2,
            "top_p": 0.9,
            "freq_penalty": 0.2,
            "presence_penalty": 0.3
        }
    ]

    print(f"🧪 PRESENCE PENALTY VARIATION TESTING")
    print(f"Testing context diversity with different presence penalty values")
    print(f"Words: {len(test_words)} | Configurations: {len(configurations)}")
    print("="*80)

    for config in configurations:
        print(f"\n📊 CONFIGURATION: {config['name']}")
        print(f"Temperature: {config['temp']} | Top_p: {config['top_p']}")
        print(f"Frequency Penalty: {config['freq_penalty']} | Presence Penalty: {config['presence_penalty']}")
        print("="*80)

        for i, test_case in enumerate(test_words, 1):
            word = test_case["word"]
            language = test_case["language"]
            
            print(f"\n{i}. {language} - '{word}'")
            print("-" * 50)
            
            try:
                # Generate sentences with specific configuration
                sentences = generate_sentences_with_config(
                    ai_service, word, language, config
                )
                
                if sentences and len(sentences) == 5:
                    print(f"✅ Generated {len(sentences)} sentences")
                    print()
                    
                    # Display sentences with context analysis
                    for j, sentence in enumerate(sentences, 1):
                        context = analyze_context(sentence, word)
                        print(f"{j}. {context}")
                        print(f"   '{sentence}'")
                        print()
                        
                else:
                    print(f"❌ Error: Generated {len(sentences) if sentences else 0} sentences")
                    
            except Exception as e:
                print(f"❌ Error: {str(e)}")
                print()
            
            if i < len(test_words):
                print("-" * 40)

def generate_sentences_with_config(ai_service, word, language, config):
    """Generate sentences with specific configuration parameters"""
    
    # Create a custom prompt that includes the configuration
    prompt = f"""Generate 5 English sentences that use the {language} word '{word}' in context, with PROGRESSIVE DIFFICULTY.

Requirements:
- Use '{word}' naturally in each sentence
- ALWAYS write the foreign word in lowercase
- Create PROGRESSIVE DIFFICULTY: start subtle/hard, end easier but still challenging
- Each sentence should provide DIFFERENT context clues and scenarios
- Make sentences progressively more obvious about what '{word}' means
- Focus on CONTEXT DIVERSITY: different settings, situations, and scenarios
- Return exactly 5 sentences, one per line, numbered 1-5

PROGRESSIVE DIFFICULTY STRUCTURE:
1. Sentence 1: Very subtle, minimal clues, requires deep thinking
2. Sentence 2: Slightly more context, but still challenging
3. Sentence 3: Moderate clues, getting clearer
4. Sentence 4: More obvious context, easier to guess
5. Sentence 5: Additional context, but still requires thinking (not obvious)

IMPORTANT: The foreign word must appear in lowercase in all sentences.
Return exactly 5 sentences, numbered 1-5, one per line."""

    try:
        response = ai_service.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=config['temp'],
            top_p=config['top_p'],
            frequency_penalty=config['freq_penalty'],
            presence_penalty=config['presence_penalty']
        )
        
        content = response.choices[0].message.content
        if not content:
            return []
        
        # Parse the numbered sentences
        sentences = []
        lines = content.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if line and any(line.startswith(str(i)) for i in range(1, 6)):
                # Remove the number and any following punctuation
                sentence = line.split('.', 1)[-1].split(' ', 1)[-1].strip()
                if sentence:
                    sentences.append(sentence)
        
        return sentences[:5]  # Return exactly 5 sentences
        
    except Exception as e:
        print(f"Error in generation: {str(e)}")
        return []

def analyze_context(sentence, target_word):
    """Analyze the context of a sentence"""
    sentence_lower = sentence.lower()
    
    # Context categories
    contexts = {
        "work/office": ["work", "office", "meeting", "desk", "job", "business"],
        "home/family": ["home", "family", "house", "room", "bed", "kitchen"],
        "social/leisure": ["party", "friends", "social", "leisure", "entertainment"],
        "nature/outdoor": ["forest", "garden", "outdoor", "nature", "park", "beach"],
        "travel/transport": ["travel", "car", "trip", "journey", "transport"],
        "morning/routine": ["morning", "breakfast", "alarm", "wake", "routine"],
        "weather/environment": ["rain", "weather", "climate", "environment", "air"],
        "emotion/feeling": ["feel", "emotion", "mood", "feeling", "sense"]
    }
    
    # Find matching contexts
    found_contexts = []
    for context_name, keywords in contexts.items():
        if any(keyword in sentence_lower for keyword in keywords):
            found_contexts.append(context_name)
    
    if found_contexts:
        return f"Context: {', '.join(found_contexts)}"
    else:
        return "Context: General/Other"

def test_context_diversity_analysis():
    """Additional test to analyze context diversity across configurations"""
    print(f"\n📈 CONTEXT DIVERSITY ANALYSIS")
    print("="*80)
    
    # This would analyze how diverse the contexts are across different configurations
    # For now, just a placeholder for future analysis
    print("Context diversity analysis would go here...")

if __name__ == "__main__":
    # Run the main presence penalty variation test
    test_presence_penalty_variations()
    
    # Run the context diversity analysis
    test_context_diversity_analysis()
    
    print(f"\n✅ Testing complete!")
    print(f"Check the output above to see how presence penalty affects context diversity.") 