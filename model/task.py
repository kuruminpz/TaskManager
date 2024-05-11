from app import db
from datetime import datetime


class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description =db.Column(db.String(256), nullable=False)
    end_date = db.Column(db.Datetime, nullable=True)
    start_date = db.Column(db.dateTime, default=datetime.now)
    status = db.Column(db.String(16), nullable=False)