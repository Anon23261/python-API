from marshmallow import Schema, fields

class MechanicSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    specialization = fields.Str(required=True)
