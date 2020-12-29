from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class TaskCreateForm(FlaskForm):
    id = IntegerField('ID')
    name = StringField('Название', validators=[DataRequired()])
    start_pos = StringField('Начальная позиция', validators=[DataRequired()])
    end_pos = StringField('Конечная позиция', validators=[DataRequired()])
    submit = SubmitField('Добавить')
