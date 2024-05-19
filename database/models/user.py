from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash

from database.config import engine

Session = sessionmaker(bind=engine)


def register_user_bd(
    nome,
    senha,
    cpf,
    telefone,
    data_nascimento,
    crm,
    cargo,
    rua,
    numero_casa,
    bairro,
    complemento,
    data_cadastro,
    status_usuario=True,
):
    session = Session()
    try:
        senha_hash = generate_password_hash(senha)
        query = text(
            "INSERT INTO USUARIO (NM_USU, SENHA, CRM, CPF, CD_CARGO, STATUS_USU, TELEFONE, BAIRRO, RUA, NUMERO_CASA, COMPLEMENTO, DT_NASC, DT_CAD) VALUES (:NM_USU, :SENHA, :CRM, :CPF, :CD_CARGO, :STATUS_USU, :TELEFONE, :BAIRRO, :RUA, :NUMERO_CASA, :COMPLEMENTO, :DT_NASC, :DT_CAD) "
        )
        session.execute(
            query,
            {
                "NM_USU": nome,
                "SENHA": senha_hash,
                "CRM": crm,
                "CPF": cpf,
                "CD_CARGO": cargo,
                "STATUS_USU": status_usuario,
                "TELEFONE": telefone,
                "BAIRRO": bairro,
                "RUA": rua,
                "NUMERO_CASA": numero_casa,
                "COMPLEMENTO": complemento,
                "DT_NASC": data_nascimento,
                "DT_CAD": data_cadastro,
            },
        )
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def get_user_by_id(user_id):
    session = Session()
    try:
        query = text("SELECT * FROM USUARIO WHERE ID = :ID")
        result = session.execute(query, {"ID": user_id}).fetchone()
        return result
    finally:
        session.close()

def get_user_by_cpf(cpf):
    session = Session()
    try:
        query = text("SELECT * FROM USUARIO WHERE CPF = :CPF")
        result = session.execute(query, {"CPF": cpf}).fetchone()
        return result
    finally:
        session.close()

def get_user_by_name(name):
    session = Session()
    try:
        query = text("SELECT * FROM USUARIO WHERE NM_USU = :NM_USU")
        result = session.execute(query, {"NM_USU": name}).fetchall()
        return result
    finally:
        session.close()

def update_user_bd(
    user_id, nome, senha, cpf, telefone, data_nascimento, crm, cargo, rua, numero_casa, bairro, complemento
):
    session = Session()
    try:
        senha_hash = generate_password_hash(senha)
        query = text(
            "UPDATE USUARIO SET NM_USU = :NM_USU, SENHA = :SENHA, CPF = :CPF, TELEFONE = :TELEFONE, "
            "DT_NASC = :DT_NASC, CRM = :CRM, CD_CARGO = :CD_CARGO, RUA = :RUA, NUMERO_CASA = :NUMERO_CASA, "
            "BAIRRO = :BAIRRO, COMPLEMENTO = :COMPLEMENTO WHERE ID = :ID"
        )
        session.execute(
            query,
            {
                "NM_USU": nome,
                "SENHA": senha_hash,
                "CPF": cpf,
                "TELEFONE": telefone,
                "DT_NASC": data_nascimento,
                "CRM": crm,
                "CD_CARGO": cargo,
                "RUA": rua,
                "NUMERO_CASA": numero_casa,
                "BAIRRO": bairro,
                "COMPLEMENTO": complemento,
                "ID": user_id
            },
        )
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def delete_user_bd(user_id):
    session = Session()
    try:
        query = text("DELETE FROM USUARIO WHERE ID = :ID")
        session.execute(query, {"ID": user_id})
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()