from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.customers.models import Customer
from app.extensions import db
from app.auth import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return jsonify({"message": "Login endpoint"}), 200

    if request.method == 'POST':
        data = request.json
        if not data or 'email' not in data:
            return jsonify({"error": "Email is required"}), 400

        email = data.get('email')
        customer = Customer.query.filter_by(email=email).first()
        if not customer:
            return jsonify({"error": "Invalid email"}), 401

        # Generate JWT token
        access_token = create_access_token(identity={"id": customer.id, "email": customer.email})
        return jsonify({"access_token": access_token}), 200
