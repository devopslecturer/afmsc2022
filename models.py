from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(120))
    lastName = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    address = db.Column(db.String(120))
    usertype = db.Column(db.String(120))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'password': self.password,
            'address': self.address,
            'usertype': self.usertype
        }


class Bookings(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    customerName = db.Column(db.String(120))
    startDate = db.Column(db.Date)
    endDate = db.Column(db.Date)
    phoneNumber = db.Column(db.String(120))
    roomType = db.Column(db.String(120))
    requests = db.Column(db.String(240))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'customerName': self.customerName,
            'startDate': self.startDate,
            'endDate': self.endDate,
            'phoneNumber': self.phoneNumber,
            'roomType': self.roomType,
            'requests': self.requests
        }
