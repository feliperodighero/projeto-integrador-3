from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from database.models.service_order import register_service_order_bd, search_order_bd

service_order_route = Blueprint("service_order", __name__)

@service_order_route.route("/service_order", methods=["GET", "POST"])
@login_required
def service_order():
    if request.method == "POST":
        client_name = request.form.get("ClientName")
        laboratory_name = request.form.get("LaboratoryName")
        items = request.form.getlist("ItemName")
        date_register = datetime.now()  # Obter todos os itens selecionados
        print(client_name, laboratory_name, items, current_user.id)

        register_service_order_bd(client_name, laboratory_name, items, current_user.id, date_register)


        flash("Ordem de serviço cadastrada com sucesso!", "success")
        return redirect(url_for("service_order.service_order"))

    return render_template("service_order.html")

@service_order_route.route("/search_orders", methods=["POST"])
@login_required
def search_orders():
    data = request.get_json()
    order_code = data.get("OrderCode")
    patient_name = data.get("PatientName")
    order_date = data.get("OrderDate")
    print(order_code, patient_name, order_date)

    orders_list = search_order_bd(order_code, patient_name, order_date)

    return jsonify({"orders": orders_list})
