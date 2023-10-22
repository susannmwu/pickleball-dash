from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String, nullable=False)

    datapoints = db.relationship("PickleballData", back_populates="user")

    def __repr__(self):
        return f"<User first_name={self.first_name}>"


class PickleballData(db.Model):
    """A pickleball session"""
    __tablename__ = "pickleball_data"

    data_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    startDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)
    activityType = db.Column(db.String, nullable=False)
    # duration = db.Column(db.Integer, nullable=False)
    # HKWeatherHumidity = db.Column(db.String, nullable=True)
    # totalEnergyBurned = db.Column(db.Integer, nullable=False)
    # HKWeatherTemperature = db.Column(db.Integer, nullable=False)

    user = db.relationship("User", back_populates="datapoints")

    def __repr__(self):
        return f"<Input data_id={self.data_id}>"


def connect_to_db(flask_app, db_uri="postgresql:///workouts", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
