from flask import Blueprint, render_template
from flask import request
from eHealthCorp import db

make_appointment = Blueprint("/make_appointment", __name__, template_folder="templates")

@make_appointment.route("/make_appointment", methods=["GET", "POST"])
def show():
    # TODO verificar se esta logado

    return render_template("make_appointment.html")