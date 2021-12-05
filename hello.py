from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/user_no_name')
def user_no_name():
    return render_template('user.html')

@app.route('/list/<num>')
def list(num):
    return render_template('list.html', num=int(num))