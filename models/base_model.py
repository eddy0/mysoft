import json
import time

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, TIMESTAMP, desc, DateTime

from utils import format, log

db = SQLAlchemy()


class SQLMixin(object):
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    # time 的时间戳是秒位单位， 其他的是毫秒为单位
    created_time = Column(DateTime, default=lambda: format())
    updated_time = Column(DateTime, default=lambda: format())

    @classmethod
    def new(cls, form):
        m = cls()
        for name, value in form.items():
            setattr(m, name, value)
        m.save()
        return m.to_json()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete(cls, id):
        m = cls.one(id=id)
        db.session.delete(m)
        db.session.commit()

    @classmethod
    def update(cls, id, **kwargs):
        m = cls.query.filter_by(id=id).first()
        for name, value in kwargs.items():
            setattr(m, name, value)
        setattr(m, 'updated_time', format())
        m.save()
        return m.to_json()

    @classmethod
    def all(cls, **kwargs):
        ms = cls.query.filter_by(**kwargs).order_by(desc('updated_time')).all()
        ms = [m.to_json() for m in ms]
        return ms

    @classmethod
    def one(cls, **kwargs):
        m = cls.query.filter_by(**kwargs).first()
        return m

    @classmethod
    def columns(cls):
        return cls.__mapper__.c.items()

    def to_json(self):
        d = {}
        for attr, column in self.columns():
            if hasattr(self, attr):
                v = getattr(self, attr)
                if attr in ['updated_time', 'created_time']:
                    v = v.strftime("%Y-%m-%d %H:%M:%S")
                d[attr] = v
        return d

    def __repr__(self):
        """
        __repr__ 是一个魔法方法
        简单来说, 它的作用是得到类的 字符串表达 形式
        比如 print(u) 实际上是 print(u.__repr__())
        不明白就看书或者 搜
        """
        name = self.__class__.__name__
        s = ''
        for attr, column in self.columns():
            if hasattr(self, attr):
                v = getattr(self, attr)
                s += '{}: ({})\n'.format(attr, v)
        return '< {}\n{} >\n'.format(name, s)
