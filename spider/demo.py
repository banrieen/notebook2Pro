#! usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, url_for
from flask import render_template # template
from flask import request # api request
from login import Login
from werkzeug.utils import secure_filename   # The secure filename
from flask import make_response  # cookies
from flask import abort, redirect # url redirect
from flask import escape

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/')
def index():
    # Read the cookie 
    # username = request.cookies.get('username')
    # Save cookies
    resp = make_response(render_template('helloword.html'))
    resp.set_cookie('username', 'The username')

    #Redirective url
    return redirect(url_for('login'))
    # return resp
    # return redirect(url_for('login')) # redirect url

@app.route('/login', methods=['GET','POST'])
def login():
    error = ""
    if request.method == 'POST':
        if Login.account_login(request.form['username'], request.form['password']):
            return Login.log_the_user_in(request.form['username'])
    else:
        error = 'Invalid username or password. '  
        abort(401)
    return render_template('login.html', error=error)

@app.route('/home/')
@app.route('/home/<string:username>')
def home_status(username=None):
    return render_template('helloworld.html', name=username)
    # '{} Home'.format(username)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file_path']
        f.save('var/www/uploads/' + secure_filename(f.filename))
# Static file should be /static
# url_for('static', filename='style.css')
@app.errorhandler(404)
def not_found(error):
    # user make_response()
    resp = make_response(render_template('error.html'),404)
    resp.headers['X-Somthing'] = 'A value'
    return render_template('error.html')


with app.test_request_context('/Hello',method='POST'):
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('home_status',username='jack tomas'))

    assert request.path == '/Hello'
    assert request.method == 'POST'

if __name__ == "__main__":
    app.run()
