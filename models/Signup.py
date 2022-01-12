"""
#
# @File         : Signup.py.py
# @Created      : 2022-01-05 11:51
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  :
#
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Signup(db.Model):
    __tablename__ = 'user_credentials'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(120))
    lastName = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'password': self.password
        }
