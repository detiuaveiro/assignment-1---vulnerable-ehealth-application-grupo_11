from flask import Blueprint, render_template
from flask import request
from eHealthCorp import db

login = Blueprint("/login", __name__, template_folder="templates")


@login.route("/login", methods=["GET", "POST"])
def show():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user_info = db.engine.execute(f"SELECT * FROM user WHERE username = '{email}' AND password = '{password}'")



        return render_template("home.html")

    return render_template("login.html")
