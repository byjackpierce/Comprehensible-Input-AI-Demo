import sys
import os
# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.ai_service import AIService

def test_progressive_sentence_generation():
    ai_service = AIService()

    # Test cases with diverse words from different languages
    test_cases = [
        # German words
        {"word": "Schlafmütze", "language": "German"},
        {"word": "Gartenzwerg", "language": "German"},
        {"word": "Feinkost", "language": "German"},
        {"word": "Fernweh", "language": "German"},
        
        # Spanish words
        {"word": "pantano", "language": "Spanish"},
        {"word": "colina", "language": "Spanish"},
        {"word": "zancudo", "language": "Spanish"},
        {"word": "trineo", "language": "Spanish"},
        
        # English words (rare/advanced)
        {"word": "aporia", "language": "English"},
        {"word": "susurrus", "language": "English"},
    ]

    print(f"🧪 PROGRESSIVE SENTENCE GENERATION TESTING")
    print(f"Testing 5-sentence sequences with progressive difficulty")
    print(f"Words: {len(test_cases)} | Sentences per word: 5")
    print("="*80)

    for i, test_case in enumerate(test_cases, 1):
        word = test_case["word"]
        language = test_case["language"]
        
        print(f"\n{i:2d}. {language} - '{word}'")
        print("=" * 60)
        
        try:
            # Generate the 5-sentence sequence
            sentences = ai_service.generate_progressive_sentence_sequence(word, language)
            
            if sentences and len(sentences) == 5:
                print(f"✅ Generated {len(sentences)} sentences successfully")
                print()
                
                # Display each sentence with its difficulty level
                difficulty_levels = [
                    "1. Very subtle (requires deep thinking)",
                    "2. Slightly more context (still challenging)",
                    "3. Moderate clues (getting clearer)",
                    "4. More obvious context (easier to guess)",
                    "5. Additional context (still requires thinking)"
                ]
                
                for j, (sentence, difficulty) in enumerate(zip(sentences, difficulty_levels), 1):
                    print(f"{difficulty}")
                    print(f"   '{sentence}'")
                    print()
                    
            else:
                print(f"❌ Error: Generated {len(sentences) if sentences else 0} sentences (expected 5)")
                if sentences:
                    for j, sentence in enumerate(sentences, 1):
                        print(f"   {j}. {sentence}")
                print()
                
        except Exception as e:
            print(f"❌ Error generating sentences for '{word}': {str(e)}")
            print()
        
        # Add a separator between words
        if i < len(test_cases):
            print("-" * 80)

def test_progressive_difficulty_analysis():
    """Additional test to analyze the progressive difficulty"""
    ai_service = AIService()
    
    # Test with a few specific words to analyze difficulty progression
    analysis_words = [
        {"word": "Schlafmütze", "language": "German"},
        {"word": "pantano", "language": "Spanish"},
        {"word": "aporia", "language": "English"},
    ]
    
    print(f"\n�� PROGRESSIVE DIFFICULTY ANALYSIS")
    print(f"Analyzing how difficulty progresses across sentences")
    print("="*80)
    
    for test_case in analysis_words:
        word = test_case["word"]
        language = test_case["language"]
        
        print(f"\n📊 Analysis: {language} - '{word}'")
        print("-" * 50)
        
        try:
            sentences = ai_service.generate_progressive_sentence_sequence(word, language)
            
            if sentences and len(sentences) == 5:
                print("Progressive difficulty analysis:")
                for j, sentence in enumerate(sentences, 1):
                    # Count context clues (words that might help)
                    context_words = len([word for word in sentence.lower().split() 
                                       if word not in ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by']])
                    
                    print(f"  Sentence {j}: {context_words} context words")
                    print(f"    '{sentence}'")
                    print()
            else:
                print(f"❌ Could not analyze - only {len(sentences) if sentences else 0} sentences generated")
                
        except Exception as e:
            print(f"❌ Error in analysis: {str(e)}")

if __name__ == "__main__":
    # Run the main progressive sentence generation test
    test_progressive_sentence_generation()
    
    # Run the difficulty analysis test
    test_progressive_difficulty_analysis()
    
    print(f"\n✅ Testing complete!")
    print(f"Check the output above to see how the progressive difficulty system works.") 