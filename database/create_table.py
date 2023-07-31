from database.database_connect import get_database_connection


def create_table():
    """
    Creates a table ready to accept our data.

    write code that will execute the given sql statement
    on the database
    """

    create_table = """CREATE TABLE IF NOT EXISTS users(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id TEXT NOT NULL,
        phone TEXT NOT NULL
    )
    """

    con = get_database_connection()
    con.execute(create_table)
    con.close()

    create_table = """CREATE TABLE IF NOT EXISTS limits(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id TEXT NOT NULL,
            limit_unit TEXT NOT NULL
        )
        """

    con = get_database_connection()
    con.execute(create_table)
    con.close()

    create_table = """CREATE TABLE IF NOT EXISTS limits_alert(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id TEXT NOT NULL,
                limit_unit TEXT NOT NULL,
                phone TEXT NOT NULL,
                last_update TEXT DEFAULT '' NOT NULL
            )
            """

    con = get_database_connection()
    con.execute(create_table)
    con.close()
