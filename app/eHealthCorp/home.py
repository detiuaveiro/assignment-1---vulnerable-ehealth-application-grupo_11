from flask import Blueprint, render_template, abort

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/')
def show():
    return render_template('home.html')
