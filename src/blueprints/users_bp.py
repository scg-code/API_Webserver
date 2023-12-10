from flask import Blueprint, request
from src.extensions import bcrypt, db
from src.models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.auth import authorize

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("/register", methods=["POST"])
def register():
    try:
        user_info = UserSchema().load(request.json)
        user = User(
            email=user_info["email"],
            password=bcrypt.generate_password_hash(user_info["password"]).decode("utf8"),
            name=user_info.get("name", ""),
            is_admin=user_info.get("is_admin", False)
        )
        db.session.add(user)
        db.session.commit()
        return UserSchema().dump(user), 201
    except IntegrityError:
        return {"error", "Email address is already in use"}, 409
    

@users_bp.route("/login", methods=["POST"])
def login():
    user_info = UserSchema().load(request.json)
    stmt = db.select(User).where(User.email == user_info["email"])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, user_info["password"]):
        token = create_access_token(identity=user.id)
        return {
            "token": token,
            "user": UserSchema().dump(user),
        }
    else:
        return {"error": "Invalid email or password"}, 401
    
@users_bp.route("/")
@jwt_required
def all_users():
    authorize() # Admin Only
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True).dump(users)

@users_bp.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    # Requires authentication (JWT) to access.
    # Users can update their own information.

    # Get the user making the request
    current_user_id = get_jwt_identity()

    # Check if the user making the request is the same as the one being updated
    if current_user_id != user_id:
        return {"error": "Unauthorized"}, 403

    try:
        user_info = UserSchema().load(request.json)
        user = User.query.get_or_404(user_id)

        # Update user information
        user.email = user_info["email"]
        user.name = user_info.get("name", "")
        user.is_admin = user_info.get("is_admin", False)

        db.session.commit()

        return UserSchema().dump(user), 200
    except IntegrityError:
        return {"error": "Email address is already in use"}, 409

@users_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    # Requires authentication (JWT) to access.
    # Requires admin privileges to delete a user.

    authorize()  # Admin Only

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return {"message": "User deleted successfully"}, 200
