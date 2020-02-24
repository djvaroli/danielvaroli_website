import os
from dotenv import load_dotenv
import json

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

if 'config.json' in os.listdir(basedir):
    with open('config.json', 'r') as config_file:
        configs = json.load(config_file)
        for key, value in configs.items():
            os.environ[key] = str(value)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = 587 or int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = 1 or os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['contact@danielvaroli.com','daniel.varoli@gmail.com']
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
    RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']
    LANGUAGES = ['en']

# '5016f9caa81821e1d64f'