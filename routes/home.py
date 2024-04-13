from flask import Blueprint, render_template, request, redirect, url_for
from database.models.fruta import cadastro_fruta, buscar_frutas


home_route = Blueprint('home', __name__)

@home_route.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        fruitName = request.form['fruitName']
        fruitQuantity = request.form['fruitQuantity']
        cadastro_fruta(fruitName, fruitQuantity)
        return redirect(url_for('home.home'))
    return render_template('home.html')

@home_route.route('/listar_frutas', methods=['GET'])
def listar_frutas():
    frutas = buscar_frutas()
    return render_template('listar_frutas.html', frutas=frutas)