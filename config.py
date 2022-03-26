import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# Later update below to ENV variable
USR = 'Addams_user'
PWD = '2DPYkyqnD0yZZEMLPYPo'
URL = 'addamsfamily.cbvz0bsw5sus.eu-west-1.rds.amazonaws.com'
DATABASE = 'addamsfamily'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:3306/{}'.format(USR, PWD, URL, DATABASE)

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
