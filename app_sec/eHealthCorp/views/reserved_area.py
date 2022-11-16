from flask import (Blueprint, render_template, session, redirect, url_for, request)
from eHealthCorp import get_conn


reserved_area = Blueprint("/reserved_area", __name__, template_folder="templates")

@reserved_area.route("/reserved_area", methods=["GET", "POST"])
def show():
    session_ = False
    if 'session_data' in session:
        session_ = session['session_data']['type']
        id_ = session['session_data']['id']

    if session_ != 'doctor':
        return redirect(url_for('auth.login'))

    conn, cur = get_conn()

    if request.method == "GET":

        lst = []
        try:
            cur.execute("SELECT * FROM appointment WHERE doctor_id = ?", (id_,))
            appointments = cur.fetchall()
            print(appointments)

            lst = []
            for appointment in appointments:
                lst.append({
                    'date' : appointment[2],
                    'time' : appointment[3],
                    'patient_email' : cur.execute(
                        "SELECT email FROM app_user WHERE id = ?", 
                        (appointment[4],)
                    ).fetchone()[0],
                    'type' : appointment[5],
                    'status' : appointment[6],
                })
        except:
            return render_template("error.html", error="Error while fetching data")

        return render_template("reserved_area.html", appointments=lst)

    elif request.method == "POST":
        
        patient_email = request.form['patient_email']
        file_ = request.files['results_file']

        try:
            file_data = file_.read()          
            cur.execute(
                "INSERT INTO test_results (patient_email, file_name_, file_data) VALUES (?, ?, ?)", 
                (patient_email, file_.filename, file_data)
            )
            code = 'EHC' + str(cur.lastrowid)
            conn.commit()
            conn.close() 

        except:
            return render_template("error.html", error="Error while sending data")

        return render_template("reserved_area.html", code=code)
