from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from database.config import engine

Session = sessionmaker(bind=engine)

def register_service_order_bd(
        client_name,
        laboratory_name,
        product_names,
        user_id,
        date_register_order,
        status_order = 1, # código do usuário logado
):
    session = Session()
    try:
        # Buscar o código do cliente
        query = text("""SELECT CD_CLI FROM CLIENTE WHERE NM_CLI = :client_name""")
        result = session.execute(query, {"client_name": client_name})
        client_code = result.scalar()
        print(client_code)

        # Buscar o código do laboratório
        query = text("""SELECT CD_LAB FROM LABORATORIO WHERE NM_LAB = :laboratory_name""")
        result = session.execute(query, {"laboratory_name": laboratory_name})
        laboratory_code = result.scalar()
        print(laboratory_code)

        inser_query = text("""INSERT INTO PEDIDO (CD_LAB, CD_USU, CD_CLI, STATUS_PED, DT_PED) VALUES (:laboratory_code, :user_id, :client_code, :status_order, :date_register_order)""")
        session.execute(inser_query, {
            "laboratory_code": laboratory_code,
            "user_id": user_id,
            "client_code": client_code,
            "status_order": status_order,
            "date_register_order": date_register_order
        })
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def search_order_bd(order_code, patient_name, order_date):
    session = Session()
    try:
        query = """
            SELECT p.CD_PED, c.NM_CLI, p.DT_PED
            FROM PEDIDO p
            JOIN CLIENTE c ON p.CD_CLI = c.CD_CLI
            WHERE 1=1
        """
        params = {}
        if order_code:
            query += " AND p.CD_PED = :order_code"
            params["order_code"] = order_code
        if patient_name:
            query += " AND c.CD_CLI = (SELECT TOP 1 CD_CLI FROM CLIENTE WHERE NM_CLI = :patient_name)"
            params["patient_name"] = patient_name
        if order_date:
            query += " AND p.DT_PED = :order_date"
            params["order_date"] = order_date

        result = session.execute(text(query), params)
        orders = result.fetchall()

        orders_list = [{"order_code": row[0], "patient_name": row[1], "order_date": row[2].strftime("%Y-%m-%d")} for row in orders]

        return orders_list

    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()
