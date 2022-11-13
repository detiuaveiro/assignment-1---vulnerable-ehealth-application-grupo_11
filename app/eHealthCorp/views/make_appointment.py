from flask import (Blueprint, render_template, session, redirect, url_for, request)

make_appointment = Blueprint("/make_appointment", __name__, template_folder="templates")

@make_appointment.route("/make_appointment", methods=["GET", "POST"])
def show():
    session_ = False
    if 'session_data' in session:
        session_ = session['session_data']['type']
        id_ = session['session_data']['id']

    if session_ != 'user':
        return redirect(url_for('auth.login'))

    

    return render_template("make_appointment.html")