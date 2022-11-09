import mysql.connector

if __name__ == '__main__':
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root0",
        database="eHealthCorp"
    )
    cur = conn.cursor()

    cur.execute("INSERT INTO user (id, email, password, first_name, last_name, role) \
                VALUES (1, 'rfg@ua.pt', '1234', 'Rafael', 'G', 'doctor')")
    conn.commit()

    cur.execute("INSERT INTO doctor (id, speciality) VALUES(1, 'ola')")
    conn.commit()

    cur.execute("SELECT * FROM user")
    print(cur.fetchall())
    cur.execute("SELECT * FROM doctor")
    print(cur.fetchall())

    cur.execute("DELETE FROM user WHERE id=1")
    conn.commit()

    cur.execute("SELECT * FROM user")
    print(cur.fetchall())
    cur.execute("SELECT * FROM doctor")
    print(cur.fetchall())

    conn.close()
