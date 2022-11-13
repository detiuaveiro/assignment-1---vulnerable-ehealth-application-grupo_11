from flask import Flask
import sqlite3


app = Flask(__name__)

def get_conn():
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    return conn, cur

@app.cli.command()
def reset_db():
    conn = sqlite3.connect('db.sqlite3')
    with open('eHealthCorp/schema.sql') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

@app.cli.command()
def test():
    conn, cur = get_conn()

    print(
        cur.execute(
            f"SELECT * FROM app_user "
        ).fetchall()
    )

# register the blueprints
from eHealthCorp.views.index import index
from eHealthCorp.views.auth import auth
from eHealthCorp.views.admin_ import admin_ 
from eHealthCorp.views.reserved_area import reserved_area
from eHealthCorp.views.make_appointment import make_appointment
from eHealthCorp.views.my_appointments import my_appointments
from eHealthCorp.views.test_results import test_results
from eHealthCorp.views.feedback import feedback
from eHealthCorp.views.doctors import doctors
from eHealthCorp.views.services import services
from eHealthCorp.views.contact import contact
from eHealthCorp.views.about import about

app.register_blueprint(index)
app.register_blueprint(auth)
app.register_blueprint(admin_)
app.register_blueprint(reserved_area)
app.register_blueprint(make_appointment)
app.register_blueprint(my_appointments)
app.register_blueprint(test_results)
app.register_blueprint(feedback)
app.register_blueprint(doctors)
app.register_blueprint(services)
app.register_blueprint(contact)
app.register_blueprint(about)


