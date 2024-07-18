import sqlite3

conn = sqlite3.connect('usersData.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Pas TEXT NOT NULL
);
""")


