from flask import Blueprint, render_template, request, redirect, url_for
from database.models.cadastro_usuario import cadastrar_usuario

cadastro_usuario = Blueprint("cadastro_usuario", __name__)


@cadastro_usuario.route("/cadastro_usuario", methods=["GET", "POST"])
def cadastro_usuario_route():
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
        data_cadastro = request.form["UserDateRegister"]
        cadastrar_usuario(
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
            data_cadastro,
        )
        return redirect(url_for("cadastro_usuario.cadastro_usuario_route"))
    return render_template("cadastro_usuario.html")
