from app.routes.auth_routes import auth_bp
from app.routes.main_routes import main_bp
from app.routes.admin_routes import admin
from app.routes.conversion_routes import conversion_bp

def register_routes (app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin)
    app.register_blueprint(conversion_bp)