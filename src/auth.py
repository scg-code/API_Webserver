# Import necessary modules and functions
from flask import jsonify  # Function to create a JSON response
from flask_jwt_extended import get_jwt_identity  # Function to get the identity of the current JWT
from src.models.user import User  # User model
from src.extensions import db  # Database instance



# Define the authorize function
def authorize(user_id=None, admin_required=False):
    jwt_user_id = get_jwt_identity()  # Get the user ID from the current JWT

    # Create a SQL SELECT statement to get the user with the ID from the JWT
    stmt = db.select(User).filter_by(id=jwt_user_id)

    # Execute the SQL statement and get the first result or None if no results are found
    result = db.session.execute(stmt).one_or_none()

    # If no result is found, return a 404 Not Found error in JSON format
    if result is None:
        return jsonify({"error": "User not found"}), 404

    # Get the User object from the result
    user = result[0]

    # If admin_required is True and the user is not an admin, return a 403 Forbidden error in JSON format
    if admin_required and not user.is_admin:
        return jsonify({"error": "Admin privileges required"}), 403

    # If the user is not an admin and the provided user ID does not match the user ID from the JWT, return a 401 Unauthorized error in JSON format
    if not (user.is_admin or (user_id and jwt_user_id == user_id)):
        return jsonify({"error": "Unauthorized access"}), 401