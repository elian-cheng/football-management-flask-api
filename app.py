import os
from flask import Flask
from dotenv import load_dotenv

from db import db


load_dotenv()


# Flask Application Factory Pattern
# This allows us to pass configuration values to the function,
# enabling us to customize the application before it's returned.
def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    #  The database URL for SQLAlchemy. It defaults to a local SQLite database file named db.sqlite3
    # if the DATABASE_URL environment variable is not set.
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///db.sqlite3"
    )
    # disables the Flask-SQLAlchemy event system, improving performance.
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


app = create_app()
