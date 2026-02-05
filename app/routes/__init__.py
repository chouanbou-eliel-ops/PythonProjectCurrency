from app.routes.auth_routes import auth
from app.routes.main import main
from app.routes.admin_routes import admin
from app.routes.conversion_routes import conversion

def register_routes (app):
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint()
    app.register_blueprint()