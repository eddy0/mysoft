import hashlib

from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from sqlalchemy import Column, String, Text

import secret
from models.base_model import SQLMixin, db
from utils import log


class User(SQLMixin, db.Model):
    __tablename__ = 'User'
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    image = Column(String(100), nullable=False, default='/images/3.jpg')
    email = Column(String(50))
    nickname = Column(String(50))
    phone_number = Column(String(50))

    @staticmethod
    def salted_password(password, salt='$!@><?>HUI&DWQa`'):
        salted = hashlib.sha256((password + salt).encode('ascii')).hexdigest()
        return salted

    @classmethod
    def register(cls, form):
        name = form.get('username', '')
        f = {}
        freeze = ['username', 'password', 'email', 'image', 'nickname', 'phone_number']
        for i in form:
            if i in freeze:
                f[i] = form[i]
        log('register', form)
        if len(name) > 2 and User.one(username=name) is None:
            # form['password'] = User.salted_password(form['password'])
            u = User.new(f)
            return u
        else:
            return None

    @classmethod
    def validate_login(cls, form):
        query = dict(
            username=form['username'],
            # password=User.salted_password(form['password']),
            password=form['password'],
        )
        log('validate_login', form, query)
        return User.one(**query)

    def create_token(self, expiration=60000):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id}).decode()

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user
