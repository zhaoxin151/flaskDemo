# from app import db, create_app
# from app.models import User, Role
#
# app = create_app('default')
# app_context = app.app_context()
# app_context.push()
#
# user = User.query.filter_by(username= "wanghaibo1").update({'role_id': 1})
# db.session.commit()

# Role.insert_roles()
# Role.query.all()

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/user/login', methods=['POST', 'GET'])
def login():

    postForm = request.form

    getArgs = request.args

    postValue = request.values

    email = request.form.get('email')
    password = request.form.get('password')

    email1 = request.values.get('email')
    password1 = request.values.get('password')

    return jsonify({
        'email': email,
        'password': password
    })

if __name__ == '__main__':
    app.run(debug=False)

