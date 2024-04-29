from flask import render_template, url_for, flash, redirect, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db, User 
from . import auth_blueprint

@auth_blueprint.route("/login/")
def login():
    return render_template("/login.html")

@auth_blueprint.route('/login/',methods=['POST'])
def login_post():
  # login code
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False 

    user = User.query.filter_by(Username=username).first()

    # check if the user actually exists
    # take the user supplied password, hash it, and compare it
    if not user or not check_password_hash(user.Password_hash, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth_blueprint.login')) # reload page if user dne or password is wrong
    # if the checks pass, the we know the user has the right password
    login_user(user, remember=remember)
    return redirect(url_for('general_blueprint.profile'))

@auth_blueprint.route('signup/')
def signup():
    return render_template('signup.html')


@auth_blueprint.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to db 
    # email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    # if this returns a username, then user already exits
    user = User.query.filter_by(Username=username).first()

    if user:
        flash('This account already exists')
        return redirect(url_for('auth_blueprint.signup'))
    # create new user
    new_user = User( Username=username, Password_hash=generate_password_hash(password,method='pbkdf2:sha256', salt_length=16)) 

    # add user to db
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth_blueprint.login'))

@auth_blueprint.route('logout/')
def logout():
    logout_user()
    return redirect(url_for('general_blueprint.index'))