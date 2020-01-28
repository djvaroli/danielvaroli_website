import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cc968ff9f1a1f59feb8bd83ad983ae3d3d565b74631cd7d9d2c7712d30258f86cc3c63fb'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com' or os.environ.get('MAIL_SERVER')
    MAIL_PORT = 587 or int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = 1 or os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = 'moreathleticyou' or os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'Uranium 238' or os.environ.get('MAIL_PASSWORD')
    ADMINS = ['moreathleticyou@gmail.com','daniel.varoli@gmail.com']
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    RECAPTCHA_PUBLIC_KEY = '6Le_mNMUAAAAAEddyecx8fYaDdcsPY8rSuYHGMiy'
    RECAPTCHA_PRIVATE_KEY = '6Le_mNMUAAAAAKeuPH-9DQnO0Gk6SUSgiP8o9rtH'
    LANGUAGES = ['en']