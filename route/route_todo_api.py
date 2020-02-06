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
    return jsonify(t)


@main.route('/<id>', methods=['PUT'])
def toggle_todo(id):
    t = Todo.toggle(id)
    return jsonify(t)


@main.route('/<id>', methods=['PATCH'])
def update_todo(id):
    form = request.get_json()
    t = Todo.update(id, **form)
    return jsonify(t)


@main.route('/<id>', methods=['DELETE'])
def delete_todo(id):
    t = Todo.delete(id)
    return jsonify(t)


@main.route('/')
@login_required
def todo_index():
    log('all')
    todos = Todo.all()
    return jsonify(todos)


@main.route('/all')
def todo_all():
    return redirect('/')


@main.route('/complete')
def todo_complete():
    todos = Todo.all(complete=True)
    return jsonify(todos)


@main.route('/uncomplete')
def todo_uncomplete():
    todos = Todo.all(complete=False)
    return jsonify(todos)
