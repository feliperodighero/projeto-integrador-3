from flask import Flask
from flask_login import LoginManager
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from database.config import engine
from database.models.login import User
from routes.home import home_route
from routes.service_order import service_order_route
from routes.login import login_user
from routes.register_patient import register_patient_bp
from routes.register_user import register_user_bp
from routes.select_user_patient import select_user_patient_bp
from routes.edit_patient import edit_patient_bp
from routes.edit_user import edit_user_bp
from routes.register_laboratory import register_laboratory_bp
from routes.edit_laboratory import edit_laboratory_bp

login_manager = LoginManager()

Session = sessionmaker(bind=engine)

@login_manager.user_loader
def load_user(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.execute(
        text("SELECT * FROM USUARIO WHERE CD_USU = :user_id"),
        {"user_id": user_id},
    ).fetchone()
    if user:
        return User(user[0], user[1], user[4])
    return None

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
login_manager.init_app(app)
login_manager.login_view = 'login_user.login'
app.register_blueprint(home_route)
app.register_blueprint(register_user_bp)
app.register_blueprint(login_user)
app.register_blueprint(select_user_patient_bp)
app.register_blueprint(register_patient_bp)
app.register_blueprint(edit_patient_bp)
app.register_blueprint(edit_user_bp)
app.register_blueprint(register_laboratory_bp)
app.register_blueprint(edit_laboratory_bp)
app.register_blueprint(service_order_route)

app.run(debug=True)
