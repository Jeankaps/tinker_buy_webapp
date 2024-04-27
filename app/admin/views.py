from flask import render_template, url_for, redirect
from . import admin_blueprint

@admin_blueprint.route('/admin/')
def admin_page():
    return render_template("dashboard.html")
