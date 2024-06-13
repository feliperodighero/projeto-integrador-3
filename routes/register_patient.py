from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for, jsonify
from flask_login import login_required

from database.models.patient import register_patient_bd, get_patient_by_cpf

register_patient_bp = Blueprint("register_patient", __name__)


@register_patient_bp.route("/register_patient", methods=["GET", "POST"])
@login_required
def register_patient():
    if request.method == "POST":
        cpf = request.form["ClientCpf"]
        existing_patient = get_patient_by_cpf(cpf)
        if existing_patient:
            # Retornar mensagem de erro ou renderizar template com erro
            return render_template("register_patient.html", error="CPF já cadastrado.")

        name = request.form["ClientName"]
        complement = request.form["ClientComplement"]
        street = request.form["ClientStreet"]
        neighborhood = request.form["ClientNeighborhood"]
        cep = request.form["ClientCep"]
        date_birth = request.form["ClientDateBirth"]
        number_phone = request.form["ClientNumberPhone"]
        number_house = request.form["ClientNumberHouse"]
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


@register_patient_bp.route("/check_cpf_exists", methods=["GET"])
def check_cpf_exists():
    cpf = request.args.get("cpf")
    if cpf:
        patient = get_patient_by_cpf(cpf)
        return jsonify({"exists": bool(patient)})
    return jsonify({"exists": False})
