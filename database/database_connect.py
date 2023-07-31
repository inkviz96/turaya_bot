import sqlite3

DB_NAME = "turaya.db"


def get_database_connection():
    con = sqlite3.connect(DB_NAME)
    return con
