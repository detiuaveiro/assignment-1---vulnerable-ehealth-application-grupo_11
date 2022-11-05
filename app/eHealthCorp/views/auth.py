from flask import (Blueprint, request, render_template, redirect, session, url_for, flash)
import sqlite3

auth = Blueprint('auth', __name__)


def get_conn():
    conn = sqlite3.connect('./instance/db.sqlite3')
    cur = conn.cursor()
    return conn, cur


@auth.route('/register', methods=('GET', 'POST'))
def register():

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            conn, cur = get_conn()
            cur.execute("INSERT INTO user (email, password, first_name, last_name, role) VALUES (?, ?, ?, ?, ?)", (email, password, first_name, last_name, "patient"))
            conn.commit()
            conn.close()
        except:
            return render_template("register.html", ctx={"error": True, "error_desc": "This email already exists!"})
        else:
            return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth.route('/register_doctor', methods=('GET', 'POST'))
def register_doctor():

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        specialization = request.form["specialization"]
        email = request.form["email"]
        password = request.form["password"]

        conn, cur = get_conn()
        cur.execute("INSERT INTO user (email, password, first_name, last_name, role) VALUES (?, ?, ?, ?, ?)", (email, password, first_name, last_name, "doctor"))
        conn.commit()
        conn.close()
        

        conn, cur = get_conn()
        result = cur.execute("SELECT id FROM user WHERE email = ?", (email,)).fetchall()
        conn.close()


        conn, cur = get_conn()
        cur.execute("INSERT INTO doctor (id, specialization) VALUES (?, ?)", (result[0][0], specialization))
        conn.commit()
        conn.close()

        return redirect(url_for("auth.login"))

    return render_template("register_doctor.html")


@auth.route('/login', methods=('GET', 'POST'))
def login():

    #if the user is already logged in
    if session.get("user_id") != None:
        return redirect(url_for("index.show"))

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn, cur = get_conn()
        query = f"SELECT * FROM user WHERE email = '{email}' AND password = '{password}'"
        user = cur.execute(query).fetchone()
        conn.close()

        if user == None:
            return render_template("login.html", ctx={"fail": True})
        else:
            session.clear()
            session["user_id"] = user[0]
            session["first_name"] = user[3]
            session["last_name"] = user[4]
            session["role"] = user[-1]
            return redirect(url_for("index.show"))
        
    return render_template("login.html")



@auth.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    return redirect(url_for("index.show"))
