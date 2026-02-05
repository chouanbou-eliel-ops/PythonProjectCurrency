from urllib import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user

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
            return redirect(url_for("main.home"))
        flash("Identifiants incorrects")

    return render_template("auth/login.html")

@auth_bp.route('/ logout')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))

@auth_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')

@auth_bp.route('/register', methods=['POST'])
def register():
    if request.method == "POST":
        register_user(
            request.form["username"],
            request.form["email"],
            request.form["password"]
        )
        flash("Compte créé avec succès")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")

@auth_bp.route('/auth/profile')
def auth_profile():
    return render_template('auth_profile.html')

@auth_bp.route('/auth/update')
def auth_update():
    return render_template('auth_update.html')
