import sys
from flask import render_template, redirect, url_for, request, abort

from models.UserModels import User

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
