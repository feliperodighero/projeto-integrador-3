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
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def get_patient_by_id(patient_id):
    session = Session()
    try:
        query = text("SELECT * FROM CLIENTE WHERE CD_CLI = :ID")
        result = session.execute(query, {"ID": patient_id}).fetchone()
        print(result)
        if result:
            return {
                "id": result[0],
                "name": result[1],
                "cpf": result[2],
                "status_cli": result[3],
                "phone": result[4],
                "neighborhood": result[5],
                "street": result[6],
                "house_number": result[7],
                "cep": result[8],
                "complement": result[9],
                "birth_date": result[10],
                "cadastro_date": result[11],
            }
        return None
    finally:
        session.close()

def get_patient_by_cpf(patient_cpf):
    session = Session()
    try:
        query = text("SELECT * FROM CLIENTE WHERE CPF = :CPF")
        result = session.execute(query, {"CPF": patient_cpf}).fetchone()
        print(result)
        if result:
            return {
                "id": result[0],
                "name": result[1],
                "cpf": result[2],
                "status_cli": result[3],
                "phone": result[4],
                "neighborhood": result[5],
                "street": result[6],
                "house_number": result[7],
                "cep": result[8],
                "complement": result[9],
                "birth_date": result[10],
                "cadastro_date": result[11],
            }
        return None
    finally:
        session.close()

def update_patient_bd(
    patient_id,
    patient_name,
    patient_cpf,
    patient_status,
    patient_phone,
    patient_neighborhood,
    patient_street,
    patient_numberHouse,
    patient_cep,
    patient_complement,
    patient_birthdate,
):
    session = Session()
    try:
        query = text(
            "UPDATE CLIENTE SET NM_CLI = :NM_CLI, CPF = :CPF, STATUS_CLI = :STATUS_CLI, TELEFONE = :TELEFONE, BAIRRO = :BAIRRO, RUA = :RUA, NUMERO = :NUMERO, CEP = :CEP, COMPLEMENTO = :COMPLEMENTO, DT_NASC = :DT_NASC WHERE CD_CLI = :ID"
        )
        session.execute(
            query,
            {
                "NM_CLI": patient_name,
                "CPF": patient_cpf,
                "STATUS_CLI": patient_status,
                "TELEFONE": patient_phone,
                "BAIRRO": patient_neighborhood,
                "RUA": patient_street,
                "NUMERO": patient_numberHouse,
                "CEP": patient_cep,
                "COMPLEMENTO": patient_complement,
                "DT_NASC": patient_birthdate,
                "ID": patient_id,
            },
        )
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()


def delete_patient_bd(patient_id):
    session = Session()
    try:
        query = text("DELETE FROM CLIENTE WHERE CD_CLI = :ID")
        session.execute(query, {"ID": patient_id})
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()