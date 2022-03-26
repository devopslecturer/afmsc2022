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

from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from models.UserModels import User

# app = Flask(__name__)

db = SQLAlchemy()


def index():
    return render_template('signup/index.html')


def register_user():
    if request.method == 'POST':
        if not request.form['firstName'] \
                or not request.form['lastName'] \
                or not request.form['email'] \
                or not request.form['password'] \
                or not request.form['confirmPassword'] \
                or not request.form['address']:
            flash('Please enter all the fields', 'error')
        else:
            if request.form['password'] == request.form['confirmPassword']:
                user = User(firstName=request.form['firstName'], lastName=request.form['lastName'],
                            email=request.form['email'], password=request.form['password'],
                            address=request.form['address'])
                db.session.add(user)
                db.session.commit()
                flash('Record was successfully added')
            else:
                flash('Passwords does not match', 'error')
    return render_template('login/login.html')
