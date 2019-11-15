""" DB 操作
    SQLlite 使用 SQL .
    Date: 2019-08-06
    Auth: haiyuan
 """

import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    # 告诉 Flask 在返回响应后进行清理的时候调用此函数。
    app.teardown_appcontext(close_db) 
    # 添加一个新的 可以与 flask 一起工作的命令。
    app.cli.add_command(init_db_command)

