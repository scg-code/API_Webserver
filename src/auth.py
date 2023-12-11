# Import necessary modules and functions
from flask import abort  # Function to abort a request and return an error
from flask_jwt_extended import get_jwt_identity  # Function to get the identity of the current JWT
from src.models.user import User  # User model
from src.extensions import db  # Database instance

# Define the authorize function
def authorize(user_id=None):
    jwt_user_id = get_jwt_identity()  # Get the user ID from the current JWT

    # Create a SQL SELECT statement to get the user with the ID from the JWT
    stmt = db.select(User).filter_by(id=jwt_user_id)

    # Execute the SQL statement and get the first result or None if no results are found
    result = db.session.execute(stmt).one_or_none()

    # If no result is found, abort the request with a 404 Not Found error
    if result is None:
        abort(404, description="User not found")

    # Get the User object from the result
    user = result[0]

    # If the user is not an admin and the provided user ID does not match the user ID from the JWT, abort the request with a 401 Unauthorized error
    if not (user.is_admin or (user_id and jwt_user_id == user_id)):
        abort(401, description="Unauthorized access")