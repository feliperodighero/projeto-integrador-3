from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from database.models.user import (
    get_user_by_id,
    get_user_by_cpf,
    update_user_bd,
    delete_user_bd,
)
from database.models.login import role_required

edit_user_bp = Blueprint("edit_user", __name__, template_folder="templates")


@edit_user_bp.route("/edit_user", methods=["GET", "POST"])
@login_required
@role_required(1)
def edit_user_route():
    if request.method == "POST":
        if "search" in request.form:
            search_id = request.form.get("SearchID")
            search_cpf = request.form.get("SearchCpfCnpj")

            user = None
            if search_id:
                user = get_user_by_id(search_id)
            elif search_cpf:
                user = get_user_by_cpf(search_cpf)

            if user:
                return render_template("edit_user.html", user=user)
            else:
                flash("Usuário não encontrado", "danger")
                return render_template("edit_user.html")

        elif "update" in request.form:
            user_id = request.form.get("UserId")
            user_data = {
                "name": request.form.get("UserName"),
                "password": request.form.get("UserPassword"),
                "cpf": request.form.get("UserCpf"),
                "phone": request.form.get("UserNumberPhone"),
                "complement": request.form.get("UserComplement"),
                "birth_date": request.form.get("UserDateBirth"),
                "crm": request.form.get("UserCrm"),
                "code_carg": request.form.get("UserCodeCarg"),
                "street": request.form.get("UserStreet"),
                "house_number": request.form.get("UserNumberHouse"),
                "neighborhood": request.form.get("UserNeighborhood"),
                "status_usu": request.form.get("UserStatus"),
            }

            # Verificar se todas as chaves estão presentes
            missing_keys = [key for key in user_data if not user_data[key]]
            if missing_keys:
                flash(f"Faltando dados nos campos: {', '.join(missing_keys)}", "danger")
                return render_template("edit_user.html", user=user_data)

            # Verificar se as senhas correspondem
            if user_data["password"] != request.form.get("UserConfirmPassword"):
                flash("As senhas não correspondem", "danger")
                return render_template("edit_user.html", user=user_data)

            update_user_bd(
                user_id,
                user_data["name"],
                user_data["password"],
                user_data["cpf"],
                user_data["phone"],
                user_data["birth_date"],
                user_data["crm"],
                user_data["code_carg"],
                user_data["street"],
                user_data["house_number"],
                user_data["neighborhood"],
                user_data["complement"],
                user_data["status_usu"],
            )
            flash("Usuário atualizado com sucesso", "success")
            return redirect(url_for("edit_user.edit_user_route"))

        elif "delete" in request.form:
            user_id = request.form["UserId"]
            delete_user_bd(user_id)
            flash("Usuário excluído com sucesso", "success")
            return redirect(url_for("edit_user.edit_user_route"))

    return render_template("edit_user.html")
