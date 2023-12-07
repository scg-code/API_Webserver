from flask import Blueprint, request
from src.extensions import bcrypt, db
from src.models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required
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