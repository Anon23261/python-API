from flask import Blueprint, request, jsonify

services_bp = Blueprint('services', __name__)

# Simulated data
services = [
    {"id": 1, "description": "Oil Change", "price": 50, "vehicle_id": 1},
    {"id": 2, "description": "Tire Rotation", "price": 30, "vehicle_id": 2}
]

@services_bp.route("/", methods=["GET", "POST"])
def manage_services():
    if request.method == "GET":
        return jsonify({"services": services, "message": "Services retrieved successfully"}), 200
    try:
        service = request.json
        if not service or not isinstance(service, dict):
            raise ValueError("Invalid input. Expected a JSON object.")
        services.append(service)
        return jsonify({"message": "Service added successfully", "service": service}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@services_bp.route("/<int:service_id>", methods=["GET", "PUT", "DELETE"])
def service_detail(service_id):
    if service_id >= len(services) or service_id < 0:
        return jsonify({"error": "Service not found"}), 404
    if request.method == "GET":
        return jsonify({"service": services[service_id], "message": "Service retrieved successfully"}), 200
    if request.method == "PUT":
        try:
            updated_service = request.json
            if not updated_service or not isinstance(updated_service, dict):
                raise ValueError("Invalid input. Expected a JSON object.")
            services[service_id] = updated_service
            return jsonify({"message": "Service updated successfully", "service": updated_service}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    removed_service = services.pop(service_id)
    return jsonify({"message": "Service deleted successfully", "service": removed_service}), 200