from datetime import datetime
from flask import render_template, session, redirect, url_for

from app.main import main
from app.forms import NameForm
from app import db
from app.models import User

from app.decorators import admin_required, permission_required
from app.models import Permission
from flask_login import login_required

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        # old_name = session.get('name')
        # if old_name is not None and old_name != form.name.data:
        #     flash('Looks like you have changed you name!')
        # session['name'] = form.name.data
        return redirect(url_for('.index', name=session.get('name')))
    return render_template('index.html',
                           title="Home",
                           comments=["wanghaibo", 'zhaoxin'],
                           current_time=datetime.utcnow(),
                           form=form,
                           name=session.get('name'))

@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return 'For administrators'

@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return 'For comment moderators!'