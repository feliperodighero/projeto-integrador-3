from flask import Blueprint, render_template, request, redirect, url_for, session
from database.models.user import register_user_bd
from datetime import datetime

register_user_bp = Blueprint("register_user", __name__)


@register_user_bp.route("/register_user", methods=["GET", "POST"])
def register_user_route():
    if "username" not in session:
        return redirect(url_for("login_user.login"))
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
