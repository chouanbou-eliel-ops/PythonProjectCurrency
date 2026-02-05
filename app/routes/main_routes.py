from flask import Blueprint, render_template, request
from flask_login import login_required
import pandas as pd

main_bp= Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route("/preview-csv", methods=["POST"])
def preview_csv():
    file = request.files.get("file")

    if not file:
        return render_template("preview.html", error="Aucun fichier")

    df = pd.read_csv(file)

    preview = df.head(10).to_dict(orient="records")
    columns = df.columns.tolist()

    return render_template(
        "preview.html",
        columns=columns,
        preview=preview
    )