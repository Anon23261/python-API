from flask import request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError

from app.extensions import db, cache, limiter
from app.customers import customers_bp
from app.customers.models import Customer
from app.customers.schemas import customer_schema, customers_schema

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
        if 'password' not in request.json:
            return jsonify({"error": "Password is required"}), 400
            
        customer = Customer(**data)
        customer.set_password(request.json['password'])
        db.session.add(customer)
        db.session.commit()
        return jsonify({
            "message": "Customer created successfully",
            "customer": customer_schema.dump(customer)
        }), 201
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@customers_bp.route("/<int:customer_id>", methods=["GET"])
@jwt_required()
@limiter.limit("5 per minute")
@cache.memoize(60)
def get_customer(customer_id):
    """Get a specific customer by ID."""
    customer = Customer.query.get_or_404(customer_id)
    return jsonify({"customer": customer_schema.dump(customer)}), 200

@customers_bp.route("/<int:customer_id>", methods=["PUT"])
@jwt_required()
@limiter.limit("5 per minute")
def update_customer(customer_id):
    """Update a specific customer."""
    customer = Customer.query.get_or_404(customer_id)
    try:
        data = customer_schema.load(request.json, partial=True)
        for key, value in data.items():
            setattr(customer, key, value)
        db.session.commit()
        cache.delete_memoized(get_customer, customer_id)
        cache.delete("all_customers")
        return jsonify({
            "message": "Customer updated successfully",
            "customer": customer_schema.dump(customer)
        }), 200
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@customers_bp.route("/<int:customer_id>", methods=["DELETE"])
@jwt_required()
@limiter.limit("5 per minute")
def delete_customer(customer_id):
    """Delete a specific customer."""
    customer = Customer.query.get_or_404(customer_id)
    try:
        db.session.delete(customer)
        db.session.commit()
        cache.delete_memoized(get_customer, customer_id)
        cache.delete("all_customers")
        return jsonify({"message": "Customer deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
