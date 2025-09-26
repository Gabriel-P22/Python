from functools import wraps
from flask import request, jsonify, current_app
import jwt

def token_required(f):
    @wraps
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(' ')[1]
            except IndexError:
                return jsonify({'message': 'Invalid Token'})

        if not token:
            return jsonify({'message': 'Token not found'}), 401

        try:
            data = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithm = ['HS256']
            )
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token invalid'}), 401

        return f(data, *args, **kwargs)
    return decorated