from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.services.admin_service import admin_required
from app.models.user import User
from app.models.conversion import Conversion

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route('/admin_bp')
def admin():
    pass

@admin_bp.route('/admin_bp/stats')
def admin_stats():
    pass

@admin_bp.route("/")
@login_required
@admin_required
def dashboard():

    if not current_user.is_admin:
        return "Access denied", 403

    total_users = User.query.count()
    total_conversions = Conversion.query.count()

    users = User.query.all()
    conversions = Conversion.query.order_by(
        Conversion.id.desc()
    ).limit(20)

    return render_template(
        "admin/dashboard.html",
        total_users=total_users,
        total_conversions=total_conversions,
        users=users,
        conversions=conversions
    )
