from flask import (Blueprint, render_template, session, redirect, url_for, request)
from eHealthCorp import get_conn

make_appointment = Blueprint("/make_appointment", __name__, template_folder="templates")

@make_appointment.route("/make_appointment", methods=["GET", "POST"])
def show():
    session_ = False
    if 'session_data' in session:
        session_ = session['session_data']['type']
        id_ = session['session_data']['id']

    if session_ != 'user':
        return redirect(url_for('auth.login'))
    
    conn, cur = get_conn()

    if request.method == "POST":
        cur.execute("INSERT INTO appointment (doctor_id, date_, time_, patient_id, type_, status_) VALUES (?, ?, ?, ?, ?, ?)",(
            request.form['doctor'],
            request.form['date'],
            request.form['time'],
            id_,
            request.form['speciality'],
            'Confirmed'
        ))
        conn.commit()
        return redirect(url_for('/my_appointments.show'))

    # select doctors and join with users
    results = cur.execute("SELECT app_user.id, app_user.name_, doctor.speciality \
                    FROM (doctor JOIN app_user ON doctor.id = app_user.id)").fetchall()
    lst = []
    for id_, name, speciality in results:
        lst.append({
            'id': id_,
            'name': name,
            'speciality': speciality # está a dar empty string
        })
    conn.close()
    return render_template("make_appointment.html", doctors=lst)
