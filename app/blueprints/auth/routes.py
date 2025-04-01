from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.extensions import jwt, limiter
from app.blueprints.customers.models import Customer
from . import auth_bp

@auth_bp.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    """Login endpoint for customers."""
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Email and password are required"}), 400

    email = data.get('email')
    password = data.get('password')
    
    customer = Customer.query.filter_by(email=email).first()
    if not customer or not customer.check_password(password):
        return jsonify({"error": "Invalid email or password"}), 401

    # Generate JWT token
    access_token = create_access_token(identity={"id": customer.id, "email": customer.email})
    return jsonify({
        "message": "Login successful",
        "access_token": access_token,
        "customer": {
            "id": customer.id,
            "name": customer.name,
            "email": customer.email
        }
    }), 200

@auth_bp.route('/verify', methods=['GET'])
@limiter.limit("5 per minute")
def verify_token():
    """Verify if the token is valid."""
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Missing or invalid token"}), 401
    
    try:
        token = auth_header.split(' ')[1]
        jwt.decode_token(token)  # This will raise an error if token is invalid
        return jsonify({"message": "Token is valid"}), 200
    except Exception as e:
        return jsonify({"error": "Invalid token"}), 401
