from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cursor = sqlite3.connect('./instance/db.sqlite3').cursor()

from eHealthCorp.models.User import User


@app.cli.command()
def create_db():
    db.create_all()
    print('Database created!')


@app.cli.command()
def drop_db():
    db.drop_all()
    print('Database deleted!')


@app.cli.command()
def show_tables():
    print(db.engine.table_names())


@app.cli.command()
def show_users():
    username = "' or 1=1 -- ; DROP TABLE user; -- //"
    password = 'hard_code_porque_eu_quero'
    query = f"SELECT * FROM user WHERE username = '{username}' AND password = {password}"
    print(cursor.executescript(query).fetchall())


# register the blueprints
from eHealthCorp.views.index import index
from eHealthCorp.views.login import login
from eHealthCorp.views.register import register

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(register)
