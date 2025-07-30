import os
from tempfile import tempdir
from openai import OpenAI
from .prompts import (
    BINARY_FEEDBACK_PROMPT,
    WORD_GENERATION_PROMPT,
    SENTENCE_GENERATION_PROMPT,
    NATURAL_TRANSLATION_PROMPT,
    DETAILED_FEEDBACK_PROMPT,
    PROGRESSIVE_SENTENCE_SEQUENCE_PROMPT
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
    

    def generate_words(self, language, count=4, temperature=1.5, top_p=0.9):
        prompt = WORD_GENERATION_PROMPT.format(count=count, language=language)

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages = [
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=temperature,
                top_p=top_p,
            )

            # Get the response and split it into individual words
            words = (response.choices[0].message.content or "").strip().split('\n')
            # Clean up empty lines
            words = [word.strip() for word in words if word.strip()]

            return words[:count] # Makes sure only requested number is returned

        except Exception as e:
            return []

    def generate_sentence_with_word(self, word, language, temperature=1.5, top_p=0.85):
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
                temperature=temperature,
                top_p=top_p
            )
        
            return response.choices[0].message.content

        except:
            return "error in sentence generation"

    def generate_progressive_sentence_sequence(self, word, language, temperature=1.2, top_p=0.9):
        """
        Generate 5 sentences with progressive difficulty (subtle → obvious).
        
        Args:
            word (str): The target foreign word
            language (str): The language of the word
        
        Returns:
            list: 5 sentences with progressive difficulty
        """
        prompt = PROGRESSIVE_SENTENCE_SEQUENCE_PROMPT.format(language=language, word=word)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=temperature,
                top_p=top_p,
                presence_penalty=0.4  # Added presence penalty for better context diversity
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
            
            # Ensure we have exactly 5 sentences
            if len(sentences) < 5:
                # Fallback: generate individual sentences to fill up
                while len(sentences) < 5:
                    fallback_sentence = self.generate_sentence_with_word(word, language)
                    if fallback_sentence and fallback_sentence != "error in sentence generation":
                        sentences.append(fallback_sentence)
            
            return sentences[:5]  # Return exactly 5 sentences
            
        except Exception as e:
            # Fallback to individual sentence generation
            sentences = []
            for _ in range(5):
                sentence = self.generate_sentence_with_word(word, language)
                if sentence and sentence != "error in sentence generation":
                    sentences.append(sentence)
            return sentences

        
    def return_binary_feedback(self, word, language, guess):
        """
        Check if user's guess is correct for the target word.
        
        Args:
            word (str): The target foreign word
            language (str): The language of the word
            guess (str): The user's guess
        
        Returns:
            str: "correct" or "incorrect"
        """
        prompt = BINARY_FEEDBACK_PROMPT.format(
            language=language,
            word=word,
            guess=guess
        )

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=10,
                temperature=0.05,
                top_p=0.5
                
            )

            # Safer handling of response
            content = response.choices[0].message.content
            if content is None:
                return "incorrect"
            
            return content.strip().lower()

        except Exception as e:
            return "incorrect" # return incorrect as default on error

    def get_natural_translation(self, word, language):
        """
        Get a natural, detailed translation for the target word.
        
        Args:
            word (str): The target foreign word
            language (str): The language of the word
        
        Returns:
            str: Natural translation with explanation
        """
        prompt = NATURAL_TRANSLATION_PROMPT.format(
            language=language,
            word=word
        )

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=0.7,
                top_p=0.9
            )

            content = response.choices[0].message.content
            return content.strip() if content else f"'{word}' means the target word in {language}"

        except Exception as e:
            return f"'{word}' means the target word in {language}"

    def get_detailed_feedback(self, word, language, final_guess, all_guesses, sentences):
        """
        Generate detailed feedback for the learning session.
        
        Args:
            word (str): The target foreign word
            language (str): The language of the word
            final_guess (str): The user's final/correct guess
            all_guesses (list): All guesses made by the user
            sentences (list): All sentences shown to the user
        
        Returns:
            str: Detailed feedback message
        """
        prompt = DETAILED_FEEDBACK_PROMPT.format(
            language=language,
            word=word,
            final_guess=final_guess,
            all_guesses=", ".join(all_guesses),
            sentence_count=len(sentences),
            sentences=" | ".join(sentences)
        )

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.8,
                top_p=0.9
            )

            content = response.choices[0].message.content
            return content.strip() if content else "Great job learning through context!"

        except Exception as e:
            return "Great job learning through context!"
