# Import necessary modules and classes
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.extensions import db
from src.models.goal import Goal, GoalSchema

# Define the goals blueprint
goals_bp = Blueprint('goals', __name__, url_prefix='/goals')

# Create an instance of GoalSchema for serializing and deserializing goals
goal_schema = GoalSchema()

# Define the route for getting all goals
@goals_bp.route('', methods=['GET'])
@jwt_required()  # Require a valid JWT token to access this route
def get_goals():
    # Get the ID of the user making the request
    user_id = get_jwt_identity()

    # Query the database for all goals belonging to the user
    goals = Goal.query.filter_by(user_id=user_id).all()

    # Serialize the goals and return them in a JSON response
    result = goal_schema.dump(goals, many=True)
    return jsonify(result)

# Define the route for creating a new goal
@goals_bp.route('', methods=['POST'])
@jwt_required()  # Require a valid JWT token to access this route
def create_goal():
    # Get the ID of the user making the request
    user_id = get_jwt_identity()

    # Get the request data
    data = request.json

    # Get the goal, description, and deadline from the request data
    goal = data.get('goal')
    description = data.get('description')
    deadline = data.get('deadline')

    # If the description is not provided, return an error message and a 400 Bad Request status code
    if not description:
        return jsonify({'error': 'Description cannot be empty'}), 400

    # Create a new goal with the provided data
    new_goal = Goal(user_id=user_id, goal=goal, description=description, deadline=deadline)

    # Add the new goal to the database and commit the changes
    db.session.add(new_goal)
    db.session.commit()

    # Serialize the new goal and return it in a JSON response with a 201 Created status code
    result = goal_schema.dump(new_goal)
    return jsonify(result), 201

# Define the route for updating a goal
@goals_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()  # Require a valid JWT token to access this route
def update_goal(id):
    # Get the ID of the user making the request
    user_id = get_jwt_identity()

    # Query the database for the specified goal
    goal = Goal.query.get(id)

    # If the goal does not exist, return an error message and a 404 Not Found status code
    if not goal:
        return jsonify({'error': 'Goal not found'}), 404

    # If the user making the request is not the one who created the goal, return an error message and a 403 Forbidden status code
    if goal.user_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    # Get the request data
    data = request.json

    # Get the description, deadline, and status from the request data
    description = data.get('description')
    deadline = data.get('deadline')
    status = data.get('status')

    # If the description is not provided, return an error message and a 400 Bad Request status code
    if not description:
        return jsonify({'error': 'Description cannot be empty'}), 400

    # Update the goal's description, deadline, and status with the provided data
    goal.description = description
    goal.deadline = deadline
    goal.status = status

    # Commit the changes to the database
    db.session.commit()

    # Serialize the updated goal and return it in a JSON response
    result = goal_schema.dump(goal)
    return jsonify(result)

# Define the route for deleting a goal
@goals_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()  # Require a valid JWT token to access this route
def delete_goal(id):
    # Get the ID of the user making the request
    user_id = get_jwt_identity()

    # Query the database for the specified goal
    goal = Goal.query.get(id)

    # If the goal does not exist, return an error message and a 404 Not Found status code
    if not goal:
        return jsonify({'error': 'Goal not found'}), 404

    # If the user making the request is not the one who created the goal, return an error message and a 401 Unauthorized status code
    if goal.user_id != user_id:
        return jsonify({'error': 'You do not have permission to delete this goal'}), 401

    # Delete the goal from the database and commit the changes
    db.session.delete(goal)
    db.session.commit()

    # Return a success message and a 200 OK status code
    return jsonify({'message': 'Goal deleted'}), 200