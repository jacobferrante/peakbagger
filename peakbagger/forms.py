from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CreateHike(FlaskForm):
    name = StringField('Name', render_kw={"placeholder": "Name"}, validators=[DataRequired(), Length(min=2, max=30)])
    notes = StringField('Notes', render_kw={"placeholder": "Notes"}, validators=[DataRequired(), Length(min=2, max=100)])
    link = StringField('Strava', render_kw={"placeholder": "Link"}, validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Save Hike')
