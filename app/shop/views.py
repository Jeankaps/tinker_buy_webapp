from flask import render_template
from . import shop_blueprint

@shop_blueprint.route('/shop')
def shop():
    return render_template('cart.html')
