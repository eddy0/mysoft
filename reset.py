from sqlalchemy import create_engine

import secret
from app import configured_app
from models.base_model import db
from models.todo import Todo
from utils import log


def reset_database():
    url = 'mysql+pymysql://root:{}@localhost/?charset=utf8mb4'.format(
        secret.database_password
    )
    e = create_engine(url, echo=True)

    with e.connect() as connection:
        connection.execute('DROP DATABASE IF EXISTS web19')
        connection.execute('CREATE DATABASE web19 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
        connection.execute('USE web19')

    db.metadata.create_all(bind=e)


def generate_fake_date():
    form = dict(
        todo='gua',
        note='123'
    )
    todo = Todo.add(form)
    log('todo', todo)


if __name__ == '__main__':
    app = configured_app()
    with app.app_context():
        reset_database()
        generate_fake_date()
