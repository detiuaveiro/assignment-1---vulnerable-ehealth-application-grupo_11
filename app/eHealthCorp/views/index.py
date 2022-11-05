from flask import (Blueprint, render_template, session)

index = Blueprint('index', __name__, template_folder='templates')


@index.route('/')
def show():
    ctx = {"user": False}

    #get session info
    if session.get("user_id"):
        ctx["user_id"] = session.get("user_id")
        ctx["first_name"] = session.get("first_name")
        ctx["last_name"] = session.get("last_name")
        ctx["role"] = session.get("role")

    print(ctx)
    return render_template('index.html', ctx=ctx)
