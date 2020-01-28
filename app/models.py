from flask import current_app
from flask_login import UserMixin
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Integer, index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<\nUser:\nid: {}\nemail: {}\n>'.format(self.id, self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))