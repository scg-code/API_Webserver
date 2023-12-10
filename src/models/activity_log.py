from src.extensions import db
from datetime import datetime
from marshmallow import fields, Schema

class ActivityLog(db.Model):
    __tablename__ = 'activity_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    activity = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)



class ActivityLogSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    activity = fields.Str(required=True)
    timestamp = fields.DateTime(dump_only=True)

    class Meta:
        fields = ("id", "user_id", "activity", "timestamp")
