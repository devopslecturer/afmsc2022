"""
# ----------------------
# Created : 17-01-2022 14:26
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""
from flask import Flask, render_template, request, flash, redirect
from sqlalchemy.dialects import mysql

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)

db = SQLAlchemy()
#
def index():
    # return render_template('reset_password/reset_password.html')
    print('hi');

def reset():
    print('hi');
    # if request.method == 'POST':
    #     if not request.form['email']:
    #         flash('Please enter all the fields', 'error')
    #     else:
    #         if request.form['email'] == request.form['email']:
    #              user_email = request.form['email'];
    #              user_data = User.query.filter_by(email=user_email).first()
    #              print(user_data.email)
    #              send_email(user_data.email);
    #
    #             flash('Record was successfully added')
    #         else:
    #             flash('Passwords does not match', 'error')
    return render_template('signup/index.html')
def send_email():
    print('hi');
