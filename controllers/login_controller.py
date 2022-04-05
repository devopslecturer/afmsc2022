from flask import render_template, request, session

from controllers.BookingController import getBooking
from models import User


def index():
    return render_template('login/login.html')


def login():
    if request.method == 'POST':
        _username = request.form['email']
        _password = request.form['password']
        if _username and _password is not None:
            user = User.query.filter_by(email=_username, password=_password).first()
            if user:
                session['user'] = user.id
                return getBooking()
    return render_template('login/login.html')


def logout():
    session.clear()
    return render_template('index.html')

