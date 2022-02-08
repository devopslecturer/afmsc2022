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

signup = SQLAlchemy()


class Signup(signup.Model):
    __tablename__ = 'userCred'

    id = signup.Column(signup.Integer, primary_key=True)
    firstName = signup.Column(signup.String(120))
    lastName = signup.Column(signup.String(120))
    email = signup.Column(signup.String(120))
    password = signup.Column(signup.String(120))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'password': self.password
        }
