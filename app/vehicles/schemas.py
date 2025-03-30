from marshmallow import Schema, fields, validate

class VehicleSchema(Schema):
    """Schema for serializing and deserializing Vehicle objects."""
    id = fields.Int(dump_only=True)
    make = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    model = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    year = fields.Int(required=True, validate=validate.Range(min=1900))
    owner_id = fields.Int(required=True)

vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)
