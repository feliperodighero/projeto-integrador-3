from flask import Blueprint, render_template
from flask_login import login_required, current_user

home_route = Blueprint("home", __name__)

@home_route.route("/", methods=["GET"])
@login_required
def home():
    user_data = {
        "name": current_user.name,
        "id": current_user.id,
        "cpf": current_user.cpf
    }
    return render_template("home.html", user_data=user_data)
