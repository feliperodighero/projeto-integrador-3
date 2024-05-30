from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required
from database.models.user import register_user_bd
from database.models.login import role_required

register_user_bp = Blueprint("register_user", __name__)


@register_user_bp.route("/register_user", methods=["GET", "POST"])
@login_required
# @role_required(1)
def register_user_route():
    if request.method == "POST":
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
        data_register = datetime.now()
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
