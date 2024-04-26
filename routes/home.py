from flask import Blueprint, render_template
from flask_login import login_required

home_route = Blueprint("home", __name__)

@home_route.route("/", methods=["GET"])
@login_required
def home():
    return render_template("home.html")
