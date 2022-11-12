from flask import (Blueprint, request, render_template, redirect, session, url_for)
from eHealthCorp import get_conn

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=('GET', 'POST'))
def register():

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            conn, cur = get_conn()
            cur.execute("INSERT INTO app_user (email, password_, first_name, last_name) VALUES (?, ?, ?, ?)", (email, password, first_name, last_name))
            conn.commit()
            conn.close()
        except:
            return render_template("register.html", error=True)
        else:
            return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth.route('/register_doctor', methods=('GET', 'POST'))
def register_doctor():

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        speciality = request.form["speciality"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            conn, cur = get_conn()
            cur.execute("INSERT INTO app_user (email, password_, first_name, last_name) VALUES (?, ?, ?, ?)", (email, password, first_name, last_name))
            conn.commit()
            conn.close()
        except:
            return render_template("register_doctor.html", error=True)


        conn, cur = get_conn()
        result = cur.execute("SELECT id FROM app_user WHERE email = ?", (email,)).fetchall()
        conn.close()


        conn, cur = get_conn()
        cur.execute("INSERT INTO doctor (id, speciality) VALUES (?, ?)", (result[0][0], speciality))
        conn.commit()
        conn.close()

        return redirect(url_for("auth.login"))

    return render_template("register_doctor.html")


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if "session_data" in session:
        return redirect(url_for("index.show"))

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn, cur = get_conn()
        query = f"SELECT * FROM app_user WHERE email = '{email}' AND password_ = '{password}'"
        user = cur.execute(query).fetchone()
        conn.close()

        if user == None:
            return render_template("login.html", error=True)
        else:
            #check the user type
            conn, cur = get_conn()
            exists = cur.execute("SELECT * FROM doctor WHERE id = ?", (user[0],)).fetchone()
            if exists == None:
                type = "user"
                id_ = user[0]
            else:
                type = "doctor"
                id_ = exists[0]

            session.clear()
            session_data = {
                "id": id_,
                "first_name": user[3],
                "last_name": user[4],
                "type": type
            }
            session["session_data"] = session_data

            return redirect(url_for("index.show"))
        
    return render_template("login.html")



@auth.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    return redirect(url_for("index.show"))
