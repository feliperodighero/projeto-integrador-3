from flask import Blueprint, render_template

cadastro_usuario = Blueprint('cadastro_usuario', __name__)

@cadastro_usuario.route('/cadastro_usuario', methods=['GET', 'POST'])
def cadastro_usuario_route():
    return render_template('cadastro_usuario.html')
