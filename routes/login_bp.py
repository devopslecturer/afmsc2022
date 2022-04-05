from flask import Blueprint

from controllers.login_controller import login, index, logout

login_bp = Blueprint('login_bp', __name__)

login_bp.route('/', methods=['GET'])(index)

login_bp.route('/validate', methods=['POST'])(login)

login_bp.route('/logout', methods=['GET'])(logout)
