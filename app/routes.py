
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('availability_dashboard.html')
