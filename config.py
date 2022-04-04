import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
# DEBUG = True

# Connect to the database
# USR = os.environ.get("DB_USR")
USR = "root"
# PWD = os.environ.get("DB_PWD")
PWD = "1234"
# URL = os.environ.get("DB_URL")
URL = "127.0.0.1"
# PORT = os.environ.get("DB_PORT")
PORT = "3306"
# NAME = os.environ.get("DB_NAME")
NAME = "testDB"
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USR, PWD, URL, PORT, NAME)

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
