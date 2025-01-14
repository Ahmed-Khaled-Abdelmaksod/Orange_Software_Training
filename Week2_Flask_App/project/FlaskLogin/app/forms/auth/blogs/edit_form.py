from flask_wtf import FlaskForm
from wtforms import StringField, FloatField,IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class EditForm(FlaskForm):
    title = StringField("title", validators=[DataRequired(), Length(min=5, max=20)])
    description = FloatField("description", validators=[DataRequired(), NumberRange(min=1)])
    author_id = IntegerField("author_id", validators=[DataRequired()])
    id = IntegerField("id", validators=[DataRequired()])