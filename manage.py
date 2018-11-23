#!/usr/bin/python
# --coding:utf-8--

import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from flask_login import login_required


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command('Shell', Shell(make_context=make_shell_context()))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()