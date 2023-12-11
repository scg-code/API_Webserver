# Import necessary modules and classes
from datetime import datetime  # Module for working with dates and times
from marshmallow import fields, Schema  # Classes for defining Marshmallow fields and schemas
from src.extensions import db  # SQLAlchemy database instance

# Define the ActivityLog model
class ActivityLog(db.Model):
    __tablename__ = 'activity_logs'  # Name of the table in the database

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Primary key column with autoincrement
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key column referencing the users table
    activity = db.Column(db.String, nullable=False)  # Column for the activity, which cannot be null
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)  # Timestamp column with a default value of the current time and can be null

# Define the ActivityLog schema
class ActivityLogSchema(Schema):
    id = fields.Int(dump_only=True)  # Field for the ID, which should not be loaded from input data
    user_id = fields.Int(required=True)  # Field for the user ID, which is required
    activity = fields.Str(required=True)  # Field for the activity, which is required

    def format_timestamp(self, obj):
        # Method to format the timestamp as a string
        return obj.timestamp.strftime("%Y-%m-%d %H:%M:%S")

    timestamp = fields.Method("format_timestamp", dump_only=True)  # Field for the timestamp, which should not be loaded from input data and should be formatted as a string

    class Meta:
        fields = ("id", "user_id", "activity", "timestamp")  # Fields to include in the serialized output