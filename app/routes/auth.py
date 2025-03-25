from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import Customer
from app.extensions import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    customer = Customer.query.filter_by(email=email).first()
    if not customer:
        return jsonify({"error": "Invalid email"}), 401

    # Generate JWT token
    access_token = create_access_token(identity={"id": customer.id, "email": customer.email})
    return jsonify({"access_token": access_token}), 200

@auth_bp.route('/login', methods=['GET'])
def login_not_allowed():
    return jsonify({"error": "Use POST method for this endpoint"}), 405
