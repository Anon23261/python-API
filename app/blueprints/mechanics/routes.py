from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db, cache, limiter
from . import mechanics_bp
from .models import Mechanic
from marshmallow import Schema, fields

class MechanicSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    specialization = fields.Str()

mechanic_schema = MechanicSchema()
mechanics_schema = MechanicSchema(many=True)

@mechanics_bp.route("/", methods=["GET"])
@jwt_required()
@limiter.limit("10 per minute")
@cache.cached(timeout=60, key_prefix="all_mechanics")
def get_mechanics():
    """Get all mechanics."""
    mechanics = Mechanic.query.all()
    return jsonify({"mechanics": mechanics_schema.dump(mechanics)}), 200

@mechanics_bp.route("/", methods=["POST"])
@jwt_required()
@limiter.limit("10 per minute")
def create_mechanic():
    """Create a new mechanic."""
    try:
        data = mechanic_schema.load(request.json)
        mechanic = Mechanic(**data)
        db.session.add(mechanic)
        db.session.commit()
        
        cache.delete('all_mechanics')
        return jsonify({
            "message": "Mechanic created successfully",
            "mechanic": mechanic_schema.dump(mechanic)
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@mechanics_bp.route("/<int:mechanic_id>", methods=["GET"])
@jwt_required()
@limiter.limit("5 per minute")
@cache.memoize(60)
def get_mechanic(mechanic_id):
    """Get a specific mechanic."""
    mechanic = Mechanic.query.get_or_404(mechanic_id)
    return jsonify({"mechanic": mechanic_schema.dump(mechanic)}), 200

@mechanics_bp.route("/<int:mechanic_id>", methods=["PUT"])
@jwt_required()
@limiter.limit("5 per minute")
def update_mechanic(mechanic_id):
    """Update a mechanic."""
    mechanic = Mechanic.query.get_or_404(mechanic_id)
    try:
        data = mechanic_schema.load(request.json, partial=True)
        for key, value in data.items():
            setattr(mechanic, key, value)
            
        db.session.commit()
        cache.delete('all_mechanics')
        cache.delete_memoized(get_mechanic, mechanic_id)
        
        return jsonify({
            "message": "Mechanic updated successfully",
            "mechanic": mechanic_schema.dump(mechanic)
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@mechanics_bp.route("/<int:mechanic_id>", methods=["DELETE"])
@jwt_required()
@limiter.limit("5 per minute")
def delete_mechanic(mechanic_id):
    """Delete a mechanic."""
    mechanic = Mechanic.query.get_or_404(mechanic_id)
    try:
        db.session.delete(mechanic)
        db.session.commit()
        
        cache.delete('all_mechanics')
        cache.delete_memoized(get_mechanic, mechanic_id)
        
        return jsonify({
            "message": "Mechanic deleted successfully"
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
