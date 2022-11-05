from eHealthCorp import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)  # , autoincrement=True)
    email = db.Column(db.String(length=40), nullable=True, unique=True)
    password = db.Column(db.String(length=20), nullable=False)
    first_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.String(length=30), nullable=False)


# Joined Table Inheritance
class Doctor(User):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer(), db.ForeignKey('user.id'), primary_key=True)
    specialization = db.Column(db.String(length=30), nullable=False)


class Appointment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    patient_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    doctor_id = db.Column(db.Integer(), db.ForeignKey('doctor.id'))
    date_time = db.Column(db.DateTime(), nullable=False)
    description = db.Column(db.String(length=100), nullable=False)


class Test(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    patient_id = db.Column(db.Integer(), db.ForeignKey('user.id'))


# class Feedback
#
