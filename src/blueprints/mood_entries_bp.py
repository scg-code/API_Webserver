from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.extensions import db
from src.models.mood_entry import MoodEntry, MoodEntrySchema
from datetime import datetime
from werkzeug.exceptions import NotFound, HTTPException
from marshmallow.exceptions import ValidationError

# Define the mood_entries blueprint
mood_entries_bp = Blueprint('mood_entries', __name__)

# Define the route for getting all mood entries
@mood_entries_bp.route('/mood_entries', methods=['GET'])
@jwt_required() 
def get_mood_entries():
    # Get the ID of the logged-in user
    user_id = get_jwt_identity()

    # Query the database for all mood entries created by the logged-in user
    mood_entries = MoodEntry.query.filter_by(user_id=user_id).all()

    # Create an instance of MoodEntrySchema for serializing multiple mood entries
    mood_entries_schema = MoodEntrySchema(many=True)

    # Serialize the mood entries and return them in a JSON response
    result = mood_entries_schema.dump(mood_entries)
    return jsonify(result)

@mood_entries_bp.errorhandler(HTTPException)
def handle_auth_error(e):
    if 'Missing Authorization Header' in str(e):
        response = jsonify({"message": "Missing or invalid JWT token"})
        response.status_code = 401  # Unauthorized
        return response
    return e

# Define the route for getting a specific mood entry
@mood_entries_bp.route('/mood_entries/<int:mood_entry_id>', methods=['GET'])
@jwt_required()  
def get_mood_entry(mood_entry_id):
    # Get the ID of the logged-in user
    user_id = get_jwt_identity()

    # Query the database for the specified mood entry, or return a 404 error if it does not exist
    mood_entry = MoodEntry.query.get_or_404(mood_entry_id)

    # Check if the logged-in user is the creator of the mood entry
    if mood_entry.user_id != user_id:
        return jsonify({"message": "You do not have permission to access this resource"}), 403

    # Create an instance of MoodEntrySchema for serializing a single mood entry
    mood_entry_schema = MoodEntrySchema()

    # Serialize the mood entry and return it in a JSON response
    result = mood_entry_schema.dump(mood_entry)
    return jsonify(result)

# Define a route for creating a new mood entry
@mood_entries_bp.route('/mood_entries', methods=['POST'])
@jwt_required()  # Require a valid JWT token to access this route
def create_mood_entry():
    # Get the request data
    data = request.json

    # Create an instance of MoodEntrySchema for deserializing the request data
    mood_entry_schema = MoodEntrySchema()

    try:
        # Get the ID of the user making the request
        user_id = get_jwt_identity()

        # Add the user ID to the request data
        data['user_id'] = user_id

        # Deserialize the request data into a dictionary
        deserialized_data = mood_entry_schema.load(data)

        # Create a new mood entry with the deserialized data
        new_mood_entry = MoodEntry(**deserialized_data)

        # Add the new mood entry to the database and commit the changes
        db.session.add(new_mood_entry)
        db.session.commit()

        # Serialize the new mood entry and return it in a JSON response with a 201 Created status code
        result = mood_entry_schema.dump(new_mood_entry)
        return jsonify(result), 201
    except ValidationError as e:
        # If a validation error occurs, return the error messages and a 400 Bad Request status code
        return jsonify({'error': 'Validation error', 'messages': e.messages}), 400
    except Exception as e:
        # If an error occurs, return the error message and a 400 Bad Request status code
        return jsonify({'error': str(e)}), 400

# Define the route for deleting a mood entry
@mood_entries_bp.route('/mood_entries/<int:mood_entry_id>', methods=['DELETE'])
@jwt_required()
def delete_mood_entry(mood_entry_id):
    try:
        # Query the database for the specified mood entry, or return a 404 error if it does not exist
        mood_entry = MoodEntry.query.get_or_404(mood_entry_id)

        # Get the ID of the user making the request
        user_id = get_jwt_identity()

        # If the user making the request is not the one who created the mood entry, return an error message and a 401 Unauthorized status code
        if mood_entry.user_id != user_id:
            return jsonify({'error': 'You do not have permission to delete this resource'}), 401

        # Delete the mood entry from the database and commit the changes
        db.session.delete(mood_entry)
        db.session.commit()

        # Return a success message and a 200 OK status code
        return {"message": "Mood entry deleted successfully"}, 200
    except NotFound:
        # If a NotFound exception is raised, return a custom error message and a 404 Not Found status code
        return {"error": "Mood entry not found"}, 404
    

# Define the route for updating a mood entry
@mood_entries_bp.route('/mood_entries/<int:mood_entry_id>', methods=['PUT'])
@jwt_required()  # Require a valid JWT token to access this route
def update_mood_entry(mood_entry_id):
    # Query the database for the specified mood entry, or return a 404 error if it does not exist
    mood_entry = MoodEntry.query.get_or_404(mood_entry_id)

    # Get the request data
    data = request.json

    # Validate mood_intensity
    mood_intensity = data.get('mood_intensity', mood_entry.mood_intensity)
    if not 1 <= mood_intensity <= 10:
        return jsonify({'error': 'mood_intensity must be an integer between 1 and 10'}), 400

    # Create an instance of MoodEntrySchema for deserializing the request data
    mood_entry_schema = MoodEntrySchema()

    try:
        # Get the ID of the user making the request
        user_id = get_jwt_identity()

        # If the user making the request is not the one who created the mood entry, return an error message and a 401 Unauthorized status code
        if mood_entry.user_id != user_id:
            return jsonify({'error': 'You do not have permission to update this resource'}), 401

        # Update the mood entry's mood, mood_intensity and note with the provided data, or keep the current values if no data is provided
        mood_entry.mood = data.get('mood', mood_entry.mood)
        mood_entry.mood_intensity = mood_intensity
        mood_entry.note = data.get('note', mood_entry.note)

        # Set the timestamp to the current date and time
        mood_entry.timestamp = datetime.utcnow()

        # Commit the changes to the database
        db.session.commit()

        # Serialize the updated mood entry and return it in a JSON response with a 200 OK status code
        result = mood_entry_schema.dump(mood_entry)
        return jsonify(result), 200
    except Exception as e:
        # If an error occurs, return the error message and a 400 Bad Request status code
        return jsonify({'error': str(e)}), 400
    

# Define the route for getting a depression warning
@mood_entries_bp.route('/depression_warning', methods=['GET'])
@jwt_required()  # Require a valid JWT token to access this route
def get_depression_warning():
    # Get the ID of the user making the request
    user_id = get_jwt_identity()

    # Query the database for the user's last 7 mood entries
    mood_entries = MoodEntry.query.filter_by(user_id=user_id)\
                                  .order_by(MoodEntry.timestamp.desc())\
                                  .limit(7)\
                                  .all()

    # If the user has less than 7 mood entries, return a message indicating that not enough data is available
    if len(mood_entries) < 7:
        return jsonify({'message': 'Not enough data to determine depression warning.'}), 200

    # Calculate the average mood intensity of the last 7 mood entries
    total_mood_intensity = sum([mood_entry.mood_intensity for mood_entry in mood_entries])
    average_mood_intensity = total_mood_intensity / 7

    # If the average mood intensity is less than or equal to 3, return a depression warning
    if average_mood_intensity <= 3:
        return jsonify({'warning': 'Depression warning: Your average mood intensity over the last week is very low.'}), 200

    # If the average mood intensity is greater than 3, return a message indicating that no depression warning is necessary
    return jsonify({'message': 'No depression warning necessary.'}), 200