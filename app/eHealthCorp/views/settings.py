from flask import Blueprint, request, render_template, session, redirect, url_for
from eHealthCorp import get_conn

settings = Blueprint('settings', __name__)


@settings.route('/settings', methods=('GET', 'POST'))
def account_settings():
    #just in case
    if "session_data" not in session:
        return render_template("login.html")

    session_data = session["session_data"]

    if request.method == "POST":
        new_password = request.form["new_password"]
    
        conn, cur = get_conn()
        result = cur.execute("UPDATE app_user SET password_ = ? WHERE id = ?", (new_password, session_data["id"],))
        conn.commit()
        conn.close()

        #delete session_data
        session.clear()
        return redirect(url_for("auth.login"))
    
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
