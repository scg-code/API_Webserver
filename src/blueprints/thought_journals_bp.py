# Import necessary modules and classes
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.extensions import db
from src.models.thought_journal import ThoughtJournal, ThoughtJournalSchema

# Define the thought_journals blueprint
thought_journals_bp = Blueprint('thought_journals', __name__, url_prefix='/thought_journals')

# Create an instance of ThoughtJournalSchema
thought_journal_schema = ThoughtJournalSchema()

# Define the route for getting all thought journals for a user
@thought_journals_bp.route('', methods=['GET'])
@jwt_required()
def get_thought_journals():
    # Get the ID of the user making the request
    user_id = get_jwt_identity()

    # Query the database for all thought journals for the user
    thought_journals = ThoughtJournal.query.filter_by(user_id=user_id).all()

    # If the user has no thought journals, return a custom message
    if not thought_journals:
        return jsonify({"message": "No thought journals found for this user"}), 404

    # Serialize the thought journals and return them in a JSON response
    result = thought_journal_schema.dump(thought_journals, many=True)
    return jsonify(result)

# Define the route for creating a new thought journal
@thought_journals_bp.route('', methods=['POST'])
@jwt_required()
def create_thought_journal():
    # Get the ID of the user making the request
    user_id = get_jwt_identity()

    # Get the request data
    data = request.json

    # Get the entry from the request data
    entry = data.get('entry')

    # If the entry is empty, return an error message and a 400 Bad Request status code
    if not entry:
        return jsonify({'error': 'Entry cannot be empty'}), 400

    # Create a new thought journal with the provided entry and user ID
    new_thought_journal = ThoughtJournal(user_id=user_id, entry=entry)

    # Add the new thought journal to the database and commit the changes
    db.session.add(new_thought_journal)
    db.session.commit()

    # Serialize the new thought journal and return it in a JSON response with a 201 Created status code
    result = thought_journal_schema.dump(new_thought_journal)
    return jsonify(result), 201

# Define the route for updating a thought journal
@thought_journals_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_thought_journal(id):
    # Get the ID of the user making the request
    user_id = get_jwt_identity()

    # Query the database for the thought journal being updated
    thought_journal = ThoughtJournal.query.get(id)

    # If the thought journal does not exist, return an error message and a 404 Not Found status code
    if not thought_journal:
        return jsonify({'error': 'Thought Journal not found'}), 404

    # If the user making the request is not the one who created the thought journal, return an error message and a 403 Forbidden status code
    if thought_journal.user_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    # Get the request data
    data = request.json

    # Get the entry from the request data
    entry = data.get('entry')

    # If the entry is empty, return an error message and a 400 Bad Request status code
    if not entry:
        return jsonify({'error': 'Entry cannot be empty'}), 400

    # Update the thought journal's entry
    thought_journal.entry = entry

    # Commit the changes to the database
    db.session.commit()

    # Serialize the updated thought journal and return it in a JSON response
    result = thought_journal_schema.dump(thought_journal)
    return jsonify(result)

# Define the route for deleting a thought journal
@thought_journals_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_thought_journal(id):
    # Get the ID of the user making the request
    user_id = get_jwt_identity()

    # Query the database for the thought journal being deleted
    thought_journal = ThoughtJournal.query.get(id)

    # If the thought journal does not exist, return an error message and a 404 Not Found status code
    if not thought_journal:
        return jsonify({'error': 'Thought Journal not found'}), 404

    # If the user making the request is not the one who created the thought journal, return an error message and a 403 Forbidden status code
    if thought_journal.user_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    # Delete the thought journal from the database and commit the changes
    db.session.delete(thought_journal)
    db.session.commit()

    # Return a success message and a 200 OK status code
    return jsonify({'message': 'Thought Journal deleted'}), 200
