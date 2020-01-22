import flask as f

from route.route_basic import error
from route.route_index import bp as route_index
from route.route_todo_api import bp as route_todo_api


def register_blueprint(app):
    app.register_blueprint(route_index)
    app.register_blueprint(route_todo_api)


def configured_app():
    app = f.Flask(__name__)
    register_blueprint(app)
    app.secret_key = 'asdfaax'
    app.errorhandler(404)(error)
    return app
