from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import login_required, login_user, logout_user

from database.models.login import login_authenticate

login_user = Blueprint("login_user", __name__)

@login_user.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["login"]
        password = request.form["password"]
        user = login_authenticate(username, password)
        if user:
            if user[6] == 1:
                return redirect(url_for("home.home"))
            else:
                flash("Sua conta está desativada. Entre em contato com o administrador.", "error")
                return redirect(url_for("login_user.login"))
        else:
            flash("Nome de usuário ou senha incorretos.", "error")
            return redirect(url_for("login_user.login"))
    return render_template("login_page.html")

@login_user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login_user.login"))
