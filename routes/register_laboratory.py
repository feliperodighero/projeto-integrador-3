from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from database.models.laboratory import register_laboratory_bd

register_laboratory_bp = Blueprint("register_laboratory", __name__)

@register_laboratory_bp.route("/register_laboratory", methods=["GET", "POST"])
@login_required
def edit_user():
    if request.method == "POST":
        name = request.form["LaboratoryName"]
        street = request.form["LaboratoryStreet"]
        complement = request.form["LaboratoryComplement"]
        cnpj = request.form["LaboratoryCnpj"]
        cep = request.form["LaboratoryCep"]
        number_phone = request.form["LaboratoryNumberPhone"]
        number_address = request.form["LaboratoryNumberAddress"]
        neighborhood = request.form["LaboratoryNeighborhood"]
        print(name, street, complement, cnpj, cep, number_phone, number_address, neighborhood)
        register_laboratory_bd(
            name,
            street,
            complement,
            cnpj,
            cep,
            number_phone,
            number_address,
            neighborhood,
        )
        return redirect(url_for("register_laboratory.edit_user"))
    return render_template("register_laboratory.html")
