# src/models/thought_journal.py
from marshmallow import fields, Schema
from src.extensions import db
from datetime import datetime


class ThoughtJournal(db.Model):
    __tablename__ = 'thought_journals'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    entry = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class ThoughtJournalSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    entry = fields.Str(required=True)
    timestamp = fields.DateTime(format='%Y-%m-%d %H:%M:%S', dump_only=True)

    class Meta:
        fields = ("id", "user_id", "entry", "timestamp")
