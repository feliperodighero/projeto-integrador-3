from sqlalchemy.orm import sessionmaker
from database.config import engine
from sqlalchemy import text
from werkzeug.security import generate_password_hash

Session = sessionmaker(bind=engine)


def cadastrar_usuario(
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
