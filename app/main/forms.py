from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import ValidationError, Email, DataRequired,DataRequired

class ContactForm(FlaskForm):
    name = StringField(render_kw={'placeholder':'My Name is'}, validators=[DataRequired()])
    email = StringField('Email', render_kw={'placeholder':"My Email is"}, validators=[DataRequired(),Email()])
    message = TextAreaField('Message', render_kw={'placeholder':'Dear Mr. Varoli,'}, validators=[DataRequired()])
    recaptcha = RecaptchaField("Just checking you are not AI")
    submit = SubmitField('Send')
