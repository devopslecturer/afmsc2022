from flask import Blueprint
from controllers.BookingController import add_booking, getBooking, createBooking

booking_bp = Blueprint('booking_bp', __name__)

booking_bp.route('/', methods=['GET'])(getBooking)

booking_bp.route('/create', methods=['GET'])(createBooking)

booking_bp.route('/create/add', methods=['POST'])(add_booking)

