# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
#     app.config['SECRET_KEY'] = 'your_secret_key'
#     db.init_app(app)

#     with app.app_context():
#         from . import models
#         db.create_all()

#         # Import and register routes blueprint
#         from .routes import bp as routes_bp
#         app.register_blueprint(routes_bp)

#     return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .routes import register_routes  # Import the register_routes function

# Initialize the database
db = SQLAlchemy()

def create_app():
    # Create and configure the Flask app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # Initialize the database with the app
    db.init_app(app)

    # Register the routes
    register_routes(app)  # Call the function to register routes

    return app
