#!/usr/bin/env python3


import re
from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    url = f'/<string:{username}>'
    exp= re.compile('[A-Za-z]+')
    matches = exp.findall(url)
    if len(matches) >= 2:
        type, parameter = matches[:2]
    else:
        type, parameter = 'unknown', 'unknown'

    return f'<h1>Profile for {parameter} (Type: {type})</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)


