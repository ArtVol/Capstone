import render_index
import speak
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    # render_index.render_ind()
    return render_template('index.html')

@app.route('/title.html')
def title():
    return render_template('title.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/button.html')
def button():
    return render_template('button.html')

@app.route('/my-link/')
def my_link():
    speak.say()
    return render_template('button.html')
@app.route('/fill1.html')
def fill1():
    return render_template('fill1.html')

@app.route('/fill2.html')
def fill2():
    return render_template('fill2.html')

@app.route('/fill4.html')
def fill4():
    return render_template('fill4.html')

@app.route('/fill3.html')
def fill3():
    return render_template('fill3.html')

@app.route('/skoltech.html')
def skoltech():
    return render_template('skoltech.html')

@app.route('/clothes.html')
def clothes():
    return render_template('clothes.html')

@app.route('/umbrella.html')
def umbrella():
    return render_template('umbrella.html')

@app.route('/report.html')
def report():
    return render_template('report.html')

@app.route('/settings.html')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run()