from flask import Blueprint, render_template
from flask_login import login_required

register_laboratory_bp = Blueprint("register_laboratory", __name__)

@register_laboratory_bp.route("/register_laboratory", methods=["GET"])
@login_required
def edit_user():
    return render_template("register_laboratory.html")
