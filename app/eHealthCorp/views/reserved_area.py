from flask import Blueprint, render_template
from flask import request
from eHealthCorp import db

reserved_area = Blueprint("/reserved_area", __name__, template_folder="templates")

@reserved_area.route("/reserved_area", methods=["GET", "POST"])

def show():
    # TODO verificar se é medico

    return render_template("reserved_area.html")