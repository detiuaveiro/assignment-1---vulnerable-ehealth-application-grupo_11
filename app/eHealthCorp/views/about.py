from flask import (Blueprint, render_template, session)

about = Blueprint('/about', __name__, template_folder='templates')

@about.route('/about')
def show():
    return render_template('about.html', title='About')