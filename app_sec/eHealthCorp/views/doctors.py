from flask import (Blueprint, render_template, session, redirect, url_for, request)
from eHealthCorp import get_conn

doctors = Blueprint("/doctors", __name__, template_folder="templates")

@doctors.route("/doctors", methods=["GET", "POST"])

def show():
    conn, cur = get_conn()

    if request.method == "GET":


        try:
            cur.execute("SELECT * FROM doctor")
            doctors = cur.fetchall()
            lst = []
            for doctor in doctors:
                user = cur.execute("SELECT app_user.name_, app_user.email FROM app_user WHERE id = ?", (doctor[0],)).fetchone()
                lst.append({
                    'name': user[0],
                    'email': user[1],
                    'specialty': doctor[1],
                })
        except:
            return render_template("error.html", error="Error while fetching data")

    elif request.method == "POST":

        user_input = request.form['user_input']
        speciality = request.form['speciality']

        try:
            doctors = cur.execute(
                "SELECT app_user.name_, app_user.email, doctor.speciality \
                    FROM (doctor JOIN app_user ON doctor.id = app_user.id) \
                    WHERE app_user.name_ LIKE ? \
                    AND doctor.speciality LIKE ?" , 
                    ('%' + user_input + '%' , '%' + speciality + '%')
            ).fetchall()
            
            lst = []
            for doctor in doctors:
                lst.append({
                    'name': doctor[0],
                    'email': doctor[1],
                    'specialty': doctor[2],
                })

        except:
            return render_template(
                "error.html", 
                error=f"Error while fetching data"
            )

    return render_template("doctors.html", doctors=lst)