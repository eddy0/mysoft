from flask import (
    Blueprint,
    request,
    redirect,
)

from models.todo import Todo
from utils import log

main = Blueprint('route_todo_api', __name__)


@main.route('/add', methods=['POST'])
def add_todo():
    form = request.form
    t = Todo.add(form)
    log(form)
    return


@main.route('/')
def todo_all():
    todos = Todo.all()
    return todos
