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
from flask import Flask, json, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()


def index():
    return render_template('signup/index.html')


@app.route("/add")
def create():
    pass
