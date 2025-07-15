from flask import Blueprint, render_template

from app.ai_service import AIService

# Create a Blueprint for our main routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Home page route"""
    return render_template('index.html', title='Comprehensible Input AI Demo')

@main_bp.route('/about')
def about():
    """About page route"""
    return render_template('about.html', title='About')


@main_bp.route('/test-ai')
def test_ai():
    """Test OpenAI API connection"""
    try:
        ai_service = AIService()
        result = ai_service.test_connection()
        return f"AI Test Result {result}"
    except Exception as e:
        return f"Error: {str(e)}"