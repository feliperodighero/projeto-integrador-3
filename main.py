from flask import Flask
from routes.home import home_route
from routes.register_user import register_user_bp
from routes.register_patient import register_patient_bp
from routes.login import login_user
from routes.select_user_patient import select_user_patient_bp

app = Flask(__name__)
app.secret_key = "teste"
app.register_blueprint(home_route)
app.register_blueprint(register_user_bp)
app.register_blueprint(login_user)
app.register_blueprint(select_user_patient_bp)
app.register_blueprint(register_patient_bp)

app.run(debug=True)
