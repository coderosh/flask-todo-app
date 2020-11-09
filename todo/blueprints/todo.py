from flask import Blueprint

todos = Blueprint('todos', __name__)


@todos.route('/')
def index():
    return "All Todos"


@todos.route('/completed')
def completed():
    return "All Completed todos"


@todos.route('/remaining')
def remaining():
    return "All remaining todos"
