import json

from sqlalchemy import Column, UnicodeText, Boolean, Integer

from models.base_model import SQLMixin, db
from models.comment import Comment
from route.helper import current_user
from utils import log


class Todo(SQLMixin, db.Model):
    todo = Column(UnicodeText, nullable=False)
    user_id = Column(Integer, nullable=False)
    note = Column(UnicodeText, nullable=False, default='N/A')
    complete = Column(Boolean, nullable=False, default=False)

    @classmethod
    def all(cls, **kwargs):
        u = current_user()
        data = super().all(user_id=u.id, **kwargs)
        for d in data:
            comments = Comment.all(todo_id=d['id'])
            d['comments'] = comments
        return data

    @classmethod
    def add(cls, form):
        d = {}
        freeze = ['note', 'todo']
        for f in form:
            if f in freeze:
                d[f] = form[f]
        u = current_user()
        d['user_id'] = u.id
        m = super().new(d)
        log('m', m)
        return m

    @classmethod
    def toggle(cls, id):
        m = super().one(id=id)
        complete = not m.__dict__['complete']
        m = super().update(id, complete=complete)
        return m

