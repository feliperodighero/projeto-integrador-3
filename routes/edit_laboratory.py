from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from database.models.laboratory import get_laboratory_by_id_bd, get_laboratory_by_cnpj_bd, update_laboratory_bd, delete_laboratory_bd

edit_laboratory_bp = Blueprint("edit_laboratory", __name__)

@edit_laboratory_bp.route("/edit_laboratory", methods=["GET", "POST"])
@login_required
def edit_laboratory():
    if request.method == "POST":
        if 'search' in request.form:
            search_id = request.form.get("SearchID")
            search_cnpj = request.form.get("SearchCnpj")

            laboratory = None
            if search_id:
                laboratory = get_laboratory_by_id_bd(search_id)
            elif search_cnpj:
                laboratory = get_laboratory_by_cnpj_bd(search_cnpj)

            if laboratory:
                return render_template("edit_laboratory.html", laboratory=laboratory)
            else:
                flash("Laboratório não encontrado", "danger")
                return render_template("edit_laboratory.html")

        elif 'update' in request.form:
            laboratory_id = request.form.get("LaboratoryId")
            laboratory_name = request.form.get("LaboratoryName")
            laboratory_cnpj = request.form.get("LaboratoryCnpj")
            laboratory_phone = request.form.get("LaboratoryNumberPhone")
            laboratory_neighborhood = request.form.get("LaboratoryNeighborhood")
            laboratory_street = request.form.get("LaboratoryStreet")
            laboratory_number_house = request.form.get("LaboratoryNumberAddress")
            laboratory_cep = request.form.get("LaboratoryCep")
            laboratory_complement = request.form.get("LaboratoryComplement")

            update_laboratory_bd(
                laboratory_id,
                laboratory_name,
                laboratory_cnpj,
                laboratory_phone,
                laboratory_neighborhood,
                laboratory_street,
                laboratory_number_house,
                laboratory_cep,
                laboratory_complement
            )

            flash("Laboratório atualizado com sucesso", "success")
            return redirect(url_for("edit_laboratory.edit_laboratory"))

        elif 'delete' in request.form:
            laboratory_id = request.form.get("LaboratoryId")

            delete_laboratory_bd(laboratory_id)

            flash("Laboratório excluído com sucesso", "success")
            return redirect(url_for("edit_laboratory.edit_laboratory"))

    return render_template("edit_laboratory.html")
