# Importing the blueprints for different parts of the application
from src.blueprints.main_bp import main_bp  # Blueprint for the main part of the application
from src.blueprints.users_bp import users_bp  # Blueprint for user-related routes
from src.blueprints.cli_bp import db_commands  # Blueprint for database commands
from src.blueprints.mood_entries_bp import mood_entries_bp  # Blueprint for mood entry routes
from src.blueprints.thought_journals_bp import thought_journals_bp  # Blueprint for thought journal routes
from src.blueprints.goals_bp import goals_bp  # Blueprint for goal-related routes
from src.blueprints.activity_logs_bp import activity_logs_bp  # Blueprint for activity log routes

# Importing the Flask application instance
from src.extensions import app  

# Registering the blueprints with the Flask application
app.register_blueprint(main_bp)  # Register the main blueprint
app.register_blueprint(users_bp)  # Register the users blueprint
app.register_blueprint(db_commands)  # Register the database commands blueprint
app.register_blueprint(mood_entries_bp)  # Register the mood entries blueprint
app.register_blueprint(thought_journals_bp)  # Register the thought journals blueprint
app.register_blueprint(goals_bp)  # Register the goals blueprint
app.register_blueprint(activity_logs_bp)  # Register the activity logs blueprint

for rule in app.url_map.iter_rules():
    print(rule)