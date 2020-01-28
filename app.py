import flask as f
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

import secret
from models.base_model import db
from models.todo import Todo
from route.route_basic import error

from flask_cors import CORS


def register_blueprint(app):
    from route.route_index import bp as route_index
    from route.route_todo_api import main as route_todo_api
    from route.route_comment_api import main as route_comment_api

    app.register_blueprint(route_index)
    app.register_blueprint(route_todo_api, url_prefix='/todo')
    app.register_blueprint(route_comment_api, url_prefix='/comment')


def configured_app():
    app = f.Flask(__name__)
    CORS(app)

    app.secret_key = 'asdfaax'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{}@localhost/web19?charset=utf8mb4'.format(
        secret.database_password
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    register_blueprint(app)

    app.errorhandler(404)(error)

    admin = Admin(app, name='web19', template_mode='bootstrap3')
    admin.add_view(ModelView(Todo, db.session))

    return app
