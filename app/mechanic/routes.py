from flask import request, jsonify
from . import mechanic_bp
from .schemas import MechanicSchema

# Simulated data
mechanics = [
    {"id": 1, "name": "Alice Johnson", "specialization": "Engine Repair"},
    {"id": 2, "name": "Bob Brown", "specialization": "Tire Services"}
]

mechanic_schema = MechanicSchema()
mechanic_list_schema = MechanicSchema(many=True)

@mechanic_bp.route("/", methods=["POST"])
def create_mechanic():
    data = request.json
    mechanic = mechanic_schema.load(data)
    mechanics.append(mechanic)
    return jsonify({"message": "Mechanic added successfully", "mechanic": mechanic_schema.dump(mechanic)}), 201

@mechanic_bp.route("/", methods=["GET"])
def get_mechanics():
    return jsonify({"mechanics": mechanic_list_schema.dump(mechanics), "message": "Mechanics retrieved successfully"}), 200

@mechanic_bp.route("/<int:id>", methods=["PUT", "DELETE"])
def modify_mechanic(id):
    if id >= len(mechanics) or id < 0:
        return jsonify({"error": "Mechanic not found"}), 404
    if request.method == "PUT":
        mechanics[id] = mechanic_schema.load(request.json)
        return jsonify({"message": "Mechanic updated successfully", "mechanic": mechanic_schema.dump(mechanics[id])}), 200
    removed_mechanic = mechanics.pop(id)
    return jsonify({"message": "Mechanic deleted successfully", "mechanic": mechanic_schema.dump(removed_mechanic)}), 200
