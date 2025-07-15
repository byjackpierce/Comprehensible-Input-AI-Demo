from flask import Flask
from config import config
import os

def create_app(config_name='default'):
    """
    Application factory function
    Creates and configures the Flask application
    """
    
    # Create Flask app instance
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='static')

    # Load configuration
    app.config.from_object(config[config_name])

    # Initialize extensions (we'll add these later)
    # db.init_app(app)  # for database
    # login_manager.init_app(app)  # for user authentication

    # Register blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app