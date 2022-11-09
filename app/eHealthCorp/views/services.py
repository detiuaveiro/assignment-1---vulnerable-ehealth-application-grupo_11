from flask import (Blueprint, render_template, session)

services = Blueprint('/services', __name__, template_folder='templates')

@services.route('/services')
def show():
    return render_template('services.html')