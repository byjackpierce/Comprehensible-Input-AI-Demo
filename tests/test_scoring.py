import sys
import os
# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.ai_service import AIService

def test_scoring():
    ai_service = AIService()

    # Test cases with Spanish words - focusing on nuanced scoring
    test_cases = [
        # Correct answers (should be 9-10)
        {"word": "paraguas", "language": "Spanish", "guess": "umbrella"},
        {"word": "refrigerador", "language": "Spanish", "guess": "refrigerator"},
        {"word": "bicicleta", "language": "Spanish", "guess": "bicycle"},
        {"word": "linterna", "language": "Spanish", "guess": "flashlight"},
        {"word": "guante", "language": "Spanish", "guess": "glove"},
        
        # Very close answers (should be 7-8)
        {"word": "paraguas", "language": "Spanish", "guess": "rain protection"},
        {"word": "refrigerador", "language": "Spanish", "guess": "fridge"},
        {"word": "bicicleta", "language": "Spanish", "guess": "bike"},
        {"word": "linterna", "language": "Spanish", "guess": "torch"},
        {"word": "guante", "language": "Spanish", "guess": "mitten"},
        
        # Right category, wrong specific item (should be 5-6)
        {"word": "paraguas", "language": "Spanish", "guess": "raincoat"},
        {"word": "refrigerador", "language": "Spanish", "guess": "freezer"},
        {"word": "bicicleta", "language": "Spanish", "guess": "motorcycle"},
        {"word": "linterna", "language": "Spanish", "guess": "lamp"},
        {"word": "guante", "language": "Spanish", "guess": "sock"},
        
        # More nuanced cases - harder to score
        {"word": "paraguas", "language": "Spanish", "guess": "rain hat"},
        {"word": "paraguas", "language": "Spanish", "guess": "water protection"},
        {"word": "paraguas", "language": "Spanish", "guess": "shade"},
        {"word": "paraguas", "language": "Spanish", "guess": "cover"},
        
        {"word": "refrigerador", "language": "Spanish", "guess": "cooler"},
        {"word": "refrigerador", "language": "Spanish", "guess": "ice box"},
        {"word": "refrigerador", "language": "Spanish", "guess": "cold storage"},
        {"word": "refrigerador", "language": "Spanish", "guess": "chiller"},
        
        {"word": "bicicleta", "language": "Spanish", "guess": "tricycle"},
        {"word": "bicicleta", "language": "Spanish", "guess": "scooter"},
        {"word": "bicicleta", "language": "Spanish", "guess": "two-wheeler"},
        {"word": "bicicleta", "language": "Spanish", "guess": "pedal vehicle"},
        
        {"word": "linterna", "language": "Spanish", "guess": "light"},
        {"word": "linterna", "language": "Spanish", "guess": "beam"},
        {"word": "linterna", "language": "Spanish", "guess": "spotlight"},
        {"word": "linterna", "language": "Spanish", "guess": "illuminator"},
        
        {"word": "guante", "language": "Spanish", "guess": "hand covering"},
        {"word": "guante", "language": "Spanish", "guess": "finger protection"},
        {"word": "guante", "language": "Spanish", "guess": "mitt"},
        {"word": "guante", "language": "Spanish", "guess": "hand warmer"},
        
        # Edge cases - similar concepts
        {"word": "paraguas", "language": "Spanish", "guess": "tent"},
        {"word": "paraguas", "language": "Spanish", "guess": "awning"},
        {"word": "paraguas", "language": "Spanish", "guess": "canopy"},
        
        {"word": "refrigerador", "language": "Spanish", "guess": "air conditioner"},
        {"word": "refrigerador", "language": "Spanish", "guess": "thermos"},
        {"word": "refrigerador", "language": "Spanish", "guess": "wine cooler"},
        
        {"word": "bicicleta", "language": "Spanish", "guess": "unicycle"},
        {"word": "bicicleta", "language": "Spanish", "guess": "skateboard"},
        {"word": "bicicleta", "language": "Spanish", "guess": "roller skates"},
        
        {"word": "linterna", "language": "Spanish", "guess": "candle"},
        {"word": "linterna", "language": "Spanish", "guess": "fire"},
        {"word": "linterna", "language": "Spanish", "guess": "bulb"},
        
        {"word": "guante", "language": "Spanish", "guess": "bandage"},
        {"word": "guante", "language": "Spanish", "guess": "bracelet"},
        {"word": "guante", "language": "Spanish", "guess": "ring"},
        
        # Wrong category but related concept (should be 3-4)
        {"word": "paraguas", "language": "Spanish", "guess": "hat"},
        {"word": "refrigerador", "language": "Spanish", "guess": "cabinet"},
        {"word": "bicicleta", "language": "Spanish", "guess": "car"},
        {"word": "linterna", "language": "Spanish", "guess": "window"},
        {"word": "guante", "language": "Spanish", "guess": "shirt"},
        
        # Completely wrong (should be 0-2)
        {"word": "paraguas", "language": "Spanish", "guess": "computer"},
        {"word": "refrigerador", "language": "Spanish", "guess": "book"},
        {"word": "bicicleta", "language": "Spanish", "guess": "banana"},
        {"word": "linterna", "language": "Spanish", "guess": "tree"},
        {"word": "guante", "language": "Spanish", "guess": "chair"},
    ]

    print(f"🧪 SPANISH SCORING SYSTEM TESTING")
    print(f"Testing AI scoring for Spanish words - focusing on nuanced cases")
    print(f"Running 2 tests per test case")
    print("="*80)

    for i, test_case in enumerate(test_cases, 1):
        word = test_case["word"]
        language = test_case["language"]
        guess = test_case["guess"]
        
        print(f"\n{i:2d}. {language} - '{word}'")
        print(f"    Guess: '{guess}'")
        print("-" * 60)

        for j in range(2):
            score_response = ai_service.return_score(word, language, guess)
            print(f"Test {j+1}: {score_response}")
        
        print()

if __name__ == "__main__":
    test_scoring() 