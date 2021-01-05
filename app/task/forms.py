from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class TaskCreateForm(FlaskForm):
    id = HiddenField('ID')
    name = StringField('Название', validators=[DataRequired()])
    start_pos = HiddenField('Начальная позиция', validators=[DataRequired()], default='start')
    end_pos = HiddenField('Конечная позиция', validators=[DataRequired()], default='end')
    submit = SubmitField('Добавить')
