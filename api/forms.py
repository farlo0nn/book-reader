from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField, Field
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    name = StringField("Book Name", validators=[DataRequired()])
    pages = IntegerField("Book Pages", validators=[DataRequired()])
    author_name = StringField("Author Name", validators=[DataRequired()])
    submit=SubmitField()
    