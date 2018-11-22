from flask import jsonify
from app.api_1_0 import api
from datetime import datetime
from app.exceptions import ValidationError


# 403
def forbidden(message):
    response = jsonify({
        'resultCode': 0,
        'resultMsg': message,
        'time': datetime.utcnow(),
        'data': []
    })
    response.status_code = 403
    return response


# 401
def unauthorized(message):
    response = jsonify({
        'resultCode': 0,
        'resultMsg': message,
        'time': datetime.utcnow(),
        'data': []
    })
    response.status_code = 401
    return response


# 400
def bad_request(message):
    response = jsonify({
        'resultCode': 0,
        'resultMsg': message,
        'time': datetime.utcnow(),
        'data': []
    })
    response.status_code = 400
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])