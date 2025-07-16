import os
from tempfile import tempdir
from openai import OpenAI
from .prompts import (
    SCORING_SYSTEM_PROMPT, 
    SCORING_USER_PROMPT_TEMPLATE,
    WORD_GENERATION_PROMPT,
    SENTENCE_GENERATION_PROMPT
)

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
    

    def generate_words(self, language, count=4, temperature=1.2):
        prompt = WORD_GENERATION_PROMPT.format(count=count, language=language)

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages = [
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=temperature
            )

            # Get the response and split it into individual words
            words = (response.choices[0].message.content or "").strip().split('\n')
            # Clean up empty lines
            words = [word.strip() for word in words if word.strip()]

            return words[:count] # Makes sure only requested number is returned

        except Exception as e:
            return []

    def generate_sentence_with_word(self, word, language, temperature=1.2):
        """
        Generate an English sentence containing the target foreign word.
        
        Args:
            word (str): The foreign word to include in the sentence
            language (str): The language of the word (e.g., 'German', 'Spanish')
        
        Returns:
            str: An English sentence with the foreign word in context
        """
        prompt = SENTENCE_GENERATION_PROMPT.format(language=language, word=word)
        
        try:
            response = self.client.chat.completions.create(
                model = 'gpt-4o',
                messages = [
                    {"role": "user", "content": prompt}
                ],
                max_tokens = 100,
                temperature=temperature
            )
        
            return response.choices[0].message.content

        except:
            return "error in sentence generation"


        
    def return_score(self, word, language, guess):
        """
        Score the user's guess for a foreign word.
        
        Args:
            word (str): The target foreign word
            language (str): The language of the word
            guess (str): The user's guess
        
        Returns:
            str: AI response with score and feedback
        """
        user_prompt = SCORING_USER_PROMPT_TEMPLATE.format(
            language=language,
            word=word,
            guess=guess
        )
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": SCORING_SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=150,
            )
        
            return response.choices[0].message.content

        except Exception as e:
            return f"Error in scoring: {str(e)}"