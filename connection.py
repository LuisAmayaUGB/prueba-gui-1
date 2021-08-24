import sqlite3


def Database():
    global conn, cursor
    conn = sqlite3.connect('db_member.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT, address TEXT, username TEXT, password TEXT)")
