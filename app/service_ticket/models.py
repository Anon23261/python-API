from app.extensions import db
from datetime import datetime
from app.mechanic.models import Mechanic
from app.services.models import Service

class ServiceTicket(db.Model):
    """Service ticket model representing a service request."""
    __tablename__ = 'service_ticket'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')  # pending, in_progress, completed, cancelled
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    mechanic_id = db.Column(db.Integer, db.ForeignKey('mechanic.id'), nullable=True)  # Can be assigned later
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    
    # Relationships
    vehicle = db.relationship('Vehicle')
    mechanic = db.relationship('Mechanic')
    service = db.relationship('Service')
    
    def __repr__(self):
        return f'<ServiceTicket {self.id} - {self.status}>'
    
    def to_dict(self):
        """Convert service ticket object to dictionary."""
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'customer_id': self.customer_id,
            'vehicle_id': self.vehicle_id,
            'mechanic_id': self.mechanic_id,
            'service_id': self.service_id
        }
