from flask import Blueprint, request, render_template, session
from eHealthCorp import get_conn

admin_ = Blueprint('admin_', __name__)


@admin_.route('/admin', methods=('GET', 'POST'))
def admin():

    if "session_data" not in session:
        return render_template("login.html")
    
    if session["session_data"]["id"] != 1:
        return render_template("error.html", error="You do not have permission to access this page.")

    data = []
    query= "Admin"
    if request.method == "POST":
        query = request.form["query"]
        conn, cur = get_conn()
        data = cur.execute(query).fetchall()
        conn.close()
        
    return render_template("admin.html", title=query, data=data)
