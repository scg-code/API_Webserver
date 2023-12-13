from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.extensions import db
from src.models.activity_log import ActivityLog, ActivityLogSchema

# Create a new Blueprint for activity logs
activity_logs_bp = Blueprint('activity_logs', __name__, url_prefix='/activity_logs')

# Create a schema for activity logs
activity_log_schema = ActivityLogSchema()

# Define a route for getting all activity logs
@activity_logs_bp.route('', methods=['GET'])
@jwt_required()  # Require a valid JWT token
def get_activity_logs():
    user_id = get_jwt_identity()  # Get the user ID from the JWT token
    activity_logs = ActivityLog.query.filter_by(user_id=user_id).all()  # Query all activity logs for this user

    # If the user has no activity logs, return a custom message
    if not activity_logs:
        return jsonify({"message": "No activity logs found for this user"}), 404

    result = activity_log_schema.dump(activity_logs, many=True)  # Serialize the activity logs
    return jsonify(result)  # Return the serialized activity logs

# Define a route for creating a new activity log
@activity_logs_bp.route('', methods=['POST'])
@jwt_required()  # Require a valid JWT token
def create_activity_log():
    user_id = get_jwt_identity()  # Get the user ID from the JWT token
    data = request.json  # Get the request data

    # Get the activity from the request data
    activity = data.get('activity')

    # If the activity is blank, return an error message and a 400 Bad Request status code
    if not activity:
        return jsonify({'error': 'Activity cannot be blank'}), 400

    # Create a new activity log
    new_activity_log = ActivityLog(user_id=user_id, activity=activity)
    db.session.add(new_activity_log)  # Add the new activity log to the session
    db.session.commit()  # Commit the session to save the activity log

    result = activity_log_schema.dump(new_activity_log)  # Serialize the new activity log
    return jsonify(result), 201  # Return the serialized activity log with a 201 status code

# Define a route for getting a specific activity log
@activity_logs_bp.route('/<int:log_id>', methods=['GET'])
@jwt_required()  # Require a valid JWT token
def get_activity_log(log_id):
    user_id = get_jwt_identity()  # Get the user ID from the JWT token
    activity_log = ActivityLog.query.filter_by(id=log_id, user_id=user_id).first()  # Query the activity log

    # If the activity log does not exist, return an error
    if not activity_log:
        return jsonify({'error': 'Activity log not found'}), 404

    result = activity_log_schema.dump(activity_log)  # Serialize the activity log
    return jsonify(result)  # Return the serialized activity log

# Define a route for updating a specific activity log
@activity_logs_bp.route('/<int:log_id>', methods=['PUT'])
@jwt_required()  # Require a valid JWT token
def update_activity_log(log_id):
    user_id = get_jwt_identity()  # Get the user ID from the JWT token
    activity_log = ActivityLog.query.filter_by(id=log_id, user_id=user_id).first()  # Query the activity log

    # If the activity log does not exist, return an error
    if not activity_log:
        return jsonify({'error': 'Activity log not found'}), 404

    data = request.json  # Get the request data
    activity = data.get('activity')

    # Update the activity log
    activity_log.activity = activity or activity_log.activity

    db.session.commit()  # Commit the session to save the changes

    result = activity_log_schema.dump(activity_log)  # Serialize the updated activity log
    return jsonify(result)  # Return the serialized activity log

# Define a route for deleting a specific activity log
@activity_logs_bp.route('/<int:log_id>', methods=['DELETE'])
@jwt_required()  # Require a valid JWT token
def delete_activity_log(log_id):
    user_id = get_jwt_identity()  # Get the user ID from the JWT token
    activity_log = ActivityLog.query.filter_by(id=log_id, user_id=user_id).first()  # Query the activity log

    # If the activity log does not exist, return an error
    if not activity_log:
        return jsonify({'error': 'Activity log not found'}), 404

    db.session.delete(activity_log)  # Delete the activity log
    db.session.commit()  # Commit the session to save the changes

    return jsonify({'message': 'Activity log deleted successfully'}), 200  # Return a success message
