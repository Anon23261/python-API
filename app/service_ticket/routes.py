from flask import request, jsonify
from . import service_ticket_bp
from .schemas import ServiceTicketSchema

# Simulated data
service_tickets = [
    {
        "id": 1,
        "VIN": "1HGCM82633A123456",
        "service_date": "2023-10-01",
        "service_description": "Brake Replacement",
        "customer_id": 1,
        "mechanic_ids": [1]
    },
    {
        "id": 2,
        "VIN": "2T1BURHE0JC123456",
        "service_date": "2023-10-02",
        "service_description": "Battery Replacement",
        "customer_id": 2,
        "mechanic_ids": [2]
    }
]

mechanics = [
    {"id": 1, "name": "Alice Johnson", "specialization": "Engine Repair"},
    {"id": 2, "name": "Bob Brown", "specialization": "Tire Services"}
]

service_ticket_schema = ServiceTicketSchema()
service_ticket_list_schema = ServiceTicketSchema(many=True)

@service_ticket_bp.route("/", methods=["POST"])
def create_service_ticket():
    data = request.json
    service_ticket = service_ticket_schema.load(data)
    mechanic_ids = data.get("mechanic_ids", [])
    service_ticket["mechanics"] = [mechanics[id] for id in mechanic_ids if id < len(mechanics)]
    service_tickets.append(service_ticket)
    return jsonify({"message": "Service ticket created successfully", "service_ticket": service_ticket_schema.dump(service_ticket)}), 201

@service_ticket_bp.route("/", methods=["GET"])
def get_service_tickets():
    return jsonify({"service_tickets": service_ticket_list_schema.dump(service_tickets), "message": "Service tickets retrieved successfully"}), 200
