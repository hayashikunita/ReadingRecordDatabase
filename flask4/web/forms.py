# web/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('書籍', validators=[DataRequired()])
    author = StringField('著者', validators=[DataRequired()])
    genre = StringField('ジャンル')
    date = DateField('読了日', format="%Y-%m-%d")
    submit = SubmitField('登録')