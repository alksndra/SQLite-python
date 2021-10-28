import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()


class User:

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id}, {self.name}"


def get_users():
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    user_list = []
    for row in rows:
        user = User(row[1], row[0])
        user_list.append(user)
    return user_list


def print_users():
    for user in get_users():
        print(user)


def save_user(user):
    print(f"INSERT INTO users (name) VALUES ('{user.name}')")
    cur.execute(f"INSERT INTO users (name) VALUES ('{user.name}')")
    user.id = cur.lastrowid
    conn.commit()
    return user


def delete_user(user):
    print(f"DELETE FROM users WHERE id = '{user.id}'")
    cur.execute(f"DELETE FROM users WHERE id = '{user.id}'")
    conn.commit()


a = User("Vasya")


print_users()
save_user(a)
print_users()
delete_user(a)
print_users()
