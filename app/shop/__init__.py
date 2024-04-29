from flask import Blueprint

shop_blueprint = Blueprint('shop_blueprint', 
                           __name__,
                           template_folder='templates/shop',
                           static_folder='static',
                           static_url_path='assests')

from . import views 