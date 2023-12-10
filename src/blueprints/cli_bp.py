from flask import Blueprint
from flask.cli import with_appcontext
from src.extensions import db, bcrypt  # Adjust the path as needed
from src.models.user import User
from src.models.mood_entry import MoodEntry
from datetime import datetime

db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")

@db_commands.cli.command("seed")
@with_appcontext
def db_seed():
    # Users
    users = [
        User(
            name="Sam Gifford",
            email="admin@moodnest.com",
            password=bcrypt.generate_password_hash("admin123").decode("utf8"),
            is_admin=True,
        ),
        User(
            name="Sarah Jane",
            email="sarahjane99@gmail.com",
            password=bcrypt.generate_password_hash("puppy12345").decode("utf8"),
        ),
        User(
            name="Andrew Tate",
            email="TopG69@gmail.com",
            password=bcrypt.generate_password_hash("bugatti222").decode("utf8"),
        ),
    ]

    db.session.add_all(users)
    db.session.commit()
    print("Users Seeded")

    # Dummy Mood Entries
    mood_entries = [
        MoodEntry(
            user_id=1,
            mood="Happy",
            note="Feeling great today!",
            timestamp=datetime.utcnow(),
        ),
        MoodEntry(
            user_id=2,
            mood="Sad",
            note="Had a tough day.",
            timestamp=datetime.utcnow(),
        ),
        MoodEntry(
            user_id=3,
            mood="Excited",
            note="Looking forward to the weekend!",
            timestamp=datetime.utcnow(),
        ),
    ]

    db.session.add_all(mood_entries)
    db.session.commit()
    print("Mood Entries Seeded")