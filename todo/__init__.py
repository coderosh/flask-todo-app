from flask import Flask

from todo.config import configs

from todo.blueprints.todo import todos
from todo.blueprints.user import users

from todo.extensions import db, csrf, login_manager


def create_app(env="dev"):
    app = Flask(__name__)
    app.config.from_object(configs[env])

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(todos, url_prefix="/todos")
    app.register_blueprint(users)

    return app
