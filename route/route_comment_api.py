from flask import (
    Blueprint,
    request,
    redirect,
    jsonify
)

from models.comment import Comment
from models.todo import Todo
from utils import log

main = Blueprint('route_comment_api', __name__)


@main.route('/add', methods=['POST'])
def comment_add():
    form = request.get_json()
    log(form)
    todo = Todo.one(id=form['id'])
    if todo is not None:
        c = Comment.add(form)
        return c
