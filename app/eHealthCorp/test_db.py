import sqlite3

conn = sqlite3.connect('./instance/db.sqlite3')
cur = conn.cursor()
cur.execute("SELECT * FROM user")
print(cur.fetchall())