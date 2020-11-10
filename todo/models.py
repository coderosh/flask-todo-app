from werkzeug.security import generate_password_hash
from flask_login import UserMixin

from todo.extensions import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, server_default='0')
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    creator = db.relationship('User', uselist=False, back_populates="todos")


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    todos = db.relationship('Todo', back_populates="creator")

    @classmethod
    def create(cls, email, password):
        hashed = generate_password_hash(password)
        return User(email=email.lower().strip(), password=hashed)
