from flask import request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError

from app.extensions import db, cache, limiter
from app.vehicles import vehicles_bp
from app.vehicles.models import Vehicle
from app.vehicles.schemas import vehicle_schema, vehicles_schema
from app.customers.models import Customer

@vehicles_bp.route("/", methods=["GET"])
@jwt_required()
@limiter.limit("10 per minute")
@cache.cached(timeout=60, key_prefix="all_vehicles")
def get_vehicles():
    """Get all vehicles."""
    vehicles = Vehicle.query.all()
    return jsonify({"vehicles": vehicles_schema.dump(vehicles)}), 200

@vehicles_bp.route("/", methods=["POST"])
@jwt_required()
@limiter.limit("10 per minute")
def create_vehicle():
    """Create a new vehicle."""
    try:
        data = vehicle_schema.load(request.json)
        # Verify owner exists
        owner = Customer.query.get_or_404(data['owner_id'])
        vehicle = Vehicle(**data)
        db.session.add(vehicle)
        db.session.commit()
        cache.delete("all_vehicles")
        return jsonify({
            "message": "Vehicle created successfully",
            "vehicle": vehicle_schema.dump(vehicle)
        }), 201
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@vehicles_bp.route("/<int:vehicle_id>", methods=["GET"])
@jwt_required()
@limiter.limit("5 per minute")
@cache.memoize(60)
def get_vehicle(vehicle_id):
    """Get a specific vehicle by ID."""
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    return jsonify({"vehicle": vehicle_schema.dump(vehicle)}), 200

@vehicles_bp.route("/<int:vehicle_id>", methods=["PUT"])
@jwt_required()
@limiter.limit("5 per minute")
def update_vehicle(vehicle_id):
    """Update a specific vehicle."""
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    try:
        data = vehicle_schema.load(request.json, partial=True)
        if 'owner_id' in data:
            # Verify new owner exists
            Customer.query.get_or_404(data['owner_id'])
        for key, value in data.items():
            setattr(vehicle, key, value)
        db.session.commit()
        cache.delete_memoized(get_vehicle, vehicle_id)
        cache.delete("all_vehicles")
        return jsonify({
            "message": "Vehicle updated successfully",
            "vehicle": vehicle_schema.dump(vehicle)
        }), 200
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@vehicles_bp.route("/<int:vehicle_id>", methods=["DELETE"])
@jwt_required()
@limiter.limit("5 per minute")
def delete_vehicle(vehicle_id):
    """Delete a specific vehicle."""
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    try:
        db.session.delete(vehicle)
        db.session.commit()
        cache.delete_memoized(get_vehicle, vehicle_id)
        cache.delete("all_vehicles")
        return jsonify({"message": "Vehicle deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400