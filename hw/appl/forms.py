# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import RadioField, TextAreaField
from wtforms.validators import DataRequired


class Footnote(FlaskForm):
    footnote = TextAreaField('Type in your note:',
                             validators=[DataRequired()])
    submit = SubmitField('Send')
