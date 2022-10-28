from flask import Blueprint, render_template, abort
from flask import request
from eHealthCorp import db

register = Blueprint('register', __name__, template_folder='templates')


@register.route('/register', methods=["GET", "POST"])
def show():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        print(f"---→ {username}: {email} {password}")
        db.engine.execute(
            "INSERT INTO user (username, email, password) VALUES (?, ?, ?)", (username, email, password),
        )

        return render_template("home.html")

    return render_template("login.html")
