from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required

from database.models.patient import register_patient_bd

register_patient_bp = Blueprint("register_patient", __name__)


@register_patient_bp.route("/register_patient", methods=["GET", "POST"])
@login_required
def register_patient():
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
