from flask import Blueprint, render_template

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