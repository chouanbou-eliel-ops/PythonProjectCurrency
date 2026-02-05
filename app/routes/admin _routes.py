from flask import Blueprint, render_template

main = Blueprint('admin', __name__)

@main.route('/admin')
def admin():
    return render_template('admin/admin.html')

@main.route('/admin/stats')
def admin_stats():
    return render_template('admin/stats.html')

@main.route('/admin/users')
def admin_users():
    return render_template('admin/users.html')