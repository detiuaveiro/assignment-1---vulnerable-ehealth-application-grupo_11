from flask import Blueprint, render_template
from flask import request
from eHealthCorp import db

doctors = Blueprint("/doctors", __name__, template_folder="templates")

@doctors.route("/doctors", methods=["GET", "POST"])

def show():
    return render_template("doctors.html")


    # {% for doctor in doctors %}

    #                 <tr>

    #                     <td>{{ doctor.name }}</td>

    #                     <td>{{ doctor.email }}</td>

    #                     <td>{{ doctor.specialty }}</td>

    #                 </tr>

    #                 {% endfor %}