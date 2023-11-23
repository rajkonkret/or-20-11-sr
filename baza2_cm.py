import sqlite3


class SQLiteDBContextManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    # wykonuje przed włąsciwym zadaniem
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    # wykonuje sie niezależnie od tego czy był bład czy nie było
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.commit()
            self.conn.close()


lista = []
db_name = "my_database.db"

with SQLiteDBContextManager(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT)")

    cursor.execute("INSERT INTO users (name) VALUES (?)", ("John",))
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))

    select = cursor.execute("SELECT * FROM users")
    for i in select:
        print(i)
        lista.append(i)

print(lista)
# [(1, 'John'), (2, 'John'), (3, 'Alice'),
#  (4, 'John'), (5, 'Alice'), (6, 'John'), (7, 'Alice')]
# wyswietli dane z listy w formie id name 5 Alice
