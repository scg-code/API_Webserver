# mood_entries_bp.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.extensions import db
from src.models.mood_entry import MoodEntry, MoodEntrySchema
from datetime import datetime

mood_entries_bp = Blueprint('mood_entries', __name__)

@mood_entries_bp.route('/mood_entries', methods=['GET'])
def get_mood_entries():
    mood_entries = MoodEntry.query.all()
    mood_entries_schema = MoodEntrySchema(many=True)
    result = mood_entries_schema.dump(mood_entries)
    return jsonify(result)

@mood_entries_bp.route('/mood_entries/<int:mood_entry_id>', methods=['GET'])
def get_mood_entry(mood_entry_id):
    mood_entry = MoodEntry.query.get_or_404(mood_entry_id)
    mood_entry_schema = MoodEntrySchema()
    result = mood_entry_schema.dump(mood_entry)
    return jsonify(result)

@mood_entries_bp.route('/mood_entries', methods=['POST'])
@jwt_required()
def create_mood_entry():
    data = request.json
    mood_entry_schema = MoodEntrySchema()

    try:
        # Get the user_id from the current user using get_jwt_identity()
        user_id = get_jwt_identity()

        # Set the timestamp to the current date and time
        timestamp = datetime.utcnow()

        # Add user_id and timestamp to the data dictionary
        data['user_id'] = user_id
        data['timestamp'] = timestamp

        # Use load to deserialize JSON data into a dictionary
        deserialized_data = mood_entry_schema.load(data)

        # Create a MoodEntry instance using the deserialized data
        new_mood_entry = MoodEntry(**deserialized_data)

        # Add the instance to the session
        db.session.add(new_mood_entry)

        # Commit the changes to the database
        db.session.commit()

        # Serialize the created MoodEntry and return the result
        result = mood_entry_schema.dump(new_mood_entry)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@mood_entries_bp.route('/mood_entries/<int:mood_entry_id>', methods=['DELETE'])
def delete_mood_entry(mood_entry_id):
    mood_entry = MoodEntry.query.get_or_404(mood_entry_id)
    db.session.delete(mood_entry)
    db.session.commit()
    return jsonify({'message': 'Mood entry deleted successfully'})

# Additional routes (e.g., update) can be added as needed
