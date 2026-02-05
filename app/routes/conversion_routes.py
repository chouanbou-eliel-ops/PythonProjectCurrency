from flask import Blueprint, render_template

conversion_bp = Blueprint('conversion_bp', __name__)

@conversion_bp.route('/conversion', methods=['GET', 'POST'])
def conversion():
    return render_template('conversion.html')
