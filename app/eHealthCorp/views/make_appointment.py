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
            request.form['doctor_id'],
            request.form['date_'],
            request.form['time_'],
            id_,
            request.form['type_'],
            'confirmed'
        ))
        conn.commit()
    doctors = cur.execute("SELECT * FROM doctor").fetchall()
    return render_template("make_appointment.html", doctors=doctors)
