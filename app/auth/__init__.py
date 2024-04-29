from flask import Blueprint


auth_blueprint = Blueprint("auth_blueprint",
                           __name__, 
                           template_folder='templates/auth',
                           static_folder="static",
                           static_url_path="assets")



from . import views
