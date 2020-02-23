import functools
import uuid
from functools import wraps

from flask import session, request, abort, redirect, url_for, jsonify

from models.user import User
from utils import log


def render_json(data, **kwargs):
    return jsonify(data=data, errcode=0, **kwargs)


def login_required(route_function):
    @functools.wraps(route_function)
    def f(*args, **kwargs):
        log('login_required', session)
        u = current_user()
        log('u', u)
        if u is None:
            log('guest login')
            return jsonify(user=None, redirect_url='/login', errcode=2000)
        else:
            log('user login', route_function)
            return route_function(*args, **kwargs)
    return f


# def current_user():
#     uid = session.get('user_id', '')
#     u: User = User.one(id=uid)
#     return u


def current_user():
    log('current user function')
    try:
        token = request.headers["z-token"]
        log('token', token)
    except Exception:
        return None
    u = User.verify_auth_token(token)
    log('current user,', u)
    return u


csrf_tokens = dict()


def csrf_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args['token']

        u = current_user()
        if token in csrf_tokens and csrf_tokens[token] == u.id:
            csrf_tokens.pop(token)
            return f(*args, **kwargs)
        else:
            abort(401)

    return wrapper


def new_csrf_token():
    u = current_user()
    token = str(uuid.uuid4())
    csrf_tokens[token] = u.id
    return token
