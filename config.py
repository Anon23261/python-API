import os
from datetime import timedelta

class Config:
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT settings
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key')  # Change this in production
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    
    # Cache settings
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300
    
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')  # Change this in production
