import os
from flask import Flask
from flask_smorest import Api
from dotenv import load_dotenv
from db import db
from resources.team import blp as TeamBlueprint
from resources.club import blp as ClubBlueprint
from resources.player import blp as PlayerBlueprint
from resources.user import blp as UserBlueprint
from flask_migrate import Migrate

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
    app.config["API_TITLE"] = "FC Manager REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"

    db.init_app(app)
    api = Api(app)

    api.register_blueprint(TeamBlueprint)
    api.register_blueprint(PlayerBlueprint)
    api.register_blueprint(ClubBlueprint)
    api.register_blueprint(UserBlueprint)

    with app.app_context():
        db.create_all()

    return app


app = create_app()

migrate = Migrate(app, db)
