import flask as f


bp = f.Blueprint('route_index', __name__)


@bp.route('/')
def route_index():
    return f.render_template('index.html')

