from flask import render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from models import Bookings

db = SQLAlchemy()


def index():
    return render_template('booking/booking.html')


def getBooking():
    """
        API to get All bookings
        ---
        tags:
            - get Bookings
        responses:
            200:
                description: bookings fetched
            500:
                description: Internal server error
    """
    return render_template('booking/booking.html', bookings=Bookings.query.all())


def createBooking():
    return render_template('booking/createBooking.html')


def add_booking():
    """
        API to add booking
        ---
        tags:
            - Add Booking
        parameters:
            - name: customerName
              type: String
              required: true
              description: Customer Name
            - name: startDate
              type: Date
              required: true
              description: Booking start date
            - name: endDate
              type: Date
              required: true
              description: Booking end date
            - name: phoneNumber
              type: String
              required: true
              description: Customer phone number
            - name: roomType
              type: String
              required: true
              description: Room booking type
            - name: requests
              type: String
              required: false
              description: Additional requests
        responses:
            200:
                description: Record was successfully added
            500:
                description: Error while adding record
    """

    if request.method == 'POST':
        if not request.form['customerName'] \
                or not request.form['startDate'] \
                or not request.form['endDate'] \
                or not request.form['phoneNumber'] \
                or not request.form['roomType']:
            flash('Please enter all required fields', 'error')
        else:
            booking = Bookings(customerName=request.form['customerName'], startDate=request.form['startDate'],
                               endDate=request.form['endDate'], phoneNumber=request.form['phoneNumber'],
                               roomType=request.form['roomType'], requests=request.form['requests'])
            db.session.add(booking)
            db.session.commit()
            flash('Booking added successfully')
    return redirect("/booking/")
