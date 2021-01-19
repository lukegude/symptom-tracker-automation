from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from waitress import serve
from os import system
from configurator import new_user

app = Flask(__name__)


@app.route('/new_user')
def new_user_home():
    return render_template('new_user.html')


@app.route('/new_user', methods=['GET', 'POST'])
def new_user_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        phone_number = request.form.get('phone')
        new_user(email, password, phone_number)
        return redirect(url_for('setup'))
    return render_template('new_user.html')


@app.route('/', methods=['GET', 'POST'])
def setup():
    return render_template('setup.html')


@app.route('/home')
def home():
    system('python main.py')
    return render_template('index.html')


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
