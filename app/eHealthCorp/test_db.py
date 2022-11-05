import sqlite3
import os

if __name__ == '__main__':
    conn = sqlite3.connect('instance/db.sqlite3')
    cur = conn.cursor()

    # cur.execute("INSERT INTO user VALUES (1, 'rfg@ua.pt', '1234', 'Rafael', 'G')")
    # conn.commit()
    #
    # print(cur.execute("SELECT * FROM user").fetchall())

    cur.execute("INSERT INTO doctor VALUES(8, 'ola')")
    conn.commit()

    print(cur.execute("SELECT * FROM doctor").fetchall())

    conn.close()
