"""
# ----------------------
# Created : 17-01-2022 15:51
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""
from flask import Blueprint

from controllers.reset_password_controller import index

reset_password_bp = Blueprint('resetpassword_bp', __name__)

reset_password_bp.route('/', methods=['GET'])(index)
