from flask import Blueprint, render_template
from flask import request
from eHealthCorp import db

feedback = Blueprint("/feedback", __name__, template_folder="templates")

@feedback.route("/feedback", methods=["GET", "POST"])
def show():

    return render_template("feedback.html")