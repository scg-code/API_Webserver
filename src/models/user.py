# Importing necessary modules from SQLAlchemy and Marshmallow
from src.extensions import db
from marshmallow import fields, Schema, validate


# Defining the User model for SQLAlchemy
class User(db.Model):
    __tablename__ = 'users'  # Setting the table name in the database

    # Defining the columns in the 'users' table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    name = db.Column(db.String, default='Anonymous')  # Name column with a default value
    email = db.Column(db.String, nullable=False, unique=True)  # Email column, must be unique and not null
    password = db.Column(db.String, nullable=False)  # Password column, must not be null
    registration_date = db.Column(db.Date, default=db.func.current_date())  # Registration date column with a default value of the current date
    is_admin = db.Column(db.Boolean, default=False)  # Admin status column with a default value of False

    # Defining relationships with other models
    mood_entries = db.relationship('MoodEntry', back_populates='user', cascade="all, delete-orphan")
    goals = db.relationship('Goal', back_populates='user', cascade="all, delete-orphan")
    activity_logs = db.relationship('ActivityLog', back_populates='user', cascade="all, delete-orphan")
    thought_journals = db.relationship('ThoughtJournal', back_populates='user', cascade="all, delete-orphan")


# User registration schema
class UserRegistrationSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, error='Password must be at least 8 characters'))
    registration_date = fields.Date(dump_only=True)

    class Meta:
        model = User  # Specify the model to be used for serialization
        fields = ("id", "name", "email", "password", "registration_date", "is_admin")


# User serialization schema
class UserSchema(Schema):
    email = fields.Email(required=True)
    registration_date = fields.Date(dump_only=True)

    class Meta:
        model = User  # Specify the model to be used for serialization
        fields = ("id", "name", "email", "registration_date", "is_admin")