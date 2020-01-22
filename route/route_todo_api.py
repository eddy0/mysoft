import flask as f

from utils import log

bp = f.Blueprint('route_todo_api', __name__)


@bp.route('/todo/add', methods=['POST'])
def add_todo():
    form = f.request.form
    log(form)
