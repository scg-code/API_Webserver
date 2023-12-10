# src/models/goal.py
from datetime import datetime
from marshmallow import fields, Schema
from src.extensions import db


class Goal(db.Model):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    goal = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(50), default="Pending", nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class GoalSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    goal = fields.Str(required=True)
    description = fields.Str(required=True)
    deadline = fields.Date(allow_none=True)
    status = fields.Str(default="Pending", required=True)
    created_at = fields.DateTime(dump_only=True)

    class Meta:
        fields = ("id", "user_id", "goal", "description", "deadline", "status", "created_at")
