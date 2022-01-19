"""
# 
# File          : login_bp.py
# Created       : 17/01/22 9:45 AM
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""
from flask import Blueprint

from controllers.login_controller import login, index

login_bp = Blueprint('login_bp', __name__)

login_bp.route('/', methods=['GET'])(index)