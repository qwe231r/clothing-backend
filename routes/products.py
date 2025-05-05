from flask import Blueprint, jsonify

products_bp = Blueprint('products', __name__)

@products_bp.route("/", methods=["GET"])
def get_products():
    return jsonify([
        {"id": 1, "name": "Футболка", "price": 1000},
        {"id": 2, "name": "Джинсы", "price": 2500}
    ])
