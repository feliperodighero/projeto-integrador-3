from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from database.config import engine

Session = sessionmaker(bind=engine)


def register_laboratory_bd(
    LaboratoryName,
    LaboratoryStreet,
    LaboratoryComplement,
    LaboratoryCnpj,
    LaboratoryCep,
    LaboratoryNumberPhone,
    LaboratoryNumberAddress,
    LaboratoryNeighborhood,
    LaboratoryStatus=True,
):
    session = Session()
    try:
        # Verifique se o laboratório já existe
        if check_laboratory_exists(LaboratoryCnpj):
            print("Laboratório com esse CNPJ já existe.")
            return False  # Ou você pode levantar uma exceção ou retornar uma mensagem de erro

        query = text(
            """EXEC InsertLaboratorio :NM_LAB, :CNPJ, :TELEFONE, :STATUS_LAB, :BAIRRO, :RUA, :NUMERO, :CEP, :COMPLEMENTO"""
        )
        session.execute(
            query,
            {
                "NM_LAB": LaboratoryName,
                "CNPJ": LaboratoryCnpj,
                "TELEFONE": LaboratoryNumberPhone,
                "STATUS_LAB": LaboratoryStatus,
                "BAIRRO": LaboratoryNeighborhood,
                "RUA": LaboratoryStreet,
                "NUMERO": LaboratoryNumberAddress,
                "CEP": LaboratoryCep,
                "COMPLEMENTO": LaboratoryComplement,
            },
        )
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro ao registrar laboratório: {e}")
        return False
    finally:
        session.close()


def get_laboratory_by_id_bd(laboratory_id):
    session = Session()
    try:
        query = text("SELECT * FROM LABORATORIO WHERE CD_LAB = :ID")
        result = session.execute(query, {"ID": laboratory_id}).fetchone()
        print(result)
        if result:
            return {
                "id": result[0],
                "name": result[1],
                "cnpj": result[2],
                "number_phone": result[3],
                "status": result[4],
                "neighborhood": result[5],
                "street": result[6],
                "number_address": result[7],
                "cep": result[8],
                "complement": result[9],
            }
    except Exception as e:
        print(f"Erro ao buscar laboratorio: {e}")
    finally:
        session.close()


def get_laboratory_by_cnpj_bd(laboratory_cnpj):
    session = Session()
    try:
        query = text("SELECT * FROM LABORATORIO WHERE CNPJ = :CNPJ")
        result = session.execute(query, {"CNPJ": laboratory_cnpj}).fetchone()
        print(result)
        if result:
            return {
                "id": result[0],
                "name": result[1],
                "cnpj": result[2],
                "number_phone": result[3],
                "status": result[4],
                "neighborhood": result[5],
                "street": result[6],
                "number_address": result[7],
                "cep": result[8],
                "complement": result[9],
            }
    except Exception as e:
        print(f"Erro ao buscar laboratorio: {e}")
    finally:
        session.close()


def update_laboratory_bd(
    laboratory_id,
    laboratory_name,
    laboratory_cnpj,
    laboratory_number_phone,
    laaboratory_neighborhood,
    laboratory_street,
    laboratory_number_address,
    laboratory_cep,
    laboratory_complement,
    LaboratoryStatus=True,
):
    session = Session()
    try:
        query = text(
            """EXEC UpdateLaboratorio :ID, :NM_LAB, :CNPJ, :TELEFONE, :STATUS_LAB, :BAIRRO, :RUA, :NUMERO, :CEP, :COMPLEMENTO"""
        )
        session.execute(
            query,
            {
                "ID": laboratory_id,
                "NM_LAB": laboratory_name,
                "CNPJ": laboratory_cnpj,
                "TELEFONE": laboratory_number_phone,
                "STATUS_LAB": LaboratoryStatus,
                "BAIRRO": laaboratory_neighborhood,
                "RUA": laboratory_street,
                "NUMERO": laboratory_number_address,
                "CEP": laboratory_cep,
                "COMPLEMENTO": laboratory_complement,
            },
        )
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Erro ao atualizar laboratorio: {e}")
    finally:
        session.close()


def delete_laboratory_bd(laboratory_id):
    session = Session()
    try:
        query = text("DELETE FROM LABORATORIO WHERE CD_LAB = :ID")
        session.execute(query, {"ID": laboratory_id})
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Erro ao deletar laboratorio: {e}")
    finally:
        session.close()


def check_laboratory_exists(cnpj):
    session = Session()
    try:
        query = text("SELECT COUNT(1) FROM LABORATORIO WHERE CNPJ = :CNPJ")
        result = session.execute(query, {"CNPJ": cnpj}).scalar()
        return result > 0
    except Exception as e:
        print(f"Erro ao verificar se laboratório existe: {e}")
        return False
    finally:
        session.close()
