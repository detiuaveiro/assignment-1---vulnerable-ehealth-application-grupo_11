from flask import Blueprint, render_template
from flask import request


doctors = Blueprint("/doctors", __name__, template_folder="templates")

@doctors.route("/doctors", methods=["GET", "POST"])

def show():
    return render_template("doctors.html")