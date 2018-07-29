from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import Nonprofit, Item

class SearchForm(FlaskForm):
    search = StringField('Find a Nonprofit', validators=[DataRequired()], render_kw={"value": "San Francisco"})
    submit = SubmitField('Search')

