from eHealthCorp import db

Base = db.Model  # SQLAlchemy ORM
Column = db.Column


class User(Base):
    __tablename__ = 'user'
    id = Column(db.Integer(), primary_key=True, autoincrement=True)
    email = Column(db.String(length=40), nullable=True, unique=True)
    password = Column(db.String(length=20), nullable=False)
    first_name = Column(db.String(length=30), nullable=False)
    last_name = Column(db.String(length=30), nullable=False)
    role = Column(db.String(length=20), nullable=False)

    # Delete on cascade
    doctor = db.relationship('doctor', backref='user', passive_deletes=True, uselist=False)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }


# Joined Table Inheritance
class Doctor(Base):
    __tablename__ = 'doctor'
    id = Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    specialization = Column(db.String(length=30), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'doctor'
    }


class Appointment(Base):
    id = Column(db.Integer(), primary_key=True)
    patient_id = Column(db.Integer(), db.ForeignKey('user.id'))
    doctor_id = Column(db.Integer(), db.ForeignKey('doctor.id'))
    date_time = Column(db.DateTime(), nullable=False)
    description = Column(db.String(length=100), nullable=False)


class Test(Base):
    id = Column(db.Integer(), primary_key=True)
    patient_id = Column(db.Integer(), db.ForeignKey('user.id'))


class Feedback(Base):
    # response to a test
    id = Column(db.Integer(), primary_key=True)
    test_id = Column(db.Integer(), db.ForeignKey('test.id'))
    doctor_id = Column(db.Integer(), db.ForeignKey('doctor.id'))
    description = Column(db.String(length=100), nullable=False)
    date_time = Column(db.DateTime(), nullable=False)
