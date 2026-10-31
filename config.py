import os

class Config:
    # Secret key for session management and CSRF. Use a random value in production.
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    # Database connection string. Example for MySQL.
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'mysql+pymysql://root:password@localhost/jaymani_krishi_sewa'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Flask-Login settings
    REMEMBER_COOKIE_DURATION = 86400  # 1 day in seconds
