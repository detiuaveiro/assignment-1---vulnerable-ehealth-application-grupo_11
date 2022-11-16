import sqlite3
import csv
from flask_bcrypt import Bcrypt

conn = sqlite3.connect('db.sqlite3')

reader = csv.reader(open('data/user_app.csv', 'r'))
next(reader, None)

for row in reader:
    id,email,password_,name_ = row
    password_ = Bcrypt().generate_password_hash(password_).decode('utf-8')
    conn.execute("INSERT INTO app_user (email,password_,name_) VALUES (?,?,?)",(email,password_,name_))
    conn.commit()

reader = csv.reader(open('data/doctor.csv', 'r'))
next(reader, None)

for row in reader:
    id,speciality = row
    conn.execute("INSERT INTO doctor (id,speciality) VALUES (?,?)",(id,speciality))
    conn.commit()

conn.close()
    
