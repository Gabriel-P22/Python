from flask import Blueprint, jsonify, Response, request
from pydantic import ValidationError
from WEB_APP.WEB_APP_WITH_FLASK.app import db
from bson import ObjectId
from WEB_APP.WEB_APP_WITH_FLASK.app.models.user import LoginPayload
from WEB_APP.WEB_APP_WITH_FLASK.app.models.products import Product, ProductDBModel

main__bp = Blueprint("main_bp", __name__)

@main__bp.route('/login', methods=['POST'])
def login():

    try:
        payload = request.get_json()
        user_data = LoginPayload(**payload)
        pass
    except ValidationError as e:
        return jsonify({
            "error":
                e.errors()
        }), 400
    except Exception as e:
        return jsonify({
            "error":
                "error in login"
        }), 500

    if user_data.username == "admin" and user_data.password == "123":
        return jsonify({
            "message": f"Realizar o Login do adm {user_data.model_dump_json()}"
        })
    else:
        return jsonify({
            "message": f"Realizar o Login{user_data.model_dump_json()}"
        })

@main__bp.route('/products', methods=["POST"])
def create_products() -> Response:
    return jsonify({
        "message":
            "Create a product!"
    })

@main__bp.route('/product/<int:product_id>')
def get_product_by_id(product_id) -> Response:
    return jsonify({
        "message":
            "Product find!"
    })


@main__bp.route('/products')
def get_products() -> Response:
    products_cursor = db.products.find({})
    products_list = []

    for products in products_cursor:
        products['_id'] = str(products['_id'])
        products_list.append(products)

    return jsonify({
        "list":
            products_list
    })

@main__bp.route('/product/<int:product_id>', methods=["PUT"])
def update_product_by_id(product_id) -> Response:
    return jsonify({
        "message":
            "Product find!"
    })

@main__bp.route('/product/<int:product_id>', methods=["DELETE"])
def update_product_by_id(product_id) -> Response:
    return jsonify({
        "message":
            "Product find!"
    })

@main__bp.route('/sales/upload', methods=["POST"])
def upload_sales() -> Response:
    return jsonify({
        "message":
            "Product find!"
    })

@main__bp.route('/')
def index() -> Response:
    return jsonify({
        "message":
            "Welcome to StyleSync!"
    })

