import pymysql
import time
# from pwd import sql as sql_pwd
# from pwd import db as sql_db


def log(*args, **kwargs):
    time_format = '%Y%m%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    formatted = time.strftime(time_format, value)
    print(formatted, *args, **kwargs)


def connection():
    c = pymysql.connect(
        host='localhost',
        user='root',
        password=sql_pwd,
        db=sql_db,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
    )
    return c


def connection_without_db():
    c = pymysql.connect(
        host='localhost',
        user='root',
        password=sql_pwd,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
    )
    return c