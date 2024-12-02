import os

class Config:
    # Set the secret key for session management
    SECRET_KEY = os.urandom(24)
    
    # SQLite database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/events.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking
