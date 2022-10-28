from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ehealthcorp.db'
Bootstrap(app)
db = SQLAlchemy(app)

from eHealthCorp import routes