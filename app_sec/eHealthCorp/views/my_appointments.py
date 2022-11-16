from flask import (Blueprint, render_template, session, redirect, url_for, request)
from eHealthCorp import get_conn


my_appointments = Blueprint("/my_appointments", __name__, template_folder="templates")

@my_appointments.route("/my_appointments", methods=["GET", "POST"])
def show():
    session_ = False
    if 'session_data' in session:
        session_ = session['session_data']['type']
        id_ = session['session_data']['id']

    if session_ != 'user':
        return redirect(url_for('auth.login'))

    if request.method == "GET":
        conn, cur = get_conn()
        resultados = cur.execute("SELECT date_, time_, app_user.id, type_, status_\
            FROM appointment JOIN app_user ON app_user.id = appointment.doctor_id\
            WHERE appointment.patient_id = ?", (id_,)).fetchall()
        conn.commit()
        conn.close()
        lst = []
        for date, time, doctor, type_, status in resultados:

            #get doctor name
            conn, cur = get_conn()
            doctor_name = cur.execute("SELECT name_ FROM app_user WHERE id = ?;", (doctor,)).fetchone()[0]
            conn.close()

            lst.append({
                'date': date,
                'time': time,
                'doctor': f"Dr. {doctor_name}",
                'type': type_,
                'status': status
            })
        
        return render_template("my_appointments.html", appointments=lst)


