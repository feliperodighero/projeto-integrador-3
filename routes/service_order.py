from flask import Blueprint, render_template
from flask_login import login_required

service_order_route = Blueprint("service_order", __name__)

@service_order_route.route("/service_order", methods=["GET"])
@login_required
def service_order():
    return render_template("service_order.html")
