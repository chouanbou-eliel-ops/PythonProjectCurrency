from flask import Blueprint, render_template

admin = Blueprint('admin_bp', __name__)

@admin.route('/admin')
def admin():
    return render_template('admin/admin.html')

@admin.route('/admin/stats')
def admin_stats():
    return render_template('admin/stats.html')

@admin.route('/admin/users')
def admin_users():
    return render_template('admin/users.html')