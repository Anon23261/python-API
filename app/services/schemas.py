from marshmallow import Schema, fields, validate

class ServiceSchema(Schema):
    """Schema for serializing and deserializing Service objects."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(required=True)
    price = fields.Float(required=True, validate=validate.Range(min=0))

service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)
