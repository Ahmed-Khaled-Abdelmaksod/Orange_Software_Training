from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    email = db.Column(db.String(20), primary_key=True)
    public_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10),nullable = False)

    # Define the relationship from the user side to link to multiple blogs
    blogs = db.relationship('blog', back_populates='author', lazy=True)