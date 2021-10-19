import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()


def print_users():
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    for row in rows:
        print (row)


print_users()
