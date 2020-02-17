import json

from flask import (
    Blueprint,
    request,
    redirect,
    jsonify)

from models.todo import Todo
from route.helper import login_required
from utils import log

main = Blueprint('route_todo_api', __name__)


@main.route('/add', methods=['POST'])
@login_required
def add_todo():
    data = request.get_json()
    t = Todo.add(data)
    log('data', t)
    return jsonify(data=t, errcode=0)


@main.route('/<id>', methods=['PUT'])
@login_required
def toggle_todo(id):
    t = Todo.toggle(id)
    return jsonify(data=t, errcode=0)


@main.route('/<id>', methods=['PATCH'])
@login_required
def update_todo(id):
    form = request.get_json()
    t = Todo.update(id, **form)
    return jsonify(data=t, errcode=0)


@main.route('/<id>', methods=['DELETE'])
@login_required
def delete_todo(id):
    t = Todo.delete(id)
    return jsonify(data=t, errcode=0)


@main.route('/')
@login_required
def todo_index():
    log('all')
    todos = Todo.all()
    return jsonify(data=todos, errcode=0)


@main.route('/all')
def todo_all():
    return redirect('/')


@main.route('/complete')
@login_required
def todo_complete():
    todos = Todo.all(complete=True)
    return jsonify(data=todos, errcode=0)


@main.route('/uncomplete')
@login_required
def todo_uncomplete():
    todos = Todo.all(complete=False)
    return jsonify(todos, errcode=0)
