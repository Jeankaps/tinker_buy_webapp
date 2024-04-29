import os

class Config:
    SECRET_KEY = 'Development'   # We will need to change this!!
    MYSQL_HOST = '172.17.0.1'   # Change this if not using docker
    MYSQL_USER = 'root'
    #MYSQL_PASSWORD = os.environ.get('DB_PASSWD')
    MYSQL_PASSWORD = 'hardtoguess'
    MYSQL_DB = 'development'
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Choose the appropriate configuration based on the environment
if os.environ.get('FLASK_ENV') == 'production':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()
