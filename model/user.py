from app import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True,nullable=False)
    password = db.Column(db.String(128), nullable=True)

    def __init__(self):
        pass