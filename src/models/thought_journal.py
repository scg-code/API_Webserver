# Import necessary modules and classes
from marshmallow import fields, Schema  # Classes for defining Marshmallow fields and schemas
from src.extensions import db  # SQLAlchemy database instance
from datetime import datetime  # Module for working with dates and times

# Define the ThoughtJournal model
class ThoughtJournal(db.Model):
    __tablename__ = 'thought_journals'  # Name of the table in the database

    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key column referencing the users table
    entry = db.Column(db.Text, nullable=False)  # Column for the journal entry
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Timestamp column with a default value of the current time

    # Defining a relationship with the User model
    user = db.relationship('User', back_populates='thought_journals')

# Define the ThoughtJournal schema
class ThoughtJournalSchema(Schema):
    id = fields.Int(dump_only=True)  # Field for the ID, which should not be loaded from input data
    user_id = fields.Int(required=True)  # Field for the user ID, which is required
    entry = fields.Str(required=True)  # Field for the journal entry, which is required
    timestamp = fields.DateTime(format='%Y-%m-%d %H:%M:%S', dump_only=True)  # Field for the timestamp, which should not be loaded from input data and should be formatted as a string

    class Meta:
        fields = ("id", "user_id", "entry", "timestamp")  # Fields to include in the serialized output
