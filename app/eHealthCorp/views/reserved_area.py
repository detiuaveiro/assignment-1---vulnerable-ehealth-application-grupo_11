from flask import (Blueprint, render_template, session, redirect, url_for, request)
from eHealthCorp import get_conn

import os

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
                    'patient_email' : cur.execute("SELECT email FROM app_user WHERE id = ?", (appointment[4],)).fetchone()[0],
                    'type' : appointment[5],
                    'status' : appointment[6],
                })
        except:
            return render_template("error.html", error="Error while fetching data")

        return render_template("reserved_area.html", appointments=lst)

    elif request.method == "POST":
        
        patient_email = request.form['patient_email']
        file_path = request.files['results_file']


        try:
            results_file = file_path.stream.read()
            # print(results_file)

            # print("\n\n\n")
            # print(dir(file_path.stream))
            
            cur.execute("INSERT INTO test_results (patient_email, results_file) VALUES (?, ?)", (patient_email, results_file))
            conn.commit()
            conn.close()

        except:
            return render_template("error.html", error="Error while sending data")

        return redirect(url_for('/reserved_area.show'))
