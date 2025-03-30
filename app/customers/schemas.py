from marshmallow import Schema, fields, validate

class CustomerSchema(Schema):
    """Schema for serializing and deserializing Customer objects."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
