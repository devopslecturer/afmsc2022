import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
PWD = '1234'
USR = 'root'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@127.0.0.1:3306/testDB'.format(USR, PWD)

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
