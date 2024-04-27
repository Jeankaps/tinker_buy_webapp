import os

class Config:
    SECRET_KEY = 'Development'   # We will need to change this!!

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Choose the appropriate configuration based on the environment
if os.environ.get('FLASK_ENV') == 'production':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()
