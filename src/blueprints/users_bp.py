from flask import Blueprint, request, jsonify
from src.extensions import bcrypt, db
from src.models.user import User, UserSchema, UserRegistrationSchema
from src.models.mood_entry import MoodEntry
from src.models.goal import Goal
from src.models.activity_log import ActivityLog
from src.models.thought_journal import ThoughtJournal
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required
from src.auth import authorize
from werkzeug.exceptions import NotFound
from sqlalchemy import desc

# Define the users blueprint
users_bp = Blueprint("users", __name__, url_prefix="/users")

# Define the register route
@users_bp.route("/register", methods=["POST"])
def register():
    try:
        # Load the user information from the request data
        user_info = UserRegistrationSchema().load(request.json)

        # Create a new user with the provided information
        user = User(
            email=user_info["email"],
            password=bcrypt.generate_password_hash(user_info["password"]).decode("utf8"),
            name=user_info.get("name", ""),
            is_admin=user_info.get("is_admin", False)
        )

        # Add the new user to the database and commit the changes
        db.session.add(user)
        db.session.commit()

        # Return the new user's information and a 201 Created status code
        return UserSchema().dump(user), 201
    except IntegrityError:
        # If an IntegrityError is raised, return an error message and a 409 Conflict status code
        return {"error": "Email address is already in use"}, 409

# Define the login route
@users_bp.route("/login", methods=["POST"])
def login():
    # Load the user information from the request data
    user_info = UserRegistrationSchema().load(request.json)

    # Query the database for a user with the provided email
    stmt = db.select(User).where(User.email == user_info["email"])
    user = db.session.scalar(stmt)

    # If the user exists and the provided password is correct, create a JWT and return it along with the user's information
    if user and bcrypt.check_password_hash(user.password, user_info["password"]):
        token = create_access_token(identity=user.id)
        return {
            "token": token,
            "user": UserSchema().dump(user),
        }
    else:
        # If the user does not exist or the password is incorrect, return an error message and a 401 Unauthorized status code
        return {"error": "Invalid email or password"}, 401


# Define the route for getting all users
@users_bp.route("/")
@jwt_required()
def all_users():
    authorize()  # Admin Only

    # Query the database for all users
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()

    # Create a list to store the user data
    user_data = []

    # Loop through each user
    for user in users:
        # Get the most recent mood entry for the user
        latest_mood_entry = MoodEntry.query.filter_by(user_id=user.id).order_by(desc(MoodEntry.timestamp)).first()

        # If the user has at least one mood entry, get the emotion of the most recent entry
        latest_emotion = latest_mood_entry.mood if latest_mood_entry else None

        # Append the user data to the list
        user_data.append({
            "email": user.email,
            "id": user.id,
            "is_admin": user.is_admin,
            "name": user.name,
            "registration_date": user.registration_date,
            "latest_emotion": latest_emotion
        })

    # Return the user data and a 200 OK status code
    return jsonify(user_data), 200


# Define the route for deleting a user
@users_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    authorize()  # Ensure the user is authorized (Admin Only)

    try:
        # Query the database for the user being deleted
        user = User.query.get_or_404(user_id)

        # Delete the user from the database
        db.session.delete(user)
        # Commit the changes to the database
        db.session.commit()

        # Return a success message and a 200 OK status code
        return {"message": "User deleted successfully"}, 200
    except NotFound:
        # If a NotFound exception is raised, return a custom error message and a 404 Not Found status code
        return {"error": "User not found"}, 404
    except IntegrityError:
        # If an IntegrityError is raised, return an error message and a 409 Conflict status code
        return {"error": "Cannot delete user because there are related records"}, 409
    

# Define the route for getting user statistics
@users_bp.route("/<int:user_id>/stats", methods=["GET"])
@jwt_required()
def get_user_stats(user_id):
    try:
        # Query the database for the specified user, or return a 404 error if they do not exist
        user = User.query.get_or_404(user_id)

        # Calculate the number of mood entries, goals, activity logs, and thought journals associated with the user
        num_mood_entries = MoodEntry.query.filter_by(user_id=user_id).count()
        num_goals = Goal.query.filter_by(user_id=user_id).count()
        num_activity_logs = ActivityLog.query.filter_by(user_id=user_id).count()
        num_thought_journals = ThoughtJournal.query.filter_by(user_id=user_id).count()

        # Return the calculated statistics and a 200 OK status code
        return {
            "num_mood_entries": num_mood_entries,
            "num_goals": num_goals,
            "num_activity_logs": num_activity_logs,
            "num_thought_journals": num_thought_journals
        }, 200
    except NotFound:
        # If a NotFound exception is raised, return a custom error message and a 404 Not Found status code
        return {"error": "User not found"}, 404