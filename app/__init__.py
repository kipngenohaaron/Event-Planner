from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

        from .routes import bp as routes_bp
        app.register_blueprint(routes_bp)

    return app
