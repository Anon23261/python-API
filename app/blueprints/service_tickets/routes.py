from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db, cache, limiter
from . import service_tickets_bp
from .models import ServiceTicket
from .schemas import ServiceTicketSchema

service_ticket_schema = ServiceTicketSchema()
service_tickets_schema = ServiceTicketSchema(many=True)

@service_tickets_bp.route("/", methods=["POST"])
@jwt_required()
@limiter.limit("10 per minute")
def create_service_ticket():
    """Create a new service ticket."""
    try:
        data = service_ticket_schema.load(request.json)
        service_ticket = ServiceTicket(**data)
        db.session.add(service_ticket)
        db.session.commit()
        
        cache.delete('all_service_tickets')  # Invalidate cache
        return jsonify({
            "message": "Service ticket created successfully",
            "service_ticket": service_ticket_schema.dump(service_ticket)
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@service_tickets_bp.route("/", methods=["GET"])
@jwt_required()
@limiter.limit("10 per minute")
@cache.cached(timeout=60, key_prefix="all_service_tickets")
def get_service_tickets():
    """Get all service tickets."""
    service_tickets = ServiceTicket.query.all()
    return jsonify({
        "service_tickets": service_tickets_schema.dump(service_tickets),
        "message": "Service tickets retrieved successfully"
    }), 200

@service_tickets_bp.route("/<int:ticket_id>", methods=["GET"])
@jwt_required()
@limiter.limit("5 per minute")
@cache.memoize(60)
def get_service_ticket(ticket_id):
    """Get a specific service ticket."""
    service_ticket = ServiceTicket.query.get_or_404(ticket_id)
    return jsonify({
        "service_ticket": service_ticket_schema.dump(service_ticket),
        "message": "Service ticket retrieved successfully"
    }), 200

@service_tickets_bp.route("/<int:ticket_id>", methods=["PUT"])
@jwt_required()
@limiter.limit("5 per minute")
def update_service_ticket(ticket_id):
    """Update a service ticket."""
    service_ticket = ServiceTicket.query.get_or_404(ticket_id)
    try:
        data = service_ticket_schema.load(request.json, partial=True)
        for key, value in data.items():
            setattr(service_ticket, key, value)
        
        db.session.commit()
        cache.delete('all_service_tickets')
        cache.delete_memoized(get_service_ticket, ticket_id)
        
        return jsonify({
            "message": "Service ticket updated successfully",
            "service_ticket": service_ticket_schema.dump(service_ticket)
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@service_tickets_bp.route("/<int:ticket_id>", methods=["DELETE"])
@jwt_required()
@limiter.limit("5 per minute")
def delete_service_ticket(ticket_id):
    """Delete a service ticket."""
    service_ticket = ServiceTicket.query.get_or_404(ticket_id)
    try:
        db.session.delete(service_ticket)
        db.session.commit()
        
        cache.delete('all_service_tickets')
        cache.delete_memoized(get_service_ticket, ticket_id)
        
        return jsonify({
            "message": "Service ticket deleted successfully"
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
