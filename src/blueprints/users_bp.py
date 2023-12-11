# Import necessary modules and classes
from flask import Blueprint, request
from src.extensions import bcrypt, db
from src.models.user import User, UserSchema, UserRegistrationSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.auth import authorize

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

    # Return the users' information
    return UserSchema(many=True).dump(users)

# Define the route for updating a user
@users_bp.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    # Get the ID of the user making the request
    current_user_id = get_jwt_identity()

    # If the user making the request is not the one being updated, return an error message and a 403 Forbidden status code
    if current_user_id != user_id:
        return {"error": "Unauthorized"}, 403

    try:
        # Load the user information from the request data
        user_info = UserSchema().load(request.json)

        # Query the database for the user being updated
        user = User.query.get_or_404(user_id)

        # Update the user's information
        user.email = user_info["email"]
        user.name = user_info.get("name", "")
        user.is_admin = user_info.get("is_admin", False)

        # Commit the changes to the database
        db.session.commit()

        # Return the updated user's information and a 200 OK status code
        return UserSchema().dump(user), 200
    except IntegrityError:
        # If an IntegrityError is raised, return an error message and a 409 Conflict status code
        return {"error": "Email address is already in use"}, 409

# Define the route for deleting a user
@users_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    authorize()  # Admin Only

    # Query the database for the user being deleted
    user = User.query.get_or_404(user_id)

    # Delete the user from the database and commit the changes
    db.session.delete(user)
    db.session.commit()

    # Return a success message and a 200 OK status code
    return {"message": "User deleted successfully"}, 200