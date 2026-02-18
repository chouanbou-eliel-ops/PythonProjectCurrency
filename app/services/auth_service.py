#hash password
#verifier login

from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from flask_login import current_user, login_manager
from app.models.user import User
from flask_login import login_user, logout_user
from flask import redirect, url_for, flash
from sqlalchemy.exc import IntegrityError

def register_user(username, email, password):
    if User.query.filter_by(email = email).first() is not None:
        flash("email deja utlisé")
        return redirect(url_for("auth_bp.register", username=username))
    if User.query.filter_by(username = username).first():
        flash("username existante")
        return redirect(url_for("auth_bp.register", email = email))
    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password_hash=hashed_password, role = "user")
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        flash("username ou email existante")
    return user

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        return user
    return None

def confirm_user(username, email, password):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return False
    if check_password_hash(user.password_hash, password):
        login_user(user)
        return True
    else:
        return False

"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
"""
