from flask import Flask
from Config import Config
from app.extensions import db, login_manager, migrate
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialisation des extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    register_routes(app)    #Enregitrement des routes
    return app
"""
    with app.app_context(): #Creation des tables
        db.create_all()
"""

from flask import Flask
from config import Config
from app.extensions import db, login_manager, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Import et enregistrement Blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.conversion_routes import conversion_bp
    from app.routes.admin_routes import admin_bp
    from app.routes.main_routes import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(conversion_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(main_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
