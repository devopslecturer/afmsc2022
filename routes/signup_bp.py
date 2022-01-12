"""
#
# @File         : signup_bp.py
# @Created      : 2022-01-05 11:48
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  :
#
"""

from flask import Blueprint

from controllers.SignUpController import index, create

signup_bp = Blueprint('signup_bp', __name__)

signup_bp.route('/', methods=['GET'])(index)
signup_bp.route('/create', methods=['POST'])(create)

