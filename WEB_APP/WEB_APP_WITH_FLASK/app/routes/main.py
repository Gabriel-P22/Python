from flask import Blueprint, jsonify, Response

main__bp = Blueprint("main_bp", __name__)

@main__bp.route('/')
def index() -> Response:
    return jsonify({
        "message":
            "Welcome to StyleSync!"
    })

@main__bp.route('/products')
def get_products() -> Response:
    return jsonify({
        "message":
            "Welcome to StyleSync products!"
    })

@main__bp.route('/login', methods=['POST'])
def login() -> Response:
    return jsonify({
        "message":
            "Welcome to StyleSync products!"
    })