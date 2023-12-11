# src/blueprints/activity_logs_bp.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.extensions import db
from src.models.activity_log import ActivityLog, ActivityLogSchema

activity_logs_bp = Blueprint('activity_logs', __name__, url_prefix='/activity_logs')
activity_log_schema = ActivityLogSchema()

@activity_logs_bp.route('', methods=['GET'])
@jwt_required()
def get_activity_logs():
    user_id = get_jwt_identity()
    activity_logs = ActivityLog.query.filter_by(user_id=user_id).all()
    result = activity_log_schema.dump(activity_logs, many=True)
    return jsonify(result)

@activity_logs_bp.route('', methods=['POST'])
@jwt_required()
def create_activity_log():
    user_id = get_jwt_identity()
    data = request.json

    new_activity_log = ActivityLog(user_id=user_id, activity=data.get('activity'))
    db.session.add(new_activity_log)
    db.session.commit()

    result = activity_log_schema.dump(new_activity_log)
    return jsonify(result), 201


@activity_logs_bp.route('/<int:log_id>', methods=['GET'])
@jwt_required()
def get_activity_log(log_id):
    user_id = get_jwt_identity()
    activity_log = ActivityLog.query.filter_by(id=log_id, user_id=user_id).first()

    if not activity_log:
        return jsonify({'error': 'Activity log not found'}), 404

    result = activity_log_schema.dump(activity_log)
    return jsonify(result)

@activity_logs_bp.route('/<int:log_id>', methods=['PUT'])
@jwt_required()
def update_activity_log(log_id):
    user_id = get_jwt_identity()
    activity_log = ActivityLog.query.filter_by(id=log_id, user_id=user_id).first()

    if not activity_log:
        return jsonify({'error': 'Activity log not found'}), 404

    data = request.json
    activity_id = data.get('activity_id')
    intensity = data.get('intensity')

    activity_log.activity_id = activity_id or activity_log.activity_id
    activity_log.intensity = intensity or activity_log.intensity

    db.session.commit()

    result = activity_log_schema.dump(activity_log)
    return jsonify(result)

@activity_logs_bp.route('/<int:log_id>', methods=['DELETE'])
@jwt_required()
def delete_activity_log(log_id):
    user_id = get_jwt_identity()
    activity_log = ActivityLog.query.filter_by(id=log_id, user_id=user_id).first()

    if not activity_log:
        return jsonify({'error': 'Activity log not found'}), 404

    db.session.delete(activity_log)
    db.session.commit()

    return jsonify({'message': 'Activity log deleted successfully'}), 200
