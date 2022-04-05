from flask import render_template

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def index():
    return render_template('users/index.html')


def create():
    pass


def show(user_id):
    pass


def update(user_id):
    pass


def destroy(user_id):
    pass
