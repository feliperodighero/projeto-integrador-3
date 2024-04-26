from flask import Blueprint, render_template
from flask_login import login_required

select_user_patient_bp = Blueprint("select_user_patient", __name__)


@select_user_patient_bp.route("/select_user_patient", methods=["GET"])
@login_required
def select_user_patient():
    return render_template("select_user_patient.html")
