from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

from todo.models import Todo
from todo.extensions import db

from todo.forms import TodoForm

todos = Blueprint('todos', __name__)


@todos.route('/')
@login_required
def index():
    all_todos = Todo.query.filter_by(creator_id=current_user.id)
    return render_template('todos/index.html', title="All", todos=all_todos)


@todos.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = TodoForm()

    if form.validate_on_submit():
        todo = Todo(task=form.task.data,
                    completed=form.completed.data, creator=current_user)

        db.session.add(todo)
        db.session.commit()
        return redirect('/todos')

    return render_template('todos/new.html', form=form)


@todos.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
@login_required
def edit(todo_id):
    todo = Todo.query.get_or_404(todo_id)

    if not todo.creator_id == current_user.id:
        return redirect('/todos')

    form = TodoForm(obj=todo)

    if form.validate_on_submit():
        todo.task = form.task.data
        todo.completed = form.completed.data
        db.session.add(todo)
        db.session.commit()
        return redirect('/todos')

    return render_template('todos/edit.html', form=form)


@todos.route('/delete/<int:todo_id>', methods=["POST"])
@login_required
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)

    if not todo.creator_id == current_user.id:
        return redirect('/todos')

    db.session.delete(todo)
    db.session.commit()
    return redirect('/todos')


@todos.route('/completed')
@login_required
def completed():
    all_todos = Todo.query.filter_by(
        creator_id=current_user.id, completed=True)
    return render_template('todos/index.html', title="Completed", todos=all_todos)


@todos.route('/remaining')
@login_required
def remaining():
    all_todos = Todo.query.filter_by(
        creator_id=current_user.id, completed=False)
    return render_template('todos/index.html', title="Remaining", todos=all_todos)
