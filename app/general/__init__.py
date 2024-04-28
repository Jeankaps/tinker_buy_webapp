from flask import Blueprint,render_template

general_blueprint = Blueprint('general_blueprint', __name__,
                                template_folder='templates',
                               static_folder='static',
                               static_url_path='assests')

@general_blueprint.route('/')
def index():
    return render_template("base.html")

