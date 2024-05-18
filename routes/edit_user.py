from flask import Blueprint, render_template
from flask_login import login_required

edit_user_bp = Blueprint("edit_user", __name__)

@edit_user_bp.route("/edit_user", methods=["GET"])
@login_required
def edit_user():
    return render_template("edit_user.html")
