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
    LaboratoryStatus=True):

    session = Session()
    try:
        query = text("""INSERT INTO LABORATORIO (NM_LAB, CNPJ, TELEFONE, STATUS_LAB, BAIRRO, RUA, NUMERO, CEP, COMPLEMENTO)
                        VALUES (:NM_LAB, :CNPJ, :TELEFONE, :STATUS_LAB, :BAIRRO, :RUA, :NUMERO, :CEP, :COMPLEMENTO)""")
        session.execute(query, {
            "NM_LAB": LaboratoryName,
            "CNPJ": LaboratoryCnpj,
            "TELEFONE": LaboratoryNumberPhone,
            "STATUS_LAB": LaboratoryStatus,
            "BAIRRO": LaboratoryNeighborhood,
            "RUA": LaboratoryStreet,
            "NUMERO": LaboratoryNumberAddress,
            "CEP": LaboratoryCep,
            "COMPLEMENTO": LaboratoryComplement
        })
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Erro ao registrar laboratorio: {e}")
    finally:
        session.close()
