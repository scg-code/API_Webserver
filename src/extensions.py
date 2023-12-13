from flask_sqlalchemy import SQLAlchemy  # Extension for Flask that adds support for SQLAlchemy
from flask_marshmallow import Marshmallow  # Extension for Flask that adds support for Marshmallow
from flask_bcrypt import Bcrypt  # Extension for Flask that adds support for Bcrypt password hashing
from flask_jwt_extended import JWTManager  # Extension for Flask that adds support for JWTs
from os import environ  # Module for interacting with the operating system environment
from marshmallow.exceptions import ValidationError  # Exception for validation errors in Marshmallow
from flask import Flask  # Flask web framework
from datetime import timedelta  # Module for working with time

# Create a new Flask application
app = Flask(__name__)

# Configure the Flask application
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')  # Set the database URI from the environment
app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')  # Set the JWT secret key from the environment
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)  # Set the JWT access token expiration time to 2 hours

# Initialize Flask extensions
db = SQLAlchemy(app)  # Initialize SQLAlchemy with the Flask app
ma = Marshmallow(app)  # Initialize Marshmallow with the Flask app
bcrypt = Bcrypt(app)  # Initialize Bcrypt with the Flask app
jwt = JWTManager(app)  # Initialize JWTManager with the Flask app

@app.errorhandler(401)
def unauthorized(err):
    # Return a JSON response with an error message for 401 Unauthorized errors
    return {'error': str(err)}, 401

@app.errorhandler(ValidationError)
def validation_error(err):
    # Return a JSON response with validation error messages for ValidationError exceptions
    return {'error': err.messages}, 400

@app.errorhandler(404)
def not_found(err):
    # Return a JSON response with an error message for 404 Not Found errors
    return {'error': str(err)}, 404

@app.errorhandler(405)
def method_not_allowed(err):
    # Return a JSON response with an error message for 405 Method Not Allowed errors
    return {'error': str(err)}, 405

@app.errorhandler(500)
def internal_server_error(err):
    # Return a JSON response with an error message for 500 Internal Server Error errors
    return {'error': str(err)}, 500