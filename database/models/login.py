from flask_login import UserMixin, login_user
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from werkzeug.security import check_password_hash

from database.config import engine

Session = sessionmaker(bind=engine)
class User(UserMixin):
    def __init__(self, id, name, cpf):
        self.id = id
        self.name = name
        self.cpf = cpf

    def get_id(self):
        return self.id

def login_authenticate(login, password):
    session = Session()
    user = session.execute(
        text("SELECT * FROM USUARIO WHERE CD_USU = :login"),
        {"login": login},
    ).fetchone()
    if user and check_password_hash(user[2], password):
        print(user)
        user_obj = User(user[0], user[1], user[4])
        login_user(user_obj)
        return user
    return None

