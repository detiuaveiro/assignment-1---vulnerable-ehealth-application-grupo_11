from flask import (Blueprint, request, render_template, redirect, session, url_for)
import mysql.connector
from eHealthCorp import db
from eHealthCorp.models import User

auth = Blueprint('auth', __name__)


def get_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root0",
        database="eHealthCorp"
    )
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
            # create user
            u = User()
            u.first_name = first_name
            u.last_name = last_name
            u.email = email
            u.password = password
            db.session.add(u)
            print("User added!")
            db.session.commit()
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
        cmd = "INSERT INTO user (email, password, first_name, last_name, role) VALUES ('{}', '{}', '{}', '{}', '{}')".format(email, password, first_name, last_name, "patient")
        print(cmd)
        cur.execute(cmd)
        conn.commit()
        conn.close()
        

        conn, cur = get_conn()
        cmd = "SELECT id FROM user WHERE email = '{}'".format(email)
        cur.execute(cmd)
        result = cur.fetchone()
        conn.close()


        conn, cur = get_conn()
        cmd = "INSERT INTO doctor (id, specialization) VALUES ('{}', '{}')".format(result[0][0], specialization)
        print(cmd)
        cur.execute(cmd)
        conn.commit()
        conn.close()

        return redirect(url_for("auth.login"))

    return render_template("register_doctor.html")


@auth.route('/login', methods=('GET', 'POST'))
@auth.route('/login/', methods=('GET', 'POST'))
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
