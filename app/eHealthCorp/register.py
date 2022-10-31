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
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # print(f"NEW USER --- {username}, {email}, {password} ---")

        cur.execute("INSERT INTO user (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        conn.close()

        # print("New user added to the database")

        return render_template("home.html")

    return render_template("register.html")
