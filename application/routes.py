
from flask import render_template
from application import application

@application.route('/')
@application.route('/index')
def index():
    return render_template('availability_dashboard.html')

