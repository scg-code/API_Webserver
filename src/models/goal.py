from datetime import datetime  # Module for working with dates and times
from marshmallow import fields, Schema  # Classes for defining Marshmallow fields and schemas
from src.extensions import db  # SQLAlchemy database instance

# Define the Goal model
class Goal(db.Model):
    __tablename__ = 'goals'  # Name of the table in the database

    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key column referencing the users table
    goal = db.Column(db.String(255), nullable=False)  # Column for the goal, which cannot be null
    description = db.Column(db.Text, nullable=False)  # Column for the description, which cannot be null
    deadline = db.Column(db.Date, nullable=True)  # Column for the deadline, which can be null
    status = db.Column(db.String(50), default="Pending", nullable=False)  # Column for the status, with a default value of "Pending" and cannot be null
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Timestamp column with a default value of the current time and cannot be null

    user = db.relationship('User', back_populates='goals')

# Define the Goal schema
class GoalSchema(Schema):
    id = fields.Int(dump_only=True)  # Field for the ID, which should not be loaded from input data
    user_id = fields.Int(required=True)  # Field for the user ID, which is required
    goal = fields.Str(required=True)  # Field for the goal, which is required
    description = fields.Str(required=True)  # Field for the description, which is required
    deadline = fields.Date(allow_none=True)  # Field for the deadline, which can be null
    status = fields.Str(default="Pending", required=True)  # Field for the status, with a default value of "Pending" and is required
    created_at = fields.DateTime(dump_only=True)  # Field for the timestamp, which should not be loaded from input data

    class Meta:
        fields = ("id", "user_id", "goal", "description", "deadline", "status", "created_at")  # Fields to include in the serialized output
