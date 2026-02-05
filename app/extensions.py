from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()

#migration
migrate = Migrate()

#gestion de connexion
login_manager = LoginManager()
login_manager.login_view = 'auth.login'