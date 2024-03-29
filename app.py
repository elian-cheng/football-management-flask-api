import os
from flask import Flask, jsonify
from flask_smorest import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from db import db
from resources.team import blp as TeamBlueprint
from resources.club import blp as ClubBlueprint
from resources.player import blp as PlayerBlueprint
from resources.user import blp as UserBlueprint
from blocklist import BLOCKLIST

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
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    jwt = JWTManager(app)

    db.init_app(app)
    api = Api(app)

    api.register_blueprint(TeamBlueprint)
    api.register_blueprint(PlayerBlueprint)
    api.register_blueprint(ClubBlueprint)
    api.register_blueprint(UserBlueprint)

    with app.app_context():
        db.create_all()

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    return app


app = create_app()
migrate = Migrate(app, db)
