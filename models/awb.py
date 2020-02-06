from sqlalchemy import Column, UnicodeText, Boolean, Integer
from models.base_model import SQLMixin, db
from route.helper import current_user


class AWB(SQLMixin, db.Model):
    awb = Column(UnicodeText, nullable=False)
    user_id = Column(Integer, nullable=False)
    note = Column(UnicodeText, nullable=False, default='N/A')
    complete = Column(Boolean, nullable=False, default=False)

    @classmethod
    def all(cls, **kwargs):
        u = current_user()
        data = super().all(user_id=u.id, **kwargs)
        return data

    @classmethod
    def add(cls, form):
        d = {}
        freeze = ['note', 'awb']
        for f in form:
            if f in freeze:
                d[f] = form[f]
        u = current_user()
        d['user_id'] = u.id
        m = super().new(d)
        return m

    @classmethod
    def toggle(cls, id):
        m = super().one(id=id)
        complete = not m.__dict__['complete']
        m = super().update(id, complete=complete)
        return m

