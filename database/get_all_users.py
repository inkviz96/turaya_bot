from database.database_connect import get_database_connection


def get_all_users():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    con.close()
    return users
