#hash password
#verifier login

from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from app.models.user import User

def register_user(username, email, password):
    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user
    return None
 