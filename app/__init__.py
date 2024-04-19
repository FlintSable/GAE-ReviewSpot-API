from flask import Flask
import os
from app.routes import register_routes
from app.config import Config, DevelopmentConfig, TestingConfig


def create_app():
    app = Flask(__name__)

    # Load default configuration (production)
    app.config.from_object(Config)

    # Override with development or testing configuration if specified
    env = os.getenv('FLASK_ENV')
    if env == 'development':
        app.config.from_object(DevelopmentConfig)
    elif env == 'testing':
        app.config.from_object(TestingConfig)

    # Initialize routes or other components here

    return app