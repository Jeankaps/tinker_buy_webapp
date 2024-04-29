from flask import Blueprint

cart_blueprint = Blueprint('cart_blueprint', 
                           __name__,
                           template_folder='templates/cart',
                           static_folder='static',
                           static_url_path='assets')

from . import views 

