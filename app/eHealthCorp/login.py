from flask import Blueprint, render_template, abort
from flask import request
from eHealthCorp import db

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login', methods=["GET", "POST"]) 
def show():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        print(f"---------------------- {username}: {password}")
        return render_template("home.html")

    return render_template("login.html")

