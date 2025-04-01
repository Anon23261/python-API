from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db, cache, limiter
from . import customers_bp
from .models import Customer
from marshmallow import Schema, fields

class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    vehicles = fields.Nested('VehicleSchema', many=True, dump_only=True)
    service_tickets = fields.Nested('ServiceTicketSchema', many=True, dump_only=True)

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

@customers_bp.route("/", methods=["GET"])
@jwt_required()
@limiter.limit("10 per minute")
@cache.cached(timeout=60, key_prefix="all_customers")
def get_customers():
    """Get all customers."""
    customers = Customer.query.all()
    return jsonify({"customers": customers_schema.dump(customers)}), 200

@customers_bp.route("/", methods=["POST"])
@limiter.limit("10 per minute")
def create_customer():
    """Create a new customer."""
    try:
        data = customer_schema.load(request.json)
        customer = Customer(
            name=data['name'],
            email=data['email']
        )
        customer.set_password(data['password'])
        db.session.add(customer)
        db.session.commit()
        
        cache.delete('all_customers')
        return jsonify({
            "message": "Customer created successfully",
            "customer": customer_schema.dump(customer)
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@customers_bp.route("/<int:customer_id>", methods=["GET"])
@jwt_required()
@limiter.limit("5 per minute")
@cache.memoize(60)
def get_customer(customer_id):
    """Get a specific customer."""
    customer = Customer.query.get_or_404(customer_id)
    return jsonify({"customer": customer_schema.dump(customer)}), 200

@customers_bp.route("/<int:customer_id>", methods=["PUT"])
@jwt_required()
@limiter.limit("5 per minute")
def update_customer(customer_id):
    """Update a customer."""
    customer = Customer.query.get_or_404(customer_id)
    try:
        data = customer_schema.load(request.json, partial=True)
        if 'name' in data:
            customer.name = data['name']
        if 'email' in data:
            customer.email = data['email']
        if 'password' in data:
            customer.set_password(data['password'])
            
        db.session.commit()
        cache.delete('all_customers')
        cache.delete_memoized(get_customer, customer_id)
        
        return jsonify({
            "message": "Customer updated successfully",
            "customer": customer_schema.dump(customer)
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@customers_bp.route("/<int:customer_id>", methods=["DELETE"])
@jwt_required()
@limiter.limit("5 per minute")
def delete_customer(customer_id):
    """Delete a customer."""
    customer = Customer.query.get_or_404(customer_id)
    try:
        db.session.delete(customer)
        db.session.commit()
        
        cache.delete('all_customers')
        cache.delete_memoized(get_customer, customer_id)
        
        return jsonify({
            "message": "Customer deleted successfully"
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
