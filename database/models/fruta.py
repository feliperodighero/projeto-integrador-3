from sqlalchemy.orm import sessionmaker
from database.config import engine
from sqlalchemy import text

Session = sessionmaker(bind=engine)

def cadastro_fruta(fruta_nome, fruta_quantidade):
    session = Session()
    try:
        query = text("INSERT INTO Fruta (Nome, Qtd) VALUES (:Nome, :Qtd)")
        session.execute(query, {'Nome': fruta_nome, 'Qtd': fruta_quantidade})
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def buscar_frutas():
    with engine.connect() as conn:
        query = text("SELECT Nome, Qtd FROM Fruta")
        result = conn.execute(query)
        frutas = [{'Nome': row[0], 'Qtd': row[1]} for row in result]
    return frutas

def deletar_frutas(fruta_nome):
    session = Session()
    try:
        query = text("DELETE FROM Fruta WHERE Nome = :Nome")
        session.execute(query, {'Nome': fruta_nome})
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def altera_fruta(fruta_nome, fruta_quantidade, fruta_novo_nome):
    session = Session()
    try:
        query = text("UPDATE Fruta SET Nome = :Nome, Qtd = :Qtd WHERE Nome = :Nome2")
        session.execute(query, {'Nome': fruta_novo_nome, 'Qtd': fruta_quantidade, 'Nome2': fruta_nome})
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()