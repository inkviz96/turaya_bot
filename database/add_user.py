from database.database_connect import get_database_connection


def add_user(tg_id: str, phone: str):
    add_new_user = f"""INSERT INTO users (tg_id, phone) VALUES({tg_id}, {phone})"""

    con = get_database_connection()
    con.execute(add_new_user)
    con.commit()
    con.close()
    add_limit = f"""INSERT INTO limits (tg_id, limit_unit) VALUES({tg_id}, 10)"""

    con = get_database_connection()
    con.execute(add_limit)
    con.commit()
    con.close()

    add_limit = f"""INSERT INTO limits_alert (tg_id, limit_unit, phone) VALUES({tg_id}, 10, {phone})"""

    con = get_database_connection()
    con.execute(add_limit)
    con.commit()
    con.close()
