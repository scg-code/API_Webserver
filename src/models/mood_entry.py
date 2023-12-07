# mood_entry.py
from marshmallow import fields, Schema
from datetime import datetime
from src.extensions import db

class MoodEntry(db.Model):
    __tablename__ = 'mood_entries'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mood = db.Column(db.String(50), nullable=False)
    note = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='mood_entries')


class MoodEntrySchema(Schema):
    class Meta:
        fields = ("id", "user_id", "mood", "note", "timestamp")

