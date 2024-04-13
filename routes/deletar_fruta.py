from flask import Blueprint, render_template, request, redirect, url_for
from database.models.fruta import deletar_frutas


deletar_route = Blueprint('deletar', __name__)

@deletar_route.route('/deletar_fruta', methods=['GET', 'POST'])
def deletar():
    if request.method == 'POST':
        fruitName = request.form['fruitName']
        deletar_frutas(fruitName)
        return redirect(url_for('deletar.deletar'))
    return render_template('deletar_fruta.html')

