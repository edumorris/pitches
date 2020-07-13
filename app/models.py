from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__='users'
    u_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")
    pitchs = db.relationship('Pitch', backref = 'pitch', lazy = "dynamic")
    password = db.Column(db.String9(255))

    def __repr__(self):
        return f'User {self.username}'

class Comment(db.Model):
    __tablename__='comments'
    comm_id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(10000))
    for_pitch = db.Column(db.Integer, db.ForeignKey("pitches.pitch_id"))
    submitted_by = db.Column(db.Integer, db.ForeignKey("users.u_id"))
    pitchs = db.relationship('Pitch', backref = 'pitch', lazy = "dynamic")

class Pitch(db.Model):
    __tablename__='pitches'
    pitch_id = db.Column(db.Integer, primary_key = True)
    pitch = db.Column(db.String(100000))
    category = db.Column(db.String(255))
    upvotes = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    submitted_by = db.Column(db.Integer, db.ForeignKey("users.u_id"))