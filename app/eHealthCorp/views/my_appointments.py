from flask import Blueprint, render_template
from flask import request


my_appointments = Blueprint("/my_appointments", __name__, template_folder="templates")

@my_appointments.route("/my_appointments", methods=["GET", "POST"])
def show():
    # TODO verificar se esta logado

    return render_template("my_appointments.html")



    # {% for appointment in appointments %}

    #                 <tr>

    #                     <td>{{ appointment.date }}</td>

    #                     <td>{{ appointment.time }}</td>

    #                     <td>{{ appointment.doctor }}</td>

    #                     <td>{{ appointment.type }}</td>

    #                     <td>{{ appointment.status }}</td>

    #                 </tr>

    #                 {% endfor %}