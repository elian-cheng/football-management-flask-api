from db import db


class Profile(db.Model):
    __tablename__ = "profile"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # The use of uselist=False in the relationship ensures that the link between the User and Profile is one-to-one.
    user = db.relationship("User", back_populates="profile", uselist=False)
