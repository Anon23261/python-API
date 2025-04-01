from datetime import datetime
from app.extensions import db
from app.common.models import BaseModel
from app.blueprints.associations import vehicle_service_history

class Vehicle(BaseModel):
    """Vehicle model representing a customer's vehicle."""
    __tablename__ = 'vehicle'
    
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    vin = db.Column(db.String(17), unique=True, nullable=False)
    license_plate = db.Column(db.String(20))
    color = db.Column(db.String(30))
    mileage = db.Column(db.Integer)
    last_service_date = db.Column(db.DateTime)
    
    # Foreign keys
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    
    # Many-to-Many relationships
    service_history = db.relationship('Service',
                                    secondary=vehicle_service_history,
                                    lazy='subquery',
                                    backref=db.backref('serviced_vehicles', lazy=True))
    
    # One-to-Many relationships
    service_tickets = db.relationship('ServiceTicket', backref='vehicle', lazy=True)
    
    def add_service_to_history(self, service, notes=None):
        """Add a service to the vehicle's service history."""
        self.service_history.append(service)
        db.session.execute(
            vehicle_service_history.insert().values(
                vehicle_id=self.id,
                service_id=service.id,
                service_date=datetime.utcnow(),
                notes=notes
            )
        )
    
    def __repr__(self):
        return f'<Vehicle {self.year} {self.make} {self.model}>'
    
    def to_dict(self):
        """Convert vehicle object to dictionary."""
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'vin': self.vin,
            'license_plate': self.license_plate,
            'color': self.color,
            'mileage': self.mileage,
            'last_service_date': self.last_service_date.isoformat() if self.last_service_date else None,
            'customer_id': self.customer_id,
            'service_history': [{
                'service': s.name,
                'date': db.session.query(vehicle_service_history.c.service_date)
                    .filter_by(vehicle_id=self.id, service_id=s.id)
                    .scalar().isoformat(),
                'notes': db.session.query(vehicle_service_history.c.notes)
                    .filter_by(vehicle_id=self.id, service_id=s.id)
                    .scalar()
            } for s in self.service_history],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
