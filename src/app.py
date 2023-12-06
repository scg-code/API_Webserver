from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager
from os import environ
# from marshmallow.exceptions import ValidationError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI') # Database connection string

db = SQLAlchemy(app)

