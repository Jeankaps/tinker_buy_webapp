from flask import Blueprint,render_template
from flask_login import current_user, login_required

general_blueprint = Blueprint('general_blueprint', __name__,
                                template_folder='templates',
                               static_folder='static',
                               static_url_path='assests')

@general_blueprint.route('/')
def index():
    return render_template("index.html")

@general_blueprint.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name=current_user.Username)
