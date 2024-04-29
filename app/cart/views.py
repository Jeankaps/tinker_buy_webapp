from flask import render_template
from . import cart_blueprint

@cart_blueprint.route('/cart/')
def cart():
    return render_template('test.html')
