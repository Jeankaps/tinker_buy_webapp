from flask import Flask, Blueprint
from flask import render_template, url_for, request, make_response, session 
from config import app_config

# Create Flask application instance
app = Flask(__name__)

# Load configuration from config module
app.config.from_object('config.app_config')

# Import blueprints
from app.admin import admin_blueprint 
from app.general import general_blueprint

# Register blueprints
app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(general_blueprint, url_prefix='/')
