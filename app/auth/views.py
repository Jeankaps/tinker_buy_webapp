from flask import render_template, url_for, flash
from . import auth_blueprint

@auth_blueprint.route("/login/")
def login():
    return render_template("/login.html")

@auth_blueprint.route('/login/',methods=['POST'])
def login_post():
    return "loginPost"

@auth_blueprint.route('signup/')
def signup():
    return "Signup"

@auth_blueprint.route('signup/', methods=['POST'])
def signup_post():
    return "Sign POst"

@auth_blueprint.route('logout/')
def logout():
    return "Logout"