from flask import Blueprint, render_template
from flask_login import login_required

edit_laboratory_bp = Blueprint("edit_laboratory", __name__)

@edit_laboratory_bp.route("/edit_laboratory", methods=["GET"])
@login_required
def edit_user():
    return render_template("edit_laboratory.html")
