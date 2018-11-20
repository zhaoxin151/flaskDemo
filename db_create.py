from app import db, create_app
from app.models import User

app = create_app('default')
app_context = app.app_context()
app_context.push()

user = User.query.filter_by(username='wanghaibo123')
user.update({'confirmed': True})
db.session.commit()



