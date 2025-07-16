from flask import Blueprint, render_template, jsonify
from app.ai_service import AIService

# Create a Blueprint for our main routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def game():
    """Main game interface - everything happens here"""
    return render_template('game.html')


@main_bp.route('/api/generate-words/<language>')
def api_generate_words(language):
    """API endpoint for generating words"""
    try:
        ai_service = AIService()
        words = ai_service.generate_words(language, count=4)
        return jsonify({'words': words})
    except Exception as e:
        return jsonify({'error': str(e)})

@main_bp.route('/api/generate-sentence/<language>/<word>')
def api_generate_sentence(language, word):
    """API endpoint for generating sentences with target words"""
    try:
        ai_service = AIService()
        sentence = ai_service.generate_sentence_with_word(word, language)
        return jsonify({'sentence': sentence})
    except Exception as e:
        return jsonify({'error': str(e)})

@main_bp.route('/api/score-guess/<word>/<language>/<guess>')
def api_score_guess(word, language, guess):
    """API endpoint scoring the user's guess"""
    try:
        ai_service = AIService()
        score = ai_service.return_score(word, language, guess)
        return jsonify({'score': score})
    except Exception as e:
        return jsonify({'error': str(e)})