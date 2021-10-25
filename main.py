import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()


class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name


def print_users():
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    for row in rows:
        user = User(row[0], row[1])
        print (user.id, user.name)


print_users()


test_user = User(1, "David")
print(test_user)
print(test_user.name)
