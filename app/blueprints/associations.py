from app.extensions import db

# Mechanic-Specialization association
mechanic_specializations = db.Table('mechanic_specializations',
    db.Column('mechanic_id', db.Integer, db.ForeignKey('mechanic.id'), primary_key=True),
    db.Column('specialization_id', db.Integer, db.ForeignKey('specialization.id'), primary_key=True)
)

# Service-Part association
service_parts = db.Table('service_parts',
    db.Column('service_id', db.Integer, db.ForeignKey('service.id'), primary_key=True),
    db.Column('part_id', db.Integer, db.ForeignKey('part.id'), primary_key=True),
    db.Column('quantity_required', db.Integer, default=1)
)

# Vehicle-Service History association
vehicle_service_history = db.Table('vehicle_service_history',
    db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicle.id'), primary_key=True),
    db.Column('service_id', db.Integer, db.ForeignKey('service.id'), primary_key=True),
    db.Column('service_date', db.DateTime, nullable=False),
    db.Column('notes', db.Text)
)

# Customer-Mechanic (preferred mechanics) association
customer_preferred_mechanics = db.Table('customer_preferred_mechanics',
    db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True),
    db.Column('mechanic_id', db.Integer, db.ForeignKey('mechanic.id'), primary_key=True)
)

# Service-Required Tools association
service_required_tools = db.Table('service_required_tools',
    db.Column('service_id', db.Integer, db.ForeignKey('service.id'), primary_key=True),
    db.Column('tool_id', db.Integer, db.ForeignKey('tool.id'), primary_key=True)
)

# Mechanic-Tool Certification association
mechanic_tool_certifications = db.Table('mechanic_tool_certifications',
    db.Column('mechanic_id', db.Integer, db.ForeignKey('mechanic.id'), primary_key=True),
    db.Column('tool_id', db.Integer, db.ForeignKey('tool.id'), primary_key=True),
    db.Column('certification_date', db.DateTime, nullable=False)
)
