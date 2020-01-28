from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import ValidationError, DataRequired, Email
from app.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
