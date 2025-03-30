from flask import request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError

from app.extensions import db, cache, limiter
from app.services import services_bp
from app.services.models import Service
from app.services.schemas import service_schema, services_schema

@services_bp.route("/", methods=["GET"])
@jwt_required()
@limiter.limit("10 per minute")
@cache.cached(timeout=60, key_prefix="all_services")
def get_services():
    """Get all services."""
    services = Service.query.all()
    return jsonify({"services": services_schema.dump(services)}), 200

@services_bp.route("/", methods=["POST"])
@jwt_required()
@limiter.limit("10 per minute")
def create_service():
    """Create a new service."""
    try:
        data = service_schema.load(request.json)
        service = Service(**data)
        db.session.add(service)
        db.session.commit()
        cache.delete("all_services")
        return jsonify({
            "message": "Service created successfully",
            "service": service_schema.dump(service)
        }), 201
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@services_bp.route("/<int:service_id>", methods=["GET"])
@jwt_required()
@limiter.limit("5 per minute")
@cache.memoize(60)
def get_service(service_id):
    """Get a specific service by ID."""
    service = Service.query.get_or_404(service_id)
    return jsonify({"service": service_schema.dump(service)}), 200

@services_bp.route("/<int:service_id>", methods=["PUT"])
@jwt_required()
@limiter.limit("5 per minute")
def update_service(service_id):
    """Update a specific service."""
    service = Service.query.get_or_404(service_id)
    try:
        data = service_schema.load(request.json, partial=True)
        for key, value in data.items():
            setattr(service, key, value)
        db.session.commit()
        cache.delete_memoized(get_service, service_id)
        cache.delete("all_services")
        return jsonify({
            "message": "Service updated successfully",
            "service": service_schema.dump(service)
        }), 200
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@services_bp.route("/<int:service_id>", methods=["DELETE"])
@jwt_required()
@limiter.limit("5 per minute")
def delete_service(service_id):
    """Delete a specific service."""
    service = Service.query.get_or_404(service_id)
    try:
        db.session.delete(service)
        db.session.commit()
        cache.delete_memoized(get_service, service_id)
        cache.delete("all_services")
        return jsonify({"message": "Service deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400