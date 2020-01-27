from sqlalchemy import Column, UnicodeText, Integer

from models.base_model import SQLMixin, db
from utils import log


class Comment(SQLMixin, db.Model):
    todo_id = Column(Integer, nullable=False)
    content = Column(UnicodeText, nullable=False, default='')

    @classmethod
    def add(cls, form):
        d = {}
        d['todo_id'] = form['id']
        freeze = ['todo_id', 'content']
        for f in form:
            if f in freeze:
                d[f] = form[f]
        m = super().new(d)
        return m
