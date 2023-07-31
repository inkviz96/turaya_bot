from database.database_connect import get_database_connection


def get_limit_alert(tg_id: str, phone: str):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute(
        f"SELECT last_update FROM limits_alert WHERE tg_id='{tg_id}' AND phone='{phone}'"
    )
    limit = cur.fetchone()
    cur.close()
    con.close()
    return limit
