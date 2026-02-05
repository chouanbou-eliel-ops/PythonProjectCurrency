from flask import Blueprint, render_template

conversion_bp = Blueprint('conversion_bp', __name__)

@conversion_bp.route('/conversion', methods=['GET', 'POST'])
def conversion():
    return render_template('conversion.html')

@conversion_bp.route("/history")
@login_required
def history():
    conversions = Conversion.query.filter_by(
        user_id=current_user.id
    ).order_by(Conversion.created_at.desc()).all()

    return render_template("Conversion/history.html", conversions=conversions)


@conversion_bp.route("/history/clear")
@login_required
def clear_history():
    Conversion.query.filter_by(
        user_id=current_user.id
    ).delete()

    db.session.commit()
    flash("Historique effacé")

    return redirect(url_for("Conversion.history"))

from app.extensions import db
from flask_login import current_user

@conversion_bp.route("/history/delete/<int:id>")
@login_required
def delete_conversion(id):
    conversion = Conversion.query.get_or_404(id)

    if conversion.user_id != current_user.id:
        flash("Action non autorisée")
        return redirect(url_for("Conversion.history"))

    db.session.delete(conversion)
    db.session.commit()
    flash("Conversion supprimée")

    return redirect(url_for("Conversion.history"))