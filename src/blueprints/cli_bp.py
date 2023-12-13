from flask import Blueprint
from flask.cli import with_appcontext, current_app
from src.extensions import db, bcrypt  # Adjust the path as needed
from src.models.user import User
from src.models.mood_entry import MoodEntry
from src.models.thought_journal import ThoughtJournal
from src.models.goal import Goal
from src.models.activity_log import ActivityLog
from datetime import datetime

# Create a new Blueprint for database-related commands
db_commands = Blueprint('db', __name__)

# Define a new command for the Flask CLI
@db_commands.cli.command("create")
def db_create():
    db.drop_all()  # Drop all tables in the database
    db.create_all()  # Create all tables in the database
    print("Created tables")  # Print a success message

# Define another command for the Flask CLI
@db_commands.cli.command("seed")
@with_appcontext  # Ensure the command runs in the application context
def db_seed():
    # Dummy Users
    users = [
        User(
            name="Sam Gifford",
            email="admin@moodnest.com",
            password=bcrypt.generate_password_hash("admin123").decode("utf8"),
            is_admin=True,
        ),
        User(
            name="Sarah Jane",
            email="sarahjane99@gmail.com",
            password=bcrypt.generate_password_hash("puppy12345").decode("utf8"),
        ),
        User(
            name="Andrew Tate",
            email="TopG69@gmail.com",
            password=bcrypt.generate_password_hash("bugatti222").decode("utf8"),
        ),
    ]

    db.session.add_all(users)
    db.session.commit()
    print("Users Seeded")


    # Dummy Mood Entries
    mood_entries = [
        # 7 mood entries for user_id=1
        MoodEntry(user_id=1, mood="Happy", mood_intensity=8, note="Feeling great today!", timestamp=datetime.utcnow()),
        MoodEntry(user_id=1, mood="Sad", mood_intensity=2, note="Not feeling well.", timestamp=datetime.utcnow()),
        MoodEntry(user_id=1, mood="Sad", mood_intensity=3, note="Had a tough day.", timestamp=datetime.utcnow()),
        MoodEntry(user_id=1, mood="Sad", mood_intensity=2, note="Feeling down.", timestamp=datetime.utcnow()),
        MoodEntry(user_id=1, mood="Sad", mood_intensity=1, note="Very tough day.", timestamp=datetime.utcnow()),
        MoodEntry(user_id=1, mood="Sad", mood_intensity=2, note="Not my day.", timestamp=datetime.utcnow()),
        MoodEntry(user_id=1, mood="Sad", mood_intensity=3, note="Feeling very low.", timestamp=datetime.utcnow()),
        
        # 7 mood entries for user_id=2
        MoodEntry(user_id=2, mood="Excited", mood_intensity=9, note="Looking forward to the weekend!", timestamp=datetime.utcnow()),
        MoodEntry(user_id=2, mood="Happy", mood_intensity=7, note="Good day at work.", timestamp=datetime.utcnow()),
        MoodEntry(user_id=2, mood="Content", mood_intensity=6, note="Relaxed day.", timestamp=datetime.utcnow()),
        MoodEntry(user_id=2, mood="Happy", mood_intensity=8, note="Had a great workout.", timestamp=datetime.utcnow()),
        MoodEntry(user_id=2, mood="Excited", mood_intensity=9, note="Going on a trip tomorrow!", timestamp=datetime.utcnow()),
        MoodEntry(user_id=2, mood="Happy", mood_intensity=7, note="Caught up with an old friend.", timestamp=datetime.utcnow()),
        MoodEntry(user_id=2, mood="Content", mood_intensity=6, note="Enjoyed a good book.", timestamp=datetime.utcnow()),
    ]

    db.session.add_all(mood_entries)
    db.session.commit()
    print("Mood Entries Seeded")


# Dummy Thought Journals
    thought_journals = [
    ThoughtJournal(
        user_id=1,
        entry=("Today was an amazing day! I woke up early, went for a long run, and then spent the afternoon reading my favorite book. "
               "The weather was perfect, and I felt a sense of gratitude for the simple joys in life. It's incredible how a day filled with positive experiences can uplift the spirit."),
        timestamp=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),  # Format timestamp
    ),
        ThoughtJournal(
            user_id=2,
            entry="Feeling a bit overwhelmed with work. The deadlines are approaching, and there's so much to do. Taking a deep breath and planning to tackle one task at a time. Despite the challenges, I find solace in the progress I've made so far. It's a reminder that every step forward is an achievement.",
            timestamp=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),  # Format timestamp
        ),
        ThoughtJournal(
            user_id=3,
            entry="Planning a road trip with friends! We're mapping out the route, deciding on interesting stops, and looking forward to creating wonderful memories together. It's going to be an adventure! The excitement of exploring new places and spending quality time with friends brings a sense of anticipation and joy.",
            timestamp=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),  # Format timestamp
        ),
    ]

    db.session.add_all(thought_journals)
    db.session.commit()
    print("Thought Journals Seeded")


# Dummy Goals
    goals = [
        Goal(
            user_id=1,
            goal="Learn a new programming language",
            description="I want to expand my skill set by learning a new programming language.",
            deadline=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            status="Completed",
        ),
        Goal(
            user_id=2,
            goal="Complete a marathon",
            description="I have a goal to run a full marathon and improve my endurance.",
            deadline=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            status="Pending",
        ),
        Goal(
            user_id=3,
            goal="Read 20 books this year",
            description="I aim to read 20 books within the next year to broaden my knowledge.",
            deadline=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            status="Pending",
        ),
    ]

    db.session.add_all(goals)
    db.session.commit()
    print("Goals Seeded")


# Dummy Activities
    activities = [
        ActivityLog(user_id=1, activity="Running", timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')),
        ActivityLog(user_id=2, activity="Yoga", timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')),
        ActivityLog(user_id=3, activity="Gaming", timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')),
        ActivityLog(user_id=1, activity="Cycling", timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')),
        ActivityLog(user_id=2, activity="Reading", timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')),
        ActivityLog(user_id=3, activity="Swimming", timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    ]

    with current_app.app_context():
        db.session.add_all(activities)
        db.session.commit()
        print("Activities Seeded")

