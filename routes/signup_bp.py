from flask import Blueprint
from controllers.SignUpController import index, register_user

signup_bp = Blueprint('signup_bp', __name__)

signup_bp.route('/', methods=['GET'])(index)

signup_bp.route('/add', methods=['POST'])(register_user)

