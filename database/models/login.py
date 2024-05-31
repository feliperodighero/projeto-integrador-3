from functools import wraps
from flask import flash, redirect, url_for
from flask_login import UserMixin, current_user, login_user
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from werkzeug.security import check_password_hash

from database.config import engine

Session = sessionmaker(bind=engine)

class User(UserMixin):
    def __init__(self, id, name, cpf, cargo, status):
        self.id = id
        self.name = name
        self.cpf = cpf
        self.cargo = cargo
        self.status = status

    def get_id(self):
        return self.id


def login_authenticate(login, password):
    session = Session()
    user = session.execute(
        text("SELECT * FROM USUARIO WHERE CD_USU = :login"),
        {"login": login},
    ).fetchone()
    if user and check_password_hash(user[2], password):
        if user[6] == 1:
            user_obj = User(user[0], user[1], user[4], user[5], user[6])
            login_user(user_obj)
            return user
    return None


def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if current_user.is_authenticated:
                print(f"User is authenticated: {current_user.name}, Cargo: {current_user.cargo}")
                if current_user.cargo == role:
                    return fn(*args, **kwargs)
                else:
                    flash("Você não tem permissão para acessar esta página.", "error")
            else:
                flash("Você precisa estar logado para acessar esta página.", "error")
            return redirect(url_for("home.home"))
        return decorated_view
    return wrapper
