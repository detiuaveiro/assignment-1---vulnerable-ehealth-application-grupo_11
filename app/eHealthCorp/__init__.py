from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root0@localhost:3306/eHealthCorp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from eHealthCorp.models import *

@app.cli.command()
def create_db():
    db.engine.execute("CREATE DATABASE IF NOT EXISTS eHealthCorp")
    db.create_all()
    print("Database created!")

@app.cli.command()
def drop_db():
    db.drop_all()
    print("Database deleted!")


@app.cli.command()
def show_tables():
    print(db.engine.table_names())


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
