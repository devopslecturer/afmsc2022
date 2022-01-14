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
from flask import Flask, render_template, request, flash, redirect
from sqlalchemy.dialects import mysql

from models.Signup import Signup
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

db = SQLAlchemy()


def index():
    return render_template('signup/index.html')


def register_user():
    conn = None
    cursor = None

    try:
        _fname = request.form['firstName']
        _lname = request.form['lastName']
        _email = request.form['email']
        _password = request.form['password']
        _confirmPassword = request.form['confirmPassword']

        if _fname and _lname and _email and _password and _password == _confirmPassword and request.method == 'POST':
            _hashedPassword = generate_password_hash(_password)
            sql = "INSERT INTO user_credentials(firstName, lastName, email, password) VALUES (%s, %s, %s, %s)"
            data = (_fname, _lname, _email, _hashedPassword)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit
            flash('Registered successfully!')
            return redirect('/')
        else:
            return 'Error while adding user'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



