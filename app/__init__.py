from flask import Flask
from Config import Config
from app.extensions import db, login_manager, migrate
from app.routes import register_routes
from app.models.user import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialisation des extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    register_routes(app)    #Enregitrement des routes

    with app.app_context(): #Creation des tables
        db.create_all()
    return app
"""

"""


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))