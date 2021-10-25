import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()


class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id}, {self.name}"


def get_users():
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    users_list = []
    for row in rows:
        user = User(row[0], row[1])
        users_list.append(user)
    return users_list


users = get_users()


def print_users(users_list):
    for user in users_list:
        print(user)


def save_user(newname, oldname='', action='INSERT', ):
    if action == 'INSERT':
        cur.execute(f"{action} INTO users (name) VALUES ('{newname}')")
    if action == 'UPDATE':
        cur.execute(f"{action} users SET name = '{newname}' WHERE name = '{oldname}'")
    conn.commit()


def delete_user(condition):
    cur.execute(f"DELETE FROM users WHERE {condition}")
    conn.commit()


get_users()
print_users(users)

delete_user("name == 'NewVasya'")

users = get_users()
print_users(users)


