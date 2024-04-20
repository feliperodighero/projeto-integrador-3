from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    current_app,
)
from database.models.login import login_authenticate
from datetime import timedelta


login_user = Blueprint("login_user", __name__)


@login_user.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["login"]
        password = request.form["password"]
        user = login_authenticate(username, password)
        if user:
            session["username"] = username
            session.permanent = True
            current_app.permanent_session_lifetime = timedelta(minutes=5)
            return redirect(url_for("home.home"))
        else:
            return redirect(url_for("login_user.login"))

    return render_template("login_page.html")
