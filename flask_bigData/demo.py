#! usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World! '

@app.route('/login',method=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:    
        return show_the_login_form()

@app.route('/<string:username>/home')
def home_status(username):
    return '{} Home'.format(username)


# Static file should be /static
# url_for('static', filename='style.css')

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('home_status',username='jack tomas'))

# if __name__ == "__main__":
