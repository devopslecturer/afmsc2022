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

def index():
    return render_template('reset_password/reset_password.html')


def login():
    pass

