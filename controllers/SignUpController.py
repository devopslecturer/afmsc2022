from flask import render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

from models import User

db = SQLAlchemy()


def index():
    return render_template('signup/index.html')


def register_user():
    """
        API to register User
        ---
        tags:
            - Register user
        parameters:
            - name: firstName
              type: String
              required: true
              description: First Name
            - name: lastName
              type: String
              required: true
              description: Last Name
            - name: email
              type: String
              required: true
              description: Email
            - name: password
              type: String
              required: true
              description: Password
            - name: confirmPassword
              type: String
              required: true
              description: Confirm password
            - name: address
              type: String
              required: true
              description: Address
        responses:
            200:
                description: Record was successfully added
            500:
                description: Error while adding record
    """

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
