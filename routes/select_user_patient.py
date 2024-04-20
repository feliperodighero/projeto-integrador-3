from flask import Blueprint, render_template, session, url_for, redirect


select_user_patient_bp = Blueprint("select_user_patient", __name__)


@select_user_patient_bp.route("/select_user_patient", methods=["GET"])
def select_user_patient():
    if "username" not in session:
        return redirect(url_for("login_user.login"))

    return render_template("select_user_patient.html")
