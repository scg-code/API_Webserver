# extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from os import environ
from marshmallow.exceptions import ValidationError
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')


db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@app.errorhandler(401)
def unauthorized(err):
    return {'error': 'You are not authorized to access this resource'}

@app.errorhandler(ValidationError)
def validation_error(err):
    return {'error': err.messages}
