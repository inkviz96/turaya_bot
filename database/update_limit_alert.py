from database.database_connect import get_database_connection


def change_limit_alert(tg_id: str, last_update: str, phone: str):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute(
        f"UPDATE limits_aler    `t SET tg_id = '{tg_id}' AND last_update = '{last_update}' AND phone = '{phone}'"
    )
    con.commit()
    cur.close()
    con.close()
