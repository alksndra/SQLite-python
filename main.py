import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()


def print_users():
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    for row in rows:
        print (row)


print_users()


class Users:

    def __init__(self, id, name):
        self.id = id
        self.name = name


test_user = Users(1, "David")
print(test_user)
print(test_user.name)
