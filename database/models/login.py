from sqlalchemy.orm import sessionmaker
from database.config import engine
from sqlalchemy import text
from werkzeug.security import check_password_hash


Session = sessionmaker(bind=engine)


def login_authenticate(login, password):
    session = Session()
    user = session.execute(
        text("SELECT * FROM USUARIO WHERE CD_USU = :login"),
        {"login": login},
    ).fetchone()
    print(user)
    if user and check_password_hash(user[2], password):
        return user
    return None
