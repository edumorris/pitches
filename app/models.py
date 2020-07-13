from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__='users'
    u_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")
    pitchs = db.relationship('Pitch', backref = 'pitch', lazy = "dynamic")
    pwd = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password')

    @password.setter
    def password(self, password):
        self.pwd = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.pwd, password)

    def __repr__(self):
        return f'User {self.username}'

from . import login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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