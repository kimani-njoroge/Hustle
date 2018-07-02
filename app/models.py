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
    profile = db.relationship('Profile', backref='user', lazy='dynamic')
    jobs = db.relationship('Jobs', backref='user', lazy='dynamic')
    bids = db.relationship('Bids', backref='user', lazy='dynamic')

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


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String)
    image_file = db.Column(db.String(70), nullable=False, default='default.jpg')
    cows = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    reviews = db.relationship('Reviews', backref='reviews', lazy='dynamic')


class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration = db.Column(db.String, nullable=False)
    technologies = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    bids = db.relationship('Bids', backref='jobs', lazy='dynamic')
    categories = db.relationship('Categories', backref='categories', lazy='dynamic')


class Bids(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000), nullable=False)
    cost = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    jobs_id = db.Column(db.Integer, db.ForeignKey("jobs.id"))


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000), nullable=False)
    scale = db.Column(db.Integer)
    profile_id = db.Column(db.Integer, db.ForeignKey("profile.id"))


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    jobs_id = db.Column(db.Integer, db.ForeignKey("jobs.id"))
