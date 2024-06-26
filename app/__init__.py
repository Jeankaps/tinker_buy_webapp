from flask import Flask, Blueprint
from flask import render_template, url_for, request, make_response, session 
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from app.models import init_db

# Create Flask application instance
app = Flask(__name__)

# Load configuration from config module
app.config.from_object('config.app_config')

# Initialize db and return list of class tables
tables = init_db(app)

# Import blueprints
from app.admin import admin_blueprint 
from app.general import general_blueprint
from app.auth import auth_blueprint
from app.cart import cart_blueprint
from app.shop import shop_blueprint

# Register blueprints
app.register_blueprint(admin_blueprint, url_prefix='/')
app.register_blueprint(general_blueprint, url_prefix='/')
app.register_blueprint(auth_blueprint, url_prefix='/')
app.register_blueprint(cart_blueprint, url_prefix='/')
app.register_blueprint(shop_blueprint, url_prefix='/')
