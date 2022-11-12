from flask import Blueprint, request, render_template, session
from eHealthCorp import get_conn
from datetime import datetime

feedback = Blueprint("/feedback", __name__, template_folder="templates")

@feedback.route("/feedback", methods=["GET", "POST"])
def show():
    if "session_data" in session:
        session_data = session["session_data"]

    if request.method == "POST":
        user_id = session_data["id"]
        message = request.form["message"]
        time = datetime.now().strftime("%B %d, %Y %I:%M%p")

        #insert feedback into db 
        conn, cur = get_conn()
        sql = f"INSERT INTO feedback (user, feedback, date_time) VALUES ('{user_id}', '{message}', '{time}');"
        cur.execute(sql)
        conn.commit()
        conn.close()

    #get all the feedbacks from the db
    conn, cur = get_conn()
    messages = cur.execute("SELECT * FROM feedback;").fetchall()
    conn.close()

    feedback_lst = []
    for m in messages:

        #get user info
        conn, cur = get_conn()
        user = cur.execute("SELECT first_name, last_name FROM app_user WHERE id = ?", (m[1],)).fetchone()
        conn.close()

        feedback_lst.append({
            "author": f"{user[0]} {user[1]}",
            "message": m[2],
            "date_time": m[-1]
        })

    return render_template("feedback.html", feedback=feedback_lst)
