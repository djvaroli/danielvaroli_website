import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cc968ff9f1a1f59feb8bd83ad983ae3d3d565b74631cd7d9d2c7712d30258f86cc3c63fb'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['moreathleticyou@gmail.com','daniel.varoli@gmail.com']
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    RECAPTCHA_PUBLIC_KEY = '6LdR0M8UAAAAABbKlXVR-hqAfkMm7W3ymdP5rjd3'
    RECAPTCHA_PRIVATE_KEY = '6LdR0M8UAAAAALK18OH1zzOyAecqN3zro4RpZn57'
    LANGUAGES = ['en']