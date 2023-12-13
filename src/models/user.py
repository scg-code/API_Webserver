from src.extensions import db
from marshmallow import fields, Schema, validate

# Define the User model for SQLAlchemy
class User(db.Model):
    __tablename__ = 'users'  # Set the table name in the database

    # Define the columns in the 'users' table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    name = db.Column(db.String, default='Anonymous')  # Name column with a default value
    email = db.Column(db.String, nullable=False, unique=True)  # Email column, must be unique and not null
    password = db.Column(db.String, nullable=False)  # Password column, must not be null
    registration_date = db.Column(db.Date, default=db.func.current_date())  # Registration date column with a default value of the current date
    is_admin = db.Column(db.Boolean, default=False)  # Admin status column with a default value of False

    # Define relationships with other models
    mood_entries = db.relationship('MoodEntry', back_populates='user', cascade="all, delete-orphan")  # One-to-many relationship with MoodEntry
    goals = db.relationship('Goal', back_populates='user', cascade="all, delete-orphan")  # One-to-many relationship with Goal
    activity_logs = db.relationship('ActivityLog', back_populates='user', cascade="all, delete-orphan")  # One-to-many relationship with ActivityLog
    thought_journals = db.relationship('ThoughtJournal', back_populates='user', cascade="all, delete-orphan")  # One-to-many relationship with ThoughtJournal

# Define the schema for user registration
class UserRegistrationSchema(Schema):
    email = fields.Email(required=True)  # Email field, must be a valid email
    password = fields.String(required=True, validate=validate.Length(min=8, error='Password must be at least 8 characters'))  # Password field, must be at least 8 characters
    registration_date = fields.Date(dump_only=True)  # Registration date field, only used for output

    class Meta:
        model = User  # Specify the model to be used for serialization
        fields = ("id", "name", "email", "password", "registration_date", "is_admin")  # Fields to be serialized

# Define the schema for user serialization
class UserSchema(Schema):
    email = fields.Email(required=True)  # Email field, must be a valid email
    registration_date = fields.Date(dump_only=True)  # Registration date field, only used for output

    class Meta:
        model = User  # Specify the model to be used for serialization
        fields = ("id", "name", "email", "registration_date", "is_admin")  # Fields to be serialized