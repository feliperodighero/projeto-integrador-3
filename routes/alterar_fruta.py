from flask import Blueprint, render_template, request, redirect, url_for
from database.models.fruta import altera_fruta


alterar_route = Blueprint('alterar', __name__)

@alterar_route.route('/alterar_fruta', methods=['GET', 'POST'])
def alterar():
    if request.method == 'POST':
        fruitName = request.form['fruitName']
        fruitQuantity = request.form['fruitQuantity']
        fruitNewName = request.form['fruitNewName']
        altera_fruta(fruitName, fruitQuantity, fruitNewName)
        return redirect(url_for('alterar.alterar'))
    return render_template('alterar_fruta.html')

