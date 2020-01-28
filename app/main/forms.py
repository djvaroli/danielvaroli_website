from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import ValidationError, Email, DataRequired

class ContactForm(FlaskForm):
    name = StringField(render_kw={'placeholder':'Your name goes here'}, validators=[DataRequired()])
    email = StringField('Email', render_kw={'placeholder':"I'm going to need your email as well"}, validators=[DataRequired(),Email()])
    message = TextAreaField('Message', render_kw={'placeholder':'Tell me everything...'}, validators=[DataRequired()])
    recaptcha = RecaptchaField("Just checking you are not AI")
    submit = SubmitField('Send')
