from marshmallow import fields, Schema, validate
from datetime import datetime
from src.extensions import db

# Define the MoodEntry model for SQLAlchemy
class MoodEntry(db.Model):
    __tablename__ = 'mood_entries'  # Set the table name in the database

    # Define the columns in the 'mood_entries' table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key column referencing the 'users' table, must not be null
    mood = db.Column(db.String(50), nullable=False)  # Mood column, must not be null
    mood_intensity = db.Column(db.Integer, nullable=False)  # Mood intensity column, must not be null
    note = db.Column(db.Text)  # Note column, can be null
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Timestamp column with a default value of the current time, must not be null

    user = db.relationship('User', back_populates='mood_entries')  # Define a relationship to the User model, which is back populated with 'mood_entries'

# Define the schema for mood entry serialization
class MoodEntrySchema(Schema):
    id = fields.Int(dump_only=True)  # ID field, only used for output
    user_id = fields.Int(required=True)  # User ID field, must be provided
    mood = fields.Str(required=True, validate=validate.Length(min=1))  # Mood field, must be at least 1 character long
    mood_intensity = fields.Int(required=True, validate=validate.Range(min=1, max=10))  # Mood intensity field, must be between 1 and 10
    note = fields.Str()  # Note field, optional
    timestamp = fields.Method("get_timestamp", dump_only=True)  # Timestamp field, only used for output and formatted using the 'get_timestamp' method

    class Meta:
        fields = ("id", "user_id", "mood", "mood_intensity", "note", "timestamp")  # Fields to be serialized

    def get_timestamp(self, obj):
        return obj.timestamp.strftime("%Y-%m-%d %H:%M")  # Format the timestamp as a string