import os
import configparser
config = configparser.ConfigParser()
config.read_file(open(r'..\config\config.ini'))
USERNAME = config.get('postgres','username')
PASSWORD = config.get('postgres','password')

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL -- Done
SQLALCHEMY_DATABASE_URI = 'postgres://'+USERNAME+':'+PASSWORD+'@localhost:5432/fyyurr'
SQLALCHEMY_TRACK_MODIFICATIONS = False