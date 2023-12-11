from src.extensions import db
from datetime import datetime
from marshmallow import fields, Schema

class ActivityLog(db.Model):
    __tablename__ = 'activity_logs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    activity = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)




class ActivityLogSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    activity = fields.Str(required=True)

    def format_timestamp(self, obj):
        return obj.timestamp.strftime("%Y-%m-%d %H:%M:%S")

    timestamp = fields.Method("format_timestamp", dump_only=True)
    
    class Meta:
        fields = ("id", "user_id", "activity", "timestamp")