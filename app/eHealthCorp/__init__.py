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
def test_db():
    conn, _ = get_conn()
    conn.execute("INSERT INTO app_user (email, password_, first_name, last_name) VALUES (?, ?, ?, ?)", ("admin", "admin", "admin", "admin"))
    conn.commit()
    conn.close()

@app.cli.command()
def leo_query():
    conn, cur = get_conn()
    cur.execute("INSERT INTO app_user (email, password_, first_name, last_name) VALUES (?, ?, ?, ?)", ("leo@gmail.com", "leo", "leo", "leo"))
    conn.commit()
    cur.execute(f"INSERT INTO doctor (id, speciality) VALUES (1,'yes')")
    conn.commit()
    cur.execute(f"INSERT INTO appointment (doctor_id, date_, time_, patient_id, type_, status_) VALUES (1,'2020-12-12','12:00',1,'yes','yes')")
    conn.commit()

    
    cur.execute("SELECT * FROM appointment WHERE doctor_id = 1")
    appointments = cur.fetchall()

    lst = []
    for appointment in appointments:
        lst.append({
            'date' : appointment[2],
            'time' : appointment[3],
            'patient_email' : cur.execute("SELECT email FROM app_user WHERE id = ?", (appointment[4],)).fetchone()[0],
            'type' : appointment[5],
            'status' : appointment[6],
        })
    print(lst)
    
    conn.close()

# register the blueprints
from eHealthCorp.views.index import index
from eHealthCorp.views.auth import auth
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
app.register_blueprint(reserved_area)
app.register_blueprint(make_appointment)
app.register_blueprint(my_appointments)
app.register_blueprint(test_results)
app.register_blueprint(feedback)
app.register_blueprint(doctors)
app.register_blueprint(services)
app.register_blueprint(contact)
app.register_blueprint(about)
