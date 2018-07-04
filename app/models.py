from datetime import datetime
from flask import url_for, app, config
from werkzeug.utils import redirect
from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False)
    role = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(70), nullable=False, default='default.jpg')
    jobs = db.relationship('Jobs', backref='user', lazy='dynamic')
    bids = db.relationship('Bids', backref='user', lazy='dynamic')
    acceptbids = db.relationship('Acceptbids', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'

    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration = db.Column(db.String, nullable=False)
    technologies = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    bids = db.relationship('Bids', backref='jobs', lazy='dynamic')
    acceptbids = db.relationship('Acceptbids', backref='jobs', lazy='dynamic')


class Bids(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000), nullable=False)
    cost = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    jobs_id = db.Column(db.Integer, db.ForeignKey("jobs.id"))
    acceptbids = db.relationship('Acceptbids', backref='bids', lazy='dynamic')


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000), nullable=False)
    scale = db.Column(db.Integer)


class Acceptbids(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accepted_bid = db.Column(db.Integer, db.ForeignKey("bids.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    jobs_id = db.Column(db.Integer, db.ForeignKey("jobs.id"))


class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)
