from database.database_connect import get_database_connection


def get_user_limit(tg_id: str):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute(f"SELECT limit_unit FROM limits WHERE tg_id='{tg_id}'")
    limit = cur.fetchone()
    cur.close()
    con.close()
    return limit


def change_limit(tg_id: str, limit: str):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute(f"UPDATE limits SET limit_unit = '{limit}' WHERE tg_id='{tg_id}'")
    con.commit()
    cur.close()
    con.close()
