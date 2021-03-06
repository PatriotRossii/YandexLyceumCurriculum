from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, IntegerField, StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = IntegerField("ID руководителя", validators=[DataRequired()])
    job = StringField("Описание работы", validators=[DataRequired()])
    work_size = IntegerField("Объем работы в часах", validators=[DataRequired()])
    collaborators = StringField("Список ID участников", validators=[DataRequired()])
    is_finished = BooleanField("Завершена ли работа")

    submit = SubmitField('Создать')
