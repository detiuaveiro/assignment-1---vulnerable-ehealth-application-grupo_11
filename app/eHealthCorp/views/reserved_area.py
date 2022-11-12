from flask import (Blueprint, render_template, session, redirect, url_for)
from eHealthCorp import get_conn

reserved_area = Blueprint("/reserved_area", __name__, template_folder="templates")

@reserved_area.route("/reserved_area", methods=["GET", "POST"])
def show():
    session_ = False
    if 'session_data' in session:
        session_ = session['session_data']['type']

    if session != 'user':
        redirect(url_for('login.show'))

    id_ = session['session_data']['id']

    conn, cur = get_conn()

    lst = []
    try:
        cur.execute("SELECT * FROM appointment WHERE doctor_id = ?", (id_,))
        appointments = cur.fetchall()
        print(appointments)

        for appointment in appointments:
            lst.append({
                'date' : appointment[2],
                'time' : appointment[3],
                'patient_email' : cur.execute("SELECT name FROM app_user WHERE id = ?", (appointment[4],)).fetchone()[1],
                'type' : appointment[5],
                'status' : appointment[6],
            })
    except:
        return render_template("error.html", error="Error while fetching data")


    return render_template("reserved_area.html", appointments=lst, session=session_)