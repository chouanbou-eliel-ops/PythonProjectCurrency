from flask import Flask
from Config import Config
from app.extensions import db
from app.routes import register_routes

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