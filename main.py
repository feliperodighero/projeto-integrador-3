from flask import Flask
from routes.home import home_route
from routes.deletar_fruta import deletar_route
from routes.alterar_fruta import alterar_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(deletar_route)
app.register_blueprint(alterar_route)

app.run(debug=True)