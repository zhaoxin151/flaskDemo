from flask import jsonify, request, current_app, url_for
from app.api_1_0 import api
from app.models import User, Post
import json


@api.route('/user/login', methods=['POST'])
def user_login():
    email = request.form.get('email')
    password = request.form.get('password')
    print(email)
    print(password)

    if email == '' or password == '':
        return jsonify({
            "message": 'username or password is empty'
        })

    user = User.query.filter_by(email=email).first()
    if user is None:
        return jsonify({
            "message": 'user not exist'
        })
    if user.verify_password(password):
        return jsonify({
            'data': user.to_json()
        })
    else:
        return jsonify({
            "message": 'username and password not correct'
        })


@api.route('/users', methods=['POST'])
def get_user():

    token = request.form.get('access_token')
    print(token)
    user = User.verify_auth_token(token)
    if user is not None:
        return jsonify(user.to_json())
    else:
        return jsonify({
            'message': 'token 验证失败'
        })


@api.route('/users/posts', methods=['POST'])
def get_user_posts():

    token = request.form.get('access_token')
    print(token)
    user = User.verify_auth_token(token)

    if user is None:
        return jsonify({
            'message': 'token 验证失败'
        })

    page = request.args.get('page', 1, type=int)
    pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=10,
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_posts', id=id, page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_posts', id=id, page=page+1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@api.route('/users/<int:id>/timeline/')
def get_user_followed_posts(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = user.followed_posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_followed_posts', id=id, page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_followed_posts', id=id, page=page+1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })
