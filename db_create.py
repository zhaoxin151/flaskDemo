from app import db, create_app
from app.models import User, Role

app = create_app('default')
app_context = app.app_context()
app_context.push()

user = User.query.filter_by(username= "wanghaibo1").update({'role_id': 1})
db.session.commit()

# Role.insert_roles()
# Role.query.all()

