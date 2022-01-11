"""
#
# @File         : SignUpController.py.py
# @Created      : 2022-01-04 21:53
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  :
#
"""

import sys
from flask import Flask, json, render_template, request, abort
from models.Signup import Signup
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()


def index():
    return render_template('signup/index.html')


def register_user(Signup):

    fname = Signup.get('firstName')
    lname = Signup.get('lastName')
    email = Signup.get('email')
    password = Signup.get('password')

    existingUser = Signup.query.filter(Signup.email == email).one_or_none()

    if existingUser is None:
        pass
    else:
        abort(409, f'Person {email} exists already')

    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'
