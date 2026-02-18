from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.services.currency_service import *
from app.models.conversion import Conversion

conversion_bp = Blueprint("Conversion", __name__, url_prefix="/convert")

@conversion_bp.route("/conversion", methods=["GET", "POST"])
@login_required
def convert():
    result = None
    if request.method == "POST":
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]
        try:
            amount = float(request.form["amount"])
        except ValueError:
            flash("Invalid amount.")
            return redirect(request.url)
        result = convert_currency(from_currency, to_currency, amount)
        rate = get_rate(from_currency, to_currency)
        save_conversion(current_user.id, from_currency, to_currency, rate)
        return render_template("conver/conversion.html", result=result)
    return render_template("conver/conversion.html")

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