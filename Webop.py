from flask import Flask, render_template, request
from waitress import serve
from os import system

app = Flask(__name__)



@app.route('/setup', methods=['GET', 'POST'])
def setup():
    return render_template('setup.html')
@app.route('/home')
def home():
    system('python main.py')
    return render_template('index.html')



if __name__ == "__main__":
    serve(app,host = '0.0.0.0', port = 5000)
