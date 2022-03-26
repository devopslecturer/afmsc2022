"""
# 
# File          : login_controller.py
# Created       : 17/01/22 9:42 AM
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""
from flask import render_template, request, jsonify
from models.DBModels import Signup


def index():
    return render_template('login/login.html')


def login():
    if request.method == 'POST':
        _username = request.form['email']
        _password = request.form['pwd']
        if _username and _password is not None:
            user = Signup.query.filter_by(email=_username, password=_password).first()
            print(user)
            if user:
                return render_template('users/index.html')
                # need rework after home page is created
            else:
                return jsonify({"reason": "User not found", "status": "404"})
        else:
            return jsonify({"status": "400", "reason": "Bas Request"})

