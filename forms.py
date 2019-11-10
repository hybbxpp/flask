from flask_wtf import Form
from wtforms import StringField, BooleanField,  TextAreaField, SelectMultipleField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
import datetime
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from .models import Tasks

class TaskForm(Form):
    name = StringField('name', validators=[DataRequired()])
    year = DateField('year', validators=[DataRequired()])
    urgent = SelectField('state',choices=[('None', 'None'), ('Yes', 'Yes'), ('No', 'No'), ], validators=[DataRequired()])