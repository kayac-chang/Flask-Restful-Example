"""Product view"""
from flask import Blueprint, jsonify

blueprint = Blueprint('product', __name__)

@blueprint.route("/products", methods=['GET'])
def get_products():
    return jsonify({ 'test': 'hello' })
