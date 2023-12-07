from src.blueprints.main_bp import main_bp
from src.blueprints.users_bp import users_bp
from src.blueprints.cli_bp import db_commands
from src.blueprints.mood_entries_bp import mood_entries_bp
from src.extensions import app  

app.register_blueprint(main_bp)
app.register_blueprint(users_bp)
app.register_blueprint(db_commands)
app.register_blueprint(mood_entries_bp)



