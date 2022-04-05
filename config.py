import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
# DEBUG = True

# Connect to the database
USR = os.environ.get("DB_USR")
PWD = os.environ.get("DB_PWD")
URL = os.environ.get("DB_URL")
PORT = os.environ.get("DB_PORT")
NAME = os.environ.get("DB_NAME")
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USR, PWD, URL, PORT, NAME)

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
