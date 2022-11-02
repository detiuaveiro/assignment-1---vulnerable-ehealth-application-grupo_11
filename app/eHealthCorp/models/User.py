from eHealthCorp import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=True, unique=True)
    password = db.Column(db.String(length=60), nullable=True)

# class Doctor(db.Model):
#     id = db.Column(db.Integer(), ForeignKey("User.id"), primary_key=True))
#     speciality = db.Column(db.String(choices=["..."]), nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    # pacient
    # doctor
    # date time
    # description

class Test(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    # pacient
    # doctor
    # file
    # description