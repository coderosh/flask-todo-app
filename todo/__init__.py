from flask import Flask, redirect

from todo.config import configs

from todo.blueprints.todo import todos
from todo.blueprints.user import users

from todo.extensions import db, csrf, login_manager, migrate


def create_app(env="dev"):
    app = Flask(__name__)
    app.config.from_object(configs[env])

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app=app, db=db, render_as_batch=True)

    app.register_blueprint(todos, url_prefix="/todos")
    app.register_blueprint(users)

    @app.route('/')
    def home():
        return redirect('/todos')

    return app
