from flask_wtf import FlaskForm

from wtforms.fields import StringField, BooleanField
from wtforms.validators import Length


class TodoForm(FlaskForm):
    task = StringField('Task', [Length(min=3)])
    completed = BooleanField(label="Completed", default=False)
