from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import cache, limiter

vehicles_bp = Blueprint('vehicles', __name__)

# Simulated data
vehicles = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2020, "owner_id": 1},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2019, "owner_id": 2}
]

@vehicles_bp.route("/", methods=["GET", "POST"])
@jwt_required()
@limiter.limit("10 per minute")
def manage_vehicles():
    if request.method == "GET":
        @cache.cached(timeout=60, key_prefix="all_vehicles")
        def get_all_vehicles():
            return jsonify({"vehicles": vehicles, "message": "Vehicles retrieved successfully"}), 200
        return get_all_vehicles()
    try:
        vehicle = request.json
        if not vehicle or not isinstance(vehicle, dict):
            raise ValueError("Invalid input. Expected a JSON object.")
        vehicles.append(vehicle)
        return jsonify({"message": "Vehicle added successfully", "vehicle": vehicle}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@vehicles_bp.route("/<int:vehicle_id>", methods=["GET", "PUT", "DELETE"])
@jwt_required()
@limiter.limit("5 per minute")
def vehicle_detail(vehicle_id):
    vehicle = next((v for v in vehicles if v["id"] == vehicle_id), None)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404
    if request.method == "GET":
        return jsonify({"vehicle": vehicle, "message": "Vehicle retrieved successfully"}), 200
    if request.method == "PUT":
        try:
            updated_vehicle = request.json
            if not updated_vehicle or not isinstance(updated_vehicle, dict):
                raise ValueError("Invalid input. Expected a JSON object.")
            vehicle.update(updated_vehicle)
            return jsonify({"message": "Vehicle updated successfully", "vehicle": vehicle}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    vehicles.remove(vehicle)
    return jsonify({"message": "Vehicle deleted successfully", "vehicle": vehicle}), 200