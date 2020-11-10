from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash


from wtforms.fields import StringField, BooleanField, PasswordField
from wtforms.validators import Length, email, required, EqualTo

from todo.models import User


class TodoForm(FlaskForm):
    task = StringField('Task', [Length(min=3)])
    completed = BooleanField(label="Completed", default=False)


class SignupForm(FlaskForm):
    email = StringField('Email', [email(), required()])
    password = PasswordField('Password', [required(), Length(min=4, max=20)])
    confirm = PasswordField('Confirm Password', [required(), EqualTo(
        'password', message="Passwords must match")])

    def validate(self):
        is_valid = super(SignupForm, self).validate()
        if not is_valid:
            return False

        user = User.query.filter_by(email=self.email.data).first()

        if user:
            self.email.errors.append("Email is already in use")
            return False

        return True


class LoginForm(FlaskForm):
    email = StringField('Email', [email(), required()])
    password = PasswordField('Password', [required()])

    def validate(self):
        is_valid = super(LoginForm, self).validate()

        if not is_valid:
            return False

        user = User.query.filter_by(email=self.email.data).first()

        if not user or not check_password_hash(user.password, self.password.data):
            self.email.errors.append("Invalid Credentials")
            self.password.errors.append("Invalid Credentials")
            return False

        return True
