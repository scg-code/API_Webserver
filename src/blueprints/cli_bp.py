from flask import Blueprint
from flask import current_app
from flask.cli import with_appcontext
from src.extensions import db, bcrypt  # Adjust the path as needed
from src.models.user import User
from datetime import date

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
    print("Database Seeded")

