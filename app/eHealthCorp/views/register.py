from flask import Blueprint, render_template
from flask import request
import sqlite3

register = Blueprint('register', __name__, template_folder='templates')


@register.route('/register', methods=["GET", "POST"])
def show():

    #database connection
    conn = sqlite3.connect('./instance/db.sqlite3')
    cur = conn.cursor()

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]

        # print(f"NEW USER --- {first_name} {last_name}, {email}, {password} ---")

        cur.execute("INSERT INTO user (email, password, first_name, last_name) VALUES (?, ?, ?)", (email, password, first_name, last_name))
        conn.commit()
        conn.close()

        # print("New user added to the database")

        return render_template("index.html")

    return render_template("register.html")
