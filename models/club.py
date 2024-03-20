from db import db


class ClubModel(db.Model):
    __tablename__ = "clubs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    main_stadium = db.Column(db.String(50), nullable=False)
    est = db.Column(db.Date, nullable=False)
    teams = db.relationship("TeamModel", back_populates="club", lazy="dynamic")


# The lazy="dynamic" option is crucial for addressing the N+1 query problem, a common issue
# where a separate database query is executed for each of the N-related objects, plus an
# additional query for the primary object.
# This scenario can significantly degrade performance, especially with large datasets.
