from todo.extensions import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, server_default='0')
