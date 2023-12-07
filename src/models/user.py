from src.extensions import db
from marshmallow import fields, Schema, validate

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default='Anonymous')
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    registration_date = db.Column(db.Date, default=db.func.current_date())
    is_admin = db.Column(db.Boolean, default=False)

    mood_entries = db.relationship('MoodEntry', back_populates='user')

class UserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, error='Password must be at least 8 characters'))
    registration_date = fields.Date(dump_only=True) # Read only field for registration date
    # is_admin = fields.Boolean()

    class Meta:
        fields = ("id", "name", "email", "password", "registration_date", "is_admin")