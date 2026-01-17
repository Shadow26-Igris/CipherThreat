import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True   # Enable for HTTPS
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = 3  # Minutes
    FROM_EMAIL = os.getenv("FROM_EMAIL")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'jpg', 'jpeg', 'png', 'zip', 'exe', 'docx'}