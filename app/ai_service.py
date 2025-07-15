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
    
    def test_connection(self):
        """Test if we can connect to openAI API"""
        try:
            # Simple test - ask for a short response
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": "show me 4 german nouns of differing levels of complexity"}
                ],
                max_tokens=100
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Error: {str(e)}"