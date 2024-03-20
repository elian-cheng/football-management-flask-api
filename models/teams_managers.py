from db import db


# To establish a many-to-many relationship, typically, an associative table is utilized.
# This table contains Foreign Keys from both related models.
class TeamsManagers(db.Model):
    __tablename__ = "teams_managers"

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    manager_id = db.Column(db.Integer, db.ForeignKey("users.id"))
