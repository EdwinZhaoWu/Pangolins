from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/aboutpangolins')
def aboutpangolins():
    return render_template('aboutpangolins.html')

@app.route('/conservationpage')
def conservationpage():
    return render_template('conservationpage.html')