from flask import Blueprint, render_template, redirect

from flask_login import login_user, current_user, logout_user

from todo.models import User
from todo.extensions import db, login_manager
from todo.forms import SignupForm, LoginForm

users = Blueprint('users', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login')


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = SignupForm()

    if current_user.is_authenticated:
        return redirect('/todos')

    if form.validate_on_submit():
        user = User.create(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect('/todos')

    return render_template('users/register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect('/todos')

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one()
        login_user(user)
        return redirect('/todos')

    return render_template('users/login.html', form=form)


@users.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect('/login')
