import locale
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
    value_order,
    status_order=1,
):
    session = Session()
    print(product_names)
    try:
        # Buscar o código do cliente
        query = text("""SELECT CD_CLI FROM CLIENTE WHERE NM_CLI = :client_name""")
        result = session.execute(query, {"client_name": client_name})
        client_code = result.scalar()
        print(client_code)

        # Buscar o código do laboratório
        query = text(
            """SELECT CD_LAB FROM LABORATORIO WHERE NM_LAB = :laboratory_name"""
        )
        result = session.execute(query, {"laboratory_name": laboratory_name})
        laboratory_code = result.scalar()
        print(laboratory_code)

        # Inserir o pedido na tabela PEDIDO e recuperar o código inserido
        insert_query = text("""
            INSERT INTO PEDIDO (CD_LAB, CD_USU, CD_CLI, STATUS_PED, DT_PED, VLR_TOTAL)
            OUTPUT inserted.CD_PED
            VALUES (:laboratory_code, :user_id, :client_code, :status_order, :date_register_order, :vlr_total)
        """)
        result = session.execute(
            insert_query,
            {
                "laboratory_code": laboratory_code,
                "user_id": user_id,
                "client_code": client_code,
                "status_order": status_order,
                "date_register_order": date_register_order,
                "vlr_total": value_order,
            },
        )
        pedido_code = result.scalar()
        print(pedido_code)

        if not pedido_code:
            raise ValueError("Falha ao obter o código do pedido.")

        # Inserir itens na tabela PEDIDO_IT
        for product_name in product_names:
            # Buscar o código do produto
            product_code_query = text(
                """SELECT CD_PROD FROM PRODUTO WHERE NM_PROD = :product_name"""
            )
            result = session.execute(product_code_query, {"product_name": product_name})
            product_code = result.scalar()
            print(product_code)

            # Inserir o item do pedido na tabela PEDIDO_IT
            insert_item_query = text(
                """INSERT INTO PEDIDO_IT (CD_PED, CD_PROD) VALUES (:pedido_code, :product_code)"""
            )
            session.execute(
                insert_item_query,
                {"pedido_code": pedido_code, "product_code": product_code},
            )

        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()


# Formatação da moeda
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


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

        orders_list = [
            {
                "order_code": row[0],
                "patient_name": row[1],
                "order_date": row[2].strftime("%Y-%m-%d"),
            }
            for row in orders
        ]

        return orders_list

    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()


def get_order_details(order_code):
    session = Session()
    try:
        query = text("""
            SELECT
                p.CD_PED,
                p.CD_LAB,
                l.NM_LAB,
                p.CD_USU,
                u.NM_USU,
                p.CD_CLI,
                c.NM_CLI,
                p.STATUS_PED,
                p.DT_PED,
                p.VLR_TOTAL
            FROM
                PEDIDO p
            JOIN
                LABORATORIO l ON p.CD_LAB = l.CD_LAB
            JOIN
                USUARIO u ON p.CD_USU = u.CD_USU
            JOIN
                CLIENTE c ON p.CD_CLI = c.CD_CLI
            WHERE
                p.CD_PED = :order_code
        """)
        result = session.execute(query, {"order_code": order_code}).fetchone()

        if not result:
            return None

        order_details = {
            "order_code": result[0],
            "lab_code": result[1],
            "lab_name": result[2],
            "user_code": result[3],
            "user_name": result[4],
            "client_code": result[5],
            "client_name": result[6],
            "order_status": result[7],
            "order_date": result[8].strftime("%Y-%m-%d"),
            "total_value": locale.currency(result[9], grouping=True),
        }

        items_query = text("""
            SELECT i.CD_PROD, p.NM_PROD
            FROM PEDIDO_IT i
            JOIN PRODUTO p ON i.CD_PROD = p.CD_PROD
            WHERE i.CD_PED = :order_code
        """)
        items_result = session.execute(
            items_query, {"order_code": order_code}
        ).fetchall()

        order_items = [
            {"product_code": item[0], "product_name": item[1]} for item in items_result
        ]
        order_details["items"] = order_items

        return order_details

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        session.close()


def update_order_status(order_code, new_status):
    session = Session()
    try:
        query = text("""
            UPDATE PEDIDO
            SET STATUS_PED = :new_status
            WHERE CD_PED = :order_code
        """)
        session.execute(query, {"new_status": new_status, "order_code": order_code})
        session.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
        return False
    finally:
        session.close()


def search_patients_by_name(name):
    session = Session()
    try:
        query = text("""
            SELECT CD_CLI, NM_CLI
            FROM CLIENTE
            WHERE NM_CLI LIKE :name
            ORDER BY NM_CLI
        """)
        results = session.execute(query, {"name": f"%{name}%"}).fetchall()
        print(results)
        patients = [{"id": row[0], "name": row[1]} for row in results]
        return patients
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        session.close()


def get_patient_details_by_id(patient_id):
    session = Session()
    try:
        query = text("""SELECT * FROM [dbo].[GetPatientDetailsById](:patient_id)""")
        result = session.execute(query, {"patient_id": patient_id}).fetchone()
        if result:
            return {
                "name": result[0],
                "cpf": result[1],
                "dob": result[2].strftime("%Y-%m-%d") if result[2] else None,
            }
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        session.close()
