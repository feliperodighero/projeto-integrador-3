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
            "INSERT INTO USUARIO (NM_USU, SENHA, CRM, CPF, CD_CARGO, STATUS_USU, TELEFONE, BAIRRO, RUA, NUMERO_CASA, COMPLEMENTO, DT_NASC, DT_CAD) VALUES (:NM_USU, :SENHA, :CRM, :CPF, :CD_CARGO, :STATUS_USU, :TELEFONE, :BAIRRO, :RUA, :NUMERO_CASA, :COMPLEMENTO, :DT_NASC, :DT_CAD)"
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
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
        raise
    finally:
        session.close()


def get_user_by_id(user_id):
    session = Session()
    try:
        query = text("SELECT * FROM USUARIO WHERE CD_USU = :ID")
        result = session.execute(query, {"ID": user_id}).fetchone()
        if result:
            return {
                "id": result[0],
                "name": result[1],
                "password": result[2],
                "crm": result[3],
                "cpf": result[4],
                "code_carg": result[5],
                "status_usu": result[6],
                "phone": result[7],
                "neighborhood": result[8],
                "street": result[9],
                "house_number": result[10],
                "complement": result[11],
                "birth_date": result[12],
                "cadastro_date": result[13],
            }
        return None
    finally:
        session.close()


def get_user_by_cpf(cpf):
    session = Session()
    try:
        query = text("SELECT * FROM USUARIO WHERE CPF = :CPF")
        result = session.execute(query, {"CPF": cpf}).fetchone()
        if result:
            return {
                "id": result[0],
                "name": result[1],
                "password": result[2],
                "crm": result[3],
                "cpf": result[4],
                "code_carg": result[5],
                "status_usu": result[6],
                "phone": result[7],
                "neighborhood": result[8],
                "street": result[9],
                "house_number": result[10],
                "complement": result[11],
                "birth_date": result[12],
                "cadastro_date": result[13],
            }
        return None
    finally:
        session.close()


def update_user_bd(
    user_id,
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
    status_usu,
):
    if status_usu == "Ativo":
        status_usu = True
    else:
        status_usu = False
    session = Session()
    try:
        senha_hash = generate_password_hash(senha)
        query = text(
            "UPDATE USUARIO SET NM_USU = :NM_USU, SENHA = :SENHA, CRM = :CRM, CPF = :CPF, "
            "CD_CARGO = :CD_CARGO, STATUS_USU = :STATUS_USU, TELEFONE = :TELEFONE, BAIRRO = :BAIRRO, RUA = :RUA, "
            "NUMERO_CASA = :NUMERO_CASA, COMPLEMENTO = :COMPLEMENTO, DT_NASC = :DT_NASC WHERE CD_USU = :ID"
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
                "STATUS_USU": status_usu,
                "ID": user_id,
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
        query = text("DELETE FROM USUARIO WHERE CD_USU = :ID")
        session.execute(query, {"ID": user_id})
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def get_user_by_crm(crm):
    session = Session()
    try:
        query = text("SELECT * FROM USUARIO WHERE CRM = :CRM")
        result = session.execute(query, {"CRM": crm}).fetchone()
        if result:
            return {
                "id": result[0],
                "name": result[1],
                "password": result[2],
                "crm": result[3],
                "cpf": result[4],
                "code_carg": result[5],
                "status_usu": result[6],
                "phone": result[7],
                "neighborhood": result[8],
                "street": result[9],
                "house_number": result[10],
                "complement": result[11],
                "birth_date": result[12],
                "cadastro_date": result[13],
            }
        return None
    finally:
        session.close()
