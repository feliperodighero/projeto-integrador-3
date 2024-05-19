from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from database.models.user import (
    get_user_by_id,
    get_user_by_cpf,
    get_user_by_name,
    update_user_bd,
    delete_user_bd
)

edit_user_bp = Blueprint("edit_user", __name__)

@edit_user_bp.route("/edit_user", methods=["GET", "POST"])
@login_required
def edit_user_route():
    if request.method == "POST":
        if 'search' in request.form:
            search_id = request.form.get("SearchID")
            search_cpf = request.form.get("SearchCpfCnpj")
            search_name = request.form.get("SearchName")

            user = None
            if search_id:
                user = get_user_by_id(search_id)
            elif search_cpf:
                user = get_user_by_cpf(search_cpf)
            elif search_name:
                user = get_user_by_name(search_name)

            if user:
                return render_template("edit_user.html", user=user)
            else:
                return "User not found", 404

        elif 'update' in request.form:
            user_id = request.form["UserId"]
            nome = request.form["UserName"]
            senha = request.form["UserConfirmPassword"]
            cpf = request.form["UserCpf"]
            telefone = request.form["UserNumberPhone"]
            data_nascimento = request.form["UserDateBirth"]
            crm = request.form["UserCrm"]
            cargo = request.form["UserCodeCarg"]
            rua = request.form["UserStreet"]
            numero_casa = request.form["UserNumberHouse"]
            bairro = request.form["UserNeighborhood"]
            complemento = request.form["UserComplement"]

            update_user_bd(
                user_id, nome, senha, cpf, telefone, data_nascimento, crm, cargo, rua, numero_casa, bairro, complemento
            )
            return redirect(url_for("edit_user.edit_user_route"))

        elif 'delete' in request.form:
            user_id = request.form["UserId"]
            delete_user_bd(user_id)
            return redirect(url_for("edit_user.edit_user_route"))

    return render_template("edit_user.html")