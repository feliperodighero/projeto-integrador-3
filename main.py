from flask import Flask
from routes.home import home_route
from routes.cadastro_usuario import cadastro_usuario

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(cadastro_usuario)

app.run(debug=True)