"""
# 
# File          : login_controller.py
# Created       : 17/01/22 9:42 AM
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""
from flask import Flask, render_template, request, flash, redirect


def index():
    return render_template('login/login.html')


def login():
    pass
