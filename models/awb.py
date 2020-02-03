from sqlalchemy import Column, UnicodeText, Boolean, Integer
from models.base_model import SQLMixin, db


class AWB(SQLMixin, db.Model):
    awb = Column(UnicodeText, nullable=False)
    user_id = Column(Integer, nullable=False)
    note = Column(UnicodeText, nullable=False, default='N/A')
    complete = Column(Boolean, nullable=False, default=False)

    @classmethod
    def add(cls, form):
        d = {}
        freeze = ['note', 'awb']
        for f in form:
            if f in freeze:
                d[f] = form[f]
        m = super().new(d)
        return m

    @classmethod
    def toggle(cls, id):
        m = super().one(id=id)
        complete = not m.__dict__['complete']
        m = super().update(id, complete=complete)
        return m

