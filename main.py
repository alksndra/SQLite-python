import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()


class User:

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id}, {self.name}"

    def find_all():
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        user_list = []
        for row in rows:
            user = User(row[1], row[0])
            user_list.append(user)
        return user_list

    def save_user(self):
        print(f"INSERT INTO users (name) VALUES ('{self.name}')")
        cur.execute(f"INSERT INTO users (name) VALUES ('{self.name}')")
        self.id = cur.lastrowid
        conn.commit()

    def delete_user(self):
        print(f"DELETE FROM users WHERE id = '{self.id}'")
        cur.execute(f"DELETE FROM users WHERE id = '{self.id}'")
        conn.commit()


def print_users():
    for user in User.find_all():
        print(user)


a = User("Vasya")


print_users()
a.save_user()
print_users()
a.delete_user()
print_users()
