from sqlalchemy import Column, UnicodeText, Integer, Boolean

from models.base_model import SQLMixin, db


class Todo(SQLMixin, db.Model):
    todo = Column(UnicodeText, nullable=False)
    # user_id = Column(Integer, nullable=False)
    note = Column(UnicodeText, nullable=False, default='N/A')
    complete = Column(Boolean, nullable=False, default=False)

    @classmethod
    def add(cls, form):
        m = super().new(form)
        return m
