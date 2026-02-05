from urllib import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    pass

@auth_bp.route('/ logout')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@auth_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')

@auth_bp.route('/register', methods=['POST'])
def register():
    return "n"