from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from database.config import engine

Session = sessionmaker(bind=engine)


def register_patient_bd(
    ClientName,
    ClientCpf,
    ClientDateBirth,
    ClientNumberPhone,
    ClientStreet,
    ClientCep,
    ClientNumberHouse,
    ClientNeighborhood,
    ClientComplement,
    ClientDateRegister,
    ClientStatus=True,
):
    session = Session()
    try:
        query = text(
            "INSERT INTO CLIENTE (NM_CLI, CPF, STATUS_CLI, TELEFONE, BAIRRO, RUA, NUMERO, CEP, COMPLEMENTO, DT_NASC,DT_CAD) VALUES (:NM_CLI, :CPF, :STATUS_CLI, :TELEFONE, :BAIRRO, :RUA, :NUMERO, :CEP, :COMPLEMENTO, :DT_NASC, :DT_CAD)"
        )
        session.execute(
            query,
            {
                "NM_CLI": ClientName,
                "CPF": ClientCpf,
                "STATUS_CLI": ClientStatus,
                "TELEFONE": ClientNumberPhone,
                "BAIRRO": ClientNeighborhood,
                "RUA": ClientStreet,
                "NUMERO": ClientNumberHouse,
                "CEP": ClientCep,
                "COMPLEMENTO": ClientComplement,
                "DT_NASC": ClientDateBirth,
                "DT_CAD": ClientDateRegister,
            },
        )
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()
