from flask import Blueprint, render_template, abort

index = Blueprint('index', __name__, template_folder='templates')


@index.route('/')
def show():
    return render_template('index.html')
