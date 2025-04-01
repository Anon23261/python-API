from flask import jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.blueprints.auth import bp
from app.blueprints.customers.models import Customer
from app.extensions import db

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    customer = Customer.query.filter_by(email=email).first()
    if not customer or not check_password_hash(customer.password_hash, password):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=customer.id)
    return jsonify({"access_token": access_token}), 200

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    required_fields = ['name', 'email', 'password', 'phone', 'address']
    
    # Check if all required fields are present
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Missing required fields. Required: {', '.join(required_fields)}"}), 400
    
    # Check if user already exists
    if Customer.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400
    
    # Create new customer
    customer = Customer(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        address=data['address'],
        preferred_contact_method=data.get('preferred_contact_method', 'email'),
        notes=data.get('notes', '')
    )
    customer.set_password(data['password'])
    
    try:
        db.session.add(customer)
        db.session.commit()
        return jsonify({"message": "Registration successful"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Registration failed", "details": str(e)}), 500
