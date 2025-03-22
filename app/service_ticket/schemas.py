from marshmallow import Schema, fields

class ServiceTicketSchema(Schema):
    id = fields.Int()
    VIN = fields.Str(required=True)
    service_date = fields.Date(required=True)
    service_description = fields.Str(required=True)
    customer_id = fields.Int(required=True)
    mechanic_ids = fields.List(fields.Int(), required=True)

    class Meta:
        fields = ('VIN', 'service_date', 'service_description', 'customer_id', 'mechanic_ids')
