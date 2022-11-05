import sqlite3
import os

if __name__ == '__main__':
    conn = sqlite3.connect('instance/db.sqlite3')
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys=ON")

    cur.execute("INSERT INTO user (email, password, first_name, last_name, role) \
                VALUES ('rfg@ua.pt', '1234', 'Rafael', 'G', 'doctor')")
    conn.commit()

    cur.execute("INSERT INTO doctor VALUES(1, 'ola')")
    conn.commit()

    print(cur.execute("SELECT * FROM user").fetchall())
    print(cur.execute("SELECT * FROM doctor").fetchall())

    cur.execute("DELETE FROM user WHERE id=1")
    conn.commit()

    print(cur.execute("SELECT * FROM user").fetchall())
    print(cur.execute("SELECT * FROM doctor").fetchall())

    conn.close()
