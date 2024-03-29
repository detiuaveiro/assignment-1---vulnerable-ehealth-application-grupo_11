from flask import Blueprint, request, render_template, session, redirect, url_for
from eHealthCorp import get_conn

settings = Blueprint('settings', __name__)


@settings.route('/settings', methods=('GET', 'POST'))
def account_settings():
    if request.method == "POST":
        email = request.form["email"]
        new_password = request.form["new_password"]
    
        conn, cur = get_conn()
        result = cur.execute("UPDATE app_user SET password_ = ? WHERE email = ?", (new_password, email,))
        conn.commit()
        conn.close()

        #delete session_data
        session.clear()
        return redirect(url_for("auth.login"))


    if "session_data" not in session:
        return render_template("login.html")

    session_data = session["session_data"]
    
    conn, cur = get_conn()
    result = cur.execute("SELECT * FROM app_user WHERE id = ?;", (session_data["id"],)).fetchone()
    conn.close()

    user_data = {
        "id": result[0],
        "first_name": result[-1].split()[0],
        "last_name": result[-1].split()[1],
        "email": result[1]
    }

    return render_template("settings.html", user_data=user_data)
