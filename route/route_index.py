from flask import Blueprint, render_template, request, redirect, session, jsonify, make_response

from models.user import User
from route.helper import current_user
from utils import log

main = Blueprint('route_index', __name__)


@main.route('/')
def route_index():
    return render_template('index.html')


@main.route('/login', methods=['POST'])
def route_login():
    form = request.get_json()
    u = User.validate_login(form)
    if u is None:
        return jsonify(user=None, errcode=0)
    else:
        # session 中写入 user_id
        session['user_id'] = u.id
        # 设置 cookie 有效期为 永久
        session.permanent = True
        token = u.create_token()
        r = jsonify(user=u.to_json(), token=token, errcode=0)
        return r


@main.route('/auth')
def route_auth():
    u = current_user()
    if u is None:
        return jsonify(user=None, errcode=2000, redirect_url='/login')
    else:
        # session 中写入 user_id
        session['user_id'] = u.id
        # 设置 cookie 有效期为 永久
        session.permanent = True
        token = u.create_token()
        r = jsonify(user=u.to_json(), token=token, errcode=0)
        return r


@main.route("/register", methods=['POST'])
def register():
    form = request.get_json()
    # 用类函数来判断
    u = User.register(form)
    log('regoster user', u)
    if u is None:
        return jsonify(user=u, errcode=4001)
    else:
        return jsonify(user=u, errcode=0)
