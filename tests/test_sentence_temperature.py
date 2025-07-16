import sys
import os
# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.ai_service import AIService

def test_sentence_temperature_effects():
    ai_service = AIService()

    temperatures = [1.2, 1.4, 1.6, 1.8]

    # Test with a single word to keep it simple
    language = "German"
    word = "Kofferraum"
    num_tests = 10

    print(f"🧪 SENTENCE GENERATION TEMPERATURE TESTING")
    print(f"Testing sentence generation for '{word}' ({language}) with different temperatures")
    print(f"Running {num_tests} tests per temperature value")
    print("="*80)

    for temp in temperatures:
        print(f"\n  Temperature: {temp}")
        print("-" * 40)

        for i in range(num_tests):
            sentence = ai_service.generate_sentence_with_word(word, language, temperature=temp)
            print(f"Test {i+1}: {sentence}")
        
        print()

if __name__ == "__main__":
    test_sentence_temperature_effects() 