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
                ],
                max_tokens=100
            )

            # Get the response and split it into individual words
            words = (response.choices[0].message.content or "").strip().split('\n')
            # Clean up empty lines
            words = [word.strip() for word in words if word.strip()]

            return words[:count] # Makes sure only requested number is returned

        except Exception as e:
            return []

    def generate_sentence_with_word(self, word, language):
        """
        Generate an English sentence containing the target foreign word.
        
        Args:
            word (str): The foreign word to include in the sentence
            language (str): The language of the word (e.g., 'German', 'Spanish')
        
        Returns:
            str: An English sentence with the foreign word in context
        """
        prompt = f"""
        Generate an english sentence that uses the {language} word '{word}' in context.

        Requirements:
        - Use '{word}' naturally in an English sentence
        - Provide clear context clues about what '{word}' means
        - Make it appropriate for language learning
        - Return only the sentence, nothing else
        
        Example format: 'She opened the Kofferraum and loaded her groceries.'"""
        
        try:
            response = self.client.chat.completions.create(
                model = 'gpt-4o',
                messages = [
                    {"role": "user", "content": prompt}
                ],
                max_tokens = 100
            )
        
            return response.choices[0].message.content

        except:
            return "error in sentence generation"


        
    def return_score(self, word, language, guess):
        """
        scoring system
        """
        prompt = f"""
        Score this guess for a {language} word on a 0-10 scale.

        Target word: '{word}'
        User's guess: '{guess}'

        You are acting as a language learning assistant that helps users infer the meanings of unknown words through context.

        A user is participating in a demo where they are shown a sentence that includes a foreign or rare word, and they try to guess its meaning based on the context.

        Your job is to:
        1. Evaluate how close the users guess is to the actual meaning of the word **as used in this sentence**.
        2. Score their guess from 0 to 10, where:
        - 10 means their guess is **fully correct**
        - 9-9.9 means **very close**, with only slight imprecision or missing nuance
        - 6-8.9 means **partially correct** — broadly in the right category, but with notable inaccuracy or ambiguity
        - 3-5.9 means **weakly related**, only superficially correct or contextually off
        - 0-2.9 means **wrong**, unrelated or clearly misunderstood
        3. Give a **short, helpful comment** to explain why the guess was accurate, partially accurate, or off

        ### Input format:

        - Word: [foreign or rare word]
        - Sentence: [the full English sentence with the target word in it]
        - User Guess: [the user's one-line guess of what the word means]

        ### Output format:

        Score: X/10  
        Comment: [your explanation]

        ### Example:

        Word: "Schlüssel"  
        Sentence: "He pulled the Schlüssel out of his pocket and unlocked the front door."  
        User Guess: "wallet"  

        Score: 6/10  
        Comment: You're in the right category (small object kept in a pocket), but its used to unlock things — think door access.
        """
        
        try:
            response = self.client.chat.completions.create(
                model = 'gpt-4o',
                messages = [
                    {"role": "user", "content": prompt}
                ],
                max_tokens = 100
            )
        
            return response.choices[0].message.content

        except:
            return "error in scoring"