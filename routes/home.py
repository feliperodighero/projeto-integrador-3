from flask import Blueprint, render_template, session, url_for, redirect


home_route = Blueprint("home", __name__)


@home_route.route("/", methods=["GET"])
def home():
    if "username" not in session:
        return redirect(url_for("login_usuario.login"))
    return render_template("home.html")
