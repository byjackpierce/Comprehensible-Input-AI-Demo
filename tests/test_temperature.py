import sys
import os
# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.ai_service import AIService

def test_temperature_effects():
    ai_service = AIService()

    temperatures = [0.1, 0.3, 0.5, 0.7, 1.0]

    language = "German"
    count = 8
    num_tests = 3

    print(f"️  TEMPERATURE TESTING")
    print(f"Testing word generation for {language} with different temperatures")
    print(f"Running {num_tests} tests per temperature value")
    print("="*80)

    for temp in temperatures:
        print(f"\n Temperature: {temp}")
        print("-" * 40)

        for i in range(num_tests):
            words = ai_service.generate_words(language, count, temperature=temp)
            print(f"Test {i+1}: {words}")
        
        print()

if __name__ == "__main__":
    test_temperature_effects()