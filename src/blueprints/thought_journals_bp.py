# src/blueprints/thought_journals_bp.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.extensions import db
from src.models.thought_journal import ThoughtJournal, ThoughtJournalSchema

thought_journals_bp = Blueprint('thought_journals', __name__, url_prefix='/thought_journals')
thought_journal_schema = ThoughtJournalSchema()

@thought_journals_bp.route('', methods=['GET'])
@jwt_required()
def get_thought_journals():
    user_id = get_jwt_identity()
    thought_journals = ThoughtJournal.query.filter_by(user_id=user_id).all()
    result = thought_journal_schema.dump(thought_journals, many=True)
    return jsonify(result)

@thought_journals_bp.route('', methods=['POST'])
@jwt_required()
def create_thought_journal():
    user_id = get_jwt_identity()
    data = request.json
    entry = data.get('entry')

    if not entry:
        return jsonify({'error': 'Entry cannot be empty'}), 400

    new_thought_journal = ThoughtJournal(user_id=user_id, entry=entry)
    db.session.add(new_thought_journal)
    db.session.commit()

    result = thought_journal_schema.dump(new_thought_journal)
    return jsonify(result), 201

@thought_journals_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_thought_journal(id):
    user_id = get_jwt_identity()
    thought_journal = ThoughtJournal.query.get(id)

    if not thought_journal:
        return jsonify({'error': 'Thought Journal not found'}), 404

    if thought_journal.user_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.json
    entry = data.get('entry')

    if not entry:
        return jsonify({'error': 'Entry cannot be empty'}), 400

    thought_journal.entry = entry
    db.session.commit()

    result = thought_journal_schema.dump(thought_journal)
    return jsonify(result)

@thought_journals_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_thought_journal(id):
    user_id = get_jwt_identity()
    thought_journal = ThoughtJournal.query.get(id)

    if not thought_journal:
        return jsonify({'error': 'Thought Journal not found'}), 404

    if thought_journal.user_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    db.session.delete(thought_journal)
    db.session.commit()

    return jsonify({'message': 'Thought Journal deleted'}), 200
