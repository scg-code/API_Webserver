# src/blueprints/goals_bp.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.extensions import db
from src.models.goal import Goal, GoalSchema

goals_bp = Blueprint('goals', __name__, url_prefix='/goals')
goal_schema = GoalSchema()

@goals_bp.route('', methods=['GET'])
@jwt_required()
def get_goals():
    user_id = get_jwt_identity()
    goals = Goal.query.filter_by(user_id=user_id).all()
    result = goal_schema.dump(goals, many=True)
    return jsonify(result)

@goals_bp.route('', methods=['POST'])
@jwt_required()
def create_goal():
    user_id = get_jwt_identity()
    data = request.json
    description = data.get('description')
    due_date = data.get('due_date')

    if not description:
        return jsonify({'error': 'Description cannot be empty'}), 400

    new_goal = Goal(user_id=user_id, description=description, due_date=due_date)
    db.session.add(new_goal)
    db.session.commit()

    result = goal_schema.dump(new_goal)
    return jsonify(result), 201

@goals_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_goal(id):
    user_id = get_jwt_identity()
    goal = Goal.query.get(id)

    if not goal:
        return jsonify({'error': 'Goal not found'}), 404

    if goal.user_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.json
    description = data.get('description')
    due_date = data.get('due_date')

    if not description:
        return jsonify({'error': 'Description cannot be empty'}), 400

    goal.description = description
    goal.due_date = due_date
    db.session.commit()

    result = goal_schema.dump(goal)
    return jsonify(result)

@goals_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_goal(id):
    user_id = get_jwt_identity()
    goal = Goal.query.get(id)

    if not goal:
        return jsonify({'error': 'Goal not found'}), 404

    if goal.user_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    db.session.delete(goal)
    db.session.commit()

    return jsonify({'message': 'Goal deleted'}), 200
