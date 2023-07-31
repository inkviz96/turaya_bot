from database.database_connect import get_database_connection


def get_user_phones(tg_id: str):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute(f"SELECT phone FROM users WHERE tg_id='{tg_id}'")
    user = cur.fetchall()
    cur.close()
    con.close()
    return user


def delete_phone(tg_id: str, phone: str):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute(f"DELETE FROM users WHERE tg_id='{tg_id}' AND phone='{phone}'")
    con.commit()
    cur.close()
    con.close()
