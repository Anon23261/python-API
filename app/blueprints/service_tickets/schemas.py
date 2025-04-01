from marshmallow import Schema, fields

class ServiceTicketSchema(Schema):
    id = fields.Int(dump_only=True)
    description = fields.Str(required=True)
    status = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    customer_id = fields.Int(required=True)
    vehicle_id = fields.Int(required=True)
    mechanic_id = fields.Int()
    service_id = fields.Int(required=True)
    
    # Nested relationships
    vehicle = fields.Nested('VehicleSchema', dump_only=True)
    mechanic = fields.Nested('MechanicSchema', dump_only=True)
    service = fields.Nested('ServiceSchema', dump_only=True)
