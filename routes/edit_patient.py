from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from database.models.patient import get_patient_by_id, get_patient_by_cpf, update_patient_bd, delete_patient_bd

edit_patient_bp = Blueprint("edit_patient", __name__)

@edit_patient_bp.route("/edit_patient", methods=["GET", "POST"])
@login_required
def edit_patient():
    if request.method == "POST":
        if 'search' in request.form:
            search_id = request.form.get("SearchID")
            search_cpf = request.form.get("SearchCpfCnpj")

            client = None
            if search_id:
                client = get_patient_by_id(search_id)
            elif search_cpf:
                client = get_patient_by_cpf(search_cpf)

            if client:
                return render_template("edit_patient.html", client=client)
            else:
                flash("Paciente não encontrado", "danger")
                return render_template("edit_patient.html")

        elif 'update' in request.form:
            patient_id = request.form.get("ClientId")
            patient_name = request.form.get("ClientName")
            patient_cpf = request.form.get("ClientCpf")
            patient_phone = request.form.get("ClientNumberPhone")
            patient_neighborhood = request.form.get("ClientNeighborhood")
            patient_street = request.form.get("ClientStreet")
            patient_numberHouse = request.form.get("ClientNumberHouse")
            patient_cep = request.form.get("ClientCep")
            patient_complement = request.form.get("ClientComplement")
            patient_birthdate = request.form.get("ClientDateBirth")

            # Update patient status, assuming it's always True
            patient_status = True

            update_patient_bd(
                patient_id,
                patient_name,
                patient_cpf,
                patient_status,
                patient_phone,
                patient_neighborhood,
                patient_street,
                patient_numberHouse,
                patient_cep,
                patient_complement,
                patient_birthdate
            )
            return redirect(url_for("edit_patient.edit_patient"))

        elif 'delete' in request.form:
            patient_id = request.form.get("ClientId")
            delete_patient_bd(patient_id)
            return redirect(url_for("edit_patient.edit_patient"))

    return render_template("edit_patient.html")
