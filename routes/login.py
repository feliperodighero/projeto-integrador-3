from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    current_app,
)
from database.models.login import autenticar_login
from datetime import timedelta


login_usuario = Blueprint("login_usuario", __name__)


@login_usuario.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["login"]
        password = request.form["password"]
        user = autenticar_login(username, password)
        if user:
            session["username"] = username
            session.permanent = True
            current_app.permanent_session_lifetime = timedelta(minutes=5)
            return redirect(url_for("home.home"))
        else:
            return redirect(url_for("login_usuario.login"))

    return render_template("login_page.html")
