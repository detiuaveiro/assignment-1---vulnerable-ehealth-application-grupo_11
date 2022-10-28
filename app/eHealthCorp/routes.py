from eHealthCorp import app
from flask import render_template
# import models

@app.route("/")
def index():
    return "Hello, World!"
