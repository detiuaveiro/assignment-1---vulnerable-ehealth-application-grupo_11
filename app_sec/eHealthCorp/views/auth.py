from flask import (Blueprint, request, render_template, redirect, session, url_for)
from eHealthCorp import get_conn
from flask_bcrypt import Bcrypt
import re

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=('GET', 'POST'))
def register():

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        full_name = f"{first_name} {last_name}"

        # check id password has 1 uppercase, 1 lowercase, 1 number, length >= 8 with regex
        if (
            not re.search(r"[A-Z]", password)
            or not re.search(r"[a-z]", password)
            or not re.search(r"[0-9]", password)
            or len(password) < 8
        ):
            return render_template("register.html", error="Password must have 1 uppercase, 1 lowercase, 1 number, length >= 8")

        #hash password
        password_hash = Bcrypt().generate_password_hash(password).decode('utf-8')

        try:
            conn, cur = get_conn()
            cur.execute(
                "INSERT INTO app_user (email, password_, name_) \
                    VALUES (? ,?, ?);", (email, password_hash, full_name)
            )
            conn.commit()
            conn.close()
        except:
            return render_template("register.html", error="Email already exists")
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
        full_name = f"{first_name} {last_name}"

        if (
            not re.search(r"[A-Z]", password)
            or not re.search(r"[a-z]", password)
            or not re.search(r"[0-9]", password)
            or len(password) < 8
        ):
            return render_template("register.html", error="Password must have 1 uppercase, 1 lowercase, 1 number, length >= 8")

        #hash password
        password_hash = Bcrypt().generate_password_hash(password).decode('utf-8')

        try:
            conn, cur = get_conn()
            cur.execute("INSERT INTO app_user (email, password_, name_) VALUES (?, ?, ?)", (email, password_hash, full_name))
            conn.commit()
            conn.close()
        except:
            return render_template("register_doctor.html", error="Email already exists")


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
        user = cur.execute("SELECT * FROM app_user WHERE email = ?", (email,)).fetchone()
        conn.close()

        if user == None:
            return render_template("login.html", error="Invalid email")
        else:
            if not Bcrypt().check_password_hash(user[2], password):
                return render_template("login.html", error="Invalid password")

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
                "name": user[-1],
                "type": type
            }
            session["session_data"] = session_data

            if id_ == 1:
                return redirect(url_for("admin_.admin"))
            return redirect(url_for("index.show"))
        
    return render_template("login.html")



@auth.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    return redirect(url_for("index.show"))
