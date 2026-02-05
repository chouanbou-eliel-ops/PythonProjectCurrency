from urllib import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

@auth.route('/ logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')

@auth.route('/register', methods=['POST'])
def register():
