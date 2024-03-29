from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# pip install Flask-Migrate
# flask db init
# flask db migrate -m "Initial migration."
# flask db upgrade


# Continuous migrations
#  flask db stamp head
#  flask db migrate
#  flask db upgrade
