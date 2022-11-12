from flask import (Blueprint, render_template, session, redirect, url_for,)

services = Blueprint('/services', __name__, template_folder='templates')

@services.route('/services')
def show():
    return render_template('services.html')