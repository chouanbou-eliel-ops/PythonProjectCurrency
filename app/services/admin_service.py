# creer un admin
#bloquer user
#voir les statistiques

from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for("auth.login"))

        if not current_user.is_admin:
            flash("Accès refusé")
            return redirect(url_for("main.home"))

        return func(*args, **kwargs)
    return wrapper
