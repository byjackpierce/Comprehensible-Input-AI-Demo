import os
from openai import OpenAI

class AIService:
    """Service class for OpenAI API interactions"""

    def __init__(self):
        """Initialise OpenAI client"""
        # Get API key from environment variable
        api_key = os.environ.get('OPENAI_API_KEY')

        # Check if API key exists
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")

        # Create OpenAI client
        self.client = OpenAI(api_key=api_key)
    
    
    def generate_words(self, language, count=4):
        prompt = f"generate {str(count)} nouns in {language} and return only those 4 nouns, one per line"

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages = [
                    {"role": "user", "content": prompt}
                ]
            )

            # Get the response and split it into individual words
            words = response.choices[0].message.content.strip().split('\n')
            # Clean up empty lines
            words = [word.strip() for word in words if word.strip()]

            return words[:count] # Makes sure only requested number is returned

        except Exception as e:
            return []
