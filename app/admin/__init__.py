from flask import Blueprint
from flask import render_template, url_for

admin_blueprint = Blueprint('admin_blueprint', 
                            __name__,
                            template_folder='templates',
                            static_folder='static',
                            static_url_path='assests')

from . import views