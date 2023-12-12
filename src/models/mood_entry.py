# Import necessary modules and classes
from marshmallow import fields, Schema  # Classes for defining Marshmallow fields and schemas
from datetime import datetime  # Module for working with dates and times
from src.extensions import db  # SQLAlchemy database instance

# Define the MoodEntry model
class MoodEntry(db.Model):
    __tablename__ = 'mood_entries'  # Name of the table in the database

    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key column referencing the users table
    mood = db.Column(db.String(50), nullable=False)  # Column for the mood, which cannot be null
    mood_intensity = db.Column(db.Integer, nullable=False)  # New column for the mood intensity, which cannot be null
    note = db.Column(db.Text)  # Column for the note, which can be null
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Timestamp column with a default value of the current time and cannot be null

    user = db.relationship('User', back_populates='mood_entries')  # Relationship to the User model

# Define the MoodEntry schema
class MoodEntrySchema(Schema):
    id = fields.Int(dump_only=True)  # Field for the ID, which should not be loaded from input data
    user_id = fields.Int(required=True)  # Field for the user ID, which is required
    mood = fields.Str(required=True)  # Field for the mood, which is required
    mood_intensity = fields.Int(required=True)  # New field for the mood intensity, which is required
    note = fields.Str()  # Field for the note
    timestamp = fields.Method("get_timestamp", dump_only=True)  # Field for the timestamp, which should not be loaded from input data and should be formatted as a string

    class Meta:
        fields = ("id", "user_id", "mood", "mood_intensity", "note", "timestamp")  # Fields to include in the serialized output

    def get_timestamp(self, obj):
        return obj.timestamp.strftime("%Y-%m-%d %H:%M")