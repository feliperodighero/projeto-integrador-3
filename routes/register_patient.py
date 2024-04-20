from flask import Blueprint, render_template, session, url_for, redirect, request
from database.models.patient import register_patient_bd
from datetime import datetime

register_patient_bp = Blueprint("register_patient", __name__)


@register_patient_bp.route("/register_patient", methods=["GET", "POST"])
def register_patient():
    if "username" not in session:
        return redirect(url_for("login_user.login"))
    if request.method == "POST":
        name = request.form["ClientName"]
        cpf = request.form["ClientCpf"]
        date_birth = request.form["ClientDateBirth"]
        number_phone = request.form["ClientNumberPhone"]
        street = request.form["ClientStreet"]
        cep = request.form["ClientCep"]
        number_house = request.form["ClientNumberHouse"]
        neighborhood = request.form["ClientNeighborhood"]
        complement = request.form["ClientComplement"]
        date_register = datetime.now()
        register_patient_bd(
            name,
            cpf,
            date_birth,
            number_phone,
            street,
            cep,
            number_house,
            neighborhood,
            complement,
            date_register,
        )
        return redirect(url_for("register_patient.register_patient"))
    return render_template("register_patient.html")
