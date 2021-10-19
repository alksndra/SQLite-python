import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()


def get_users():
    with conn:
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for row in rows:
            print (row)


get_users()
