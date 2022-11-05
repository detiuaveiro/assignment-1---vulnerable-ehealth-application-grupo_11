from eHealthCorp import db

Base = db.Model  # SQLAlchemy ORM


class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.String(length=40), nullable=True, unique=True)
    password = db.Column(db.String(length=20), nullable=False)
    first_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.String(length=30), nullable=False)
    role = db.Column(db.String(length=20), nullable=False)

    # Delete on cascade
    doctor = db.relationship('doctor', backref='user', passive_deletes=True, uselist=False)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }


# Joined Table Inheritance
class Doctor(Base):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    specialization = db.Column(db.String(length=30), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'doctor'
    }


class Appointment(Base):
    id = db.Column(db.Integer(), primary_key=True)
    patient_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    doctor_id = db.Column(db.Integer(), db.ForeignKey('doctor.id'))
    date_time = db.Column(db.DateTime(), nullable=False)
    description = db.Column(db.String(length=100), nullable=False)


class Test(Base):
    id = db.Column(db.Integer(), primary_key=True)
    patient_id = db.Column(db.Integer(), db.ForeignKey('user.id'))


# class Feedback
#
