from flask import render_template, current_app
from app.email import send_email


def send_contact_email(Email):
    send_email('[DanielVaroli.com] Contact',
               sender=current_app.config['ADMINS'][0],
               recipients=[current_app.config['ADMINS'][1]],
               text_body=render_template('email/contact.txt', email=Email),
               html_body=render_template('email/contact.html',email=Email))

