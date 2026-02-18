from urllib import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user

from app.models.user import User
from app.services.auth_service import *

auth_bp = Blueprint('auth_bp', __name__)




@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = authenticate_user(
            request.form["email"],
            request.form["password"]
        )
        if user:
            login_user(user)
            return redirect(url_for("main_bp.home"))
        flash("Identifiants incorrects")

    return render_template("auth/login.html")

@auth_bp.route('/ logout')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        register_user(
            request.form["username"],
            request.form["email"],
            request.form["password"]
        )
        flash("Compte créé avec succès")
        login_user(current_user)
        return redirect(url_for("main_bp.home"))

    return render_template("auth/register.html")

@auth_bp.route('/auth/profile')
def auth_profile():
    return render_template('conversion/auth_profile.html')

@auth_bp.route('/auth/update')
def auth_update():
    return render_template('conversion/auth_profile.html')
