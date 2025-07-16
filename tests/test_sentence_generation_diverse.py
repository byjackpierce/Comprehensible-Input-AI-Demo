import sys
import os
# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.ai_service import AIService

def test_sentence_generation_diverse():
    ai_service = AIService()

    # Test cases with words from different languages
    test_cases = [
        # German words
        {"word": "Kühlschrank", "language": "German"},
        {"word": "Regenschirm", "language": "German"},
        {"word": "Handschuh", "language": "German"},
        {"word": "Fahrrad", "language": "German"},
        {"word": "Taschenlampe", "language": "German"},
        
        # Spanish words
        {"word": "paraguas", "language": "Spanish"},
        {"word": "refrigerador", "language": "Spanish"},
        {"word": "guante", "language": "Spanish"},
        {"word": "bicicleta", "language": "Spanish"},
        {"word": "linterna", "language": "Spanish"},
        
        # French words
        {"word": "parapluie", "language": "French"},
        {"word": "réfrigérateur", "language": "French"},
        {"word": "gant", "language": "French"},
        {"word": "vélo", "language": "French"},
        {"word": "lampe", "language": "French"},
        
        # Italian words
        {"word": "ombrello", "language": "Italian"},
        {"word": "frigorifero", "language": "Italian"},
        {"word": "guanto", "language": "Italian"},
        {"word": "bicicletta", "language": "Italian"},
        {"word": "torcia", "language": "Italian"},
        
        # Portuguese words
        {"word": "guarda-chuva", "language": "Portuguese"},
        {"word": "geladeira", "language": "Portuguese"},
        {"word": "luva", "language": "Portuguese"},
        {"word": "bicicleta", "language": "Portuguese"},
        {"word": "lanterna", "language": "Portuguese"},
    ]

    print(f"🧪 SENTENCE GENERATION DIVERSITY TESTING")
    print(f"Testing sentence generation across multiple languages")
    print(f"Running 3 tests per word")
    print("="*80)

    for i, test_case in enumerate(test_cases, 1):
        word = test_case["word"]
        language = test_case["language"]
        
        print(f"\n{i:2d}. {language} - '{word}'")
        print("-" * 50)

        for j in range(3):
            sentence = ai_service.generate_sentence_with_word(word, language, temperature=1.2)
            print(f"Test {j+1}: {sentence}")
        
        print()

if __name__ == "__main__":
    test_sentence_generation_diverse() 