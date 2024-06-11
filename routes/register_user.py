from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for, jsonify
from flask_login import login_required
from database.models.user import register_user_bd, get_user_by_cpf, get_user_by_crm
from database.models.login import role_required

register_user_bp = Blueprint("register_user", __name__)


@register_user_bp.route("/register_user", methods=["GET", "POST"])
@login_required
@role_required(1)
def register_user_route():
    if request.method == "POST":
        nome = request.form["UserName"]
        senha = request.form["UserConfirmPassword"]
        cpf = request.form["UserCpf"]
        telefone = request.form["UserNumberPhone"]
        data_nascimento = request.form["UserDateBirth"]
        crm = request.form.get("UserCrm")
        cargo = request.form["UserCodeCarg"]
        rua = request.form["UserStreet"]
        numero_casa = request.form["UserNumberHouse"]
        bairro = request.form["UserNeighborhood"]
        complemento = request.form["UserComplement"]
        data_register = datetime.now()

        crm = crm if crm else None

        register_user_bd(
            nome,
            senha,
            cpf,
            telefone,
            data_nascimento,
            crm,
            cargo,
            rua,
            numero_casa,
            bairro,
            complemento,
            data_register,
        )
        return redirect(url_for("register_user.register_user_route"))
    return render_template("register_user.html")


@register_user_bp.route("/check_user_existence", methods=["POST"])
def check_user_existence():
    data = request.json
    cpf = data.get("UserCpf")
    crm = data.get("UserCrm", "N/A")  # Default value for 'UserCrm'

    if not cpf:
        return jsonify({"error": "UserCpf is required"}), 400

    cpf_exists = get_user_by_cpf(cpf) is not None
    crm_exists = crm != "N/A" and get_user_by_crm(crm) is not None

    return jsonify({"exists": cpf_exists or crm_exists})
