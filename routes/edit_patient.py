from flask import Blueprint, render_template
from flask_login import login_required

edit_patient_bp = Blueprint("edit_patient", __name__)

@edit_patient_bp.route("/edit_patient", methods=["GET"])
@login_required
def edit_patient():
    return render_template("edit_patient.html")