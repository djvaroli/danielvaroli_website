from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from app.main import bp
from app.main.forms import ContactForm
from app.main.email import send_contact_email
import os

@bp.route('/', methods=['GET', 'POST'])
def home():
    link_names = ['About Me', 'Projects', 'Curriculum Vitae', 'Contact']
    links = [Link(link_names[i],i) for i in range(len(link_names))]
    form = ContactForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        email = Email(name, email, message)
        send_contact_email(email)
        flash('Thank you, I will get in touch with you shortly.')
        return redirect(url_for('main.home'))

    return render_template('main.html', form = form, links=links)

# @bp.route('/send_form', methods=['GET','POST'])
# def send_form():
#     formData = request.args.getlist('formData')[0]
#     print(formData.split('&&'))
#     [token,name,email,message,recaptchaCode] = formData.split('&&')[:-1]
#     email = Email(name, email, message)
#     # send_contact_email(email)
#     return url_for('main.home')

# @bp.route('/form_submit')
# def form_submit():
#     return render_template('form_submitted.html')

class Email():
    sender_name = ''
    sender_email = ''
    message = ''

    def __init__(self, sender_name, sender_email, message):
        self.sender_name = sender_name
        self.sender_email = sender_email
        self.message = message

class Link():
    def __init__(self, name, order):
        self.name = name
        self.link = name.replace(' ','_').lower()
        self.html = self.link + '.html'
        if (1 - order%2):
            self.order = 'even'
        else:
            self.order = 'odd'

        dir = os.path.join(os.getcwd(), 'app', 'templates')
        files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f))]
        if self.html not in files:
            self.create_html_file(dir)

    def create_html_file(self,dir):
        os.mknod(os.path.join(dir,self.html))
