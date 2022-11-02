from flask import Blueprint, render_template
from flask import request
from eHealthCorp import db

test_results = Blueprint("/test_results", __name__, template_folder="templates")

@test_results.route("/test_results", methods=["GET", "POST"])
def show():
    # TODO verificar se esta logado

    return render_template("test_results.html")