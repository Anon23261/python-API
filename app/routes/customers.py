from flask import Blueprint, request, jsonify
from app.models import Customer
from app.extensions import db, cache, limiter

customers_bp = Blueprint('customers', __name__)

@customers_bp.route("/", methods=["GET", "POST"])
@limiter.limit("10 per minute")
def manage_customers():
    if request.method == "GET":
        @cache.cached(timeout=60, key_prefix="all_customers")
        def get_all_customers():
            customers = Customer.query.all()
            return jsonify({"customers": [{"id": c.id, "name": c.name, "email": c.email} for c in customers]}), 200
        return get_all_customers()
    try:
        data = request.json
        customer = Customer(name=data['name'], email=data['email'])
        db.session.add(customer)
        db.session.commit()
        return jsonify({"message": "Customer added successfully", "customer": {"id": customer.id, "name": customer.name, "email": customer.email}}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@customers_bp.route("/<int:customer_id>", methods=["GET", "PUT", "DELETE"])
@limiter.limit("5 per minute")
def customer_detail(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    if request.method == "GET":
        return jsonify({"customer": {"id": customer.id, "name": customer.name, "email": customer.email}}), 200
    if request.method == "PUT":
        try:
            data = request.json
            customer.name = data['name']
            customer.email = data['email']
            db.session.commit()
            return jsonify({"message": "Customer updated successfully", "customer": {"id": customer.id, "name": customer.name, "email": customer.email}}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": "Customer deleted successfully"}), 200