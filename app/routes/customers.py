from flask import Blueprint, request, jsonify

customers_bp = Blueprint('customers', __name__)

# Simulated data
customers = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com"}
]

@customers_bp.route("/", methods=["GET", "POST"])
def manage_customers():
    if request.method == "GET":
        return jsonify({"customers": customers, "message": "Customers retrieved successfully"}), 200
    try:
        customer = request.json
        if not customer or not isinstance(customer, dict):
            raise ValueError("Invalid input. Expected a JSON object.")
        customers.append(customer)
        return jsonify({"message": "Customer added successfully", "customer": customer}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@customers_bp.route("/<int:customer_id>", methods=["GET", "PUT", "DELETE"])
def customer_detail(customer_id):
    if customer_id >= len(customers) or customer_id < 0:
        return jsonify({"error": "Customer not found"}), 404
    if request.method == "GET":
        return jsonify({"customer": customers[customer_id], "message": "Customer retrieved successfully"}), 200
    if request.method == "PUT":
        try:
            updated_customer = request.json
            if not updated_customer or not isinstance(updated_customer, dict):
                raise ValueError("Invalid input. Expected a JSON object.")
            customers[customer_id] = updated_customer
            return jsonify({"message": "Customer updated successfully", "customer": updated_customer}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    removed_customer = customers.pop(customer_id)
    return jsonify({"message": "Customer deleted successfully", "customer": removed_customer}), 200