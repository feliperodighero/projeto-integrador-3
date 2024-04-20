from flask import Flask
from routes.home import home_route
from routes.cadastro_usuario import cadastro_usuario
from routes.login import login_usuario

app = Flask(__name__)
app.secret_key = "teste"
app.register_blueprint(home_route)
app.register_blueprint(cadastro_usuario)
app.register_blueprint(login_usuario)

app.run(debug=True)
