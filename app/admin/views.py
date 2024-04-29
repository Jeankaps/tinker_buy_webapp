from flask import render_template, url_for, redirect
from . import admin_blueprint
from flask import current_app
from app import tables
from app.models import  db 

@admin_blueprint.route('/admin/')
def admin_page():
    user = db.session.query(tables['User']).first()
    #return f"This page {user.Username}"
    return render_template("/dashboard.html")
