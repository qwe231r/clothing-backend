from flask import Blueprint, request, jsonify

cart_bp = Blueprint('cart', __name__)

@cart_bp.route("/", methods=["GET", "POST"])
def cart():
    return jsonify({"message": "Cart route"})
