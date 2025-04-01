from datetime import datetime
from app.extensions import db
from app.common.models import BaseModel

class ServiceTicket(BaseModel):
    """Service Ticket model representing a service request."""
    __tablename__ = 'service_ticket'
    
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, in_progress, completed, cancelled
    scheduled_date = db.Column(db.DateTime)
    completion_date = db.Column(db.DateTime)
    estimated_cost = db.Column(db.Float)
    final_cost = db.Column(db.Float)
    diagnostic_notes = db.Column(db.Text)
    completion_notes = db.Column(db.Text)
    priority = db.Column(db.Integer, default=1)  # 1-5 scale
    
    # Foreign keys
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    mechanic_id = db.Column(db.Integer, db.ForeignKey('mechanic.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    
    def update_status(self, new_status, notes=None):
        """Update the status of the service ticket."""
        self.status = new_status
        if new_status == 'completed':
            self.completion_date = datetime.utcnow()
            self.completion_notes = notes
        self.save()
    
    def calculate_final_cost(self):
        """Calculate the final cost including parts and labor."""
        if not self.service_type:
            return 0
            
        base_cost = self.service_type.calculate_total_price()
        labor_cost = (self.service_type.estimated_hours or 0) * (self.assigned_mechanic.hourly_rate or 0)
        return base_cost + labor_cost
    
    def __repr__(self):
        return f'<ServiceTicket {self.id} - {self.status}>'
    
    def to_dict(self):
        """Convert service ticket object to dictionary."""
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'scheduled_date': self.scheduled_date.isoformat() if self.scheduled_date else None,
            'completion_date': self.completion_date.isoformat() if self.completion_date else None,
            'estimated_cost': self.estimated_cost,
            'final_cost': self.final_cost or self.calculate_final_cost(),
            'diagnostic_notes': self.diagnostic_notes,
            'completion_notes': self.completion_notes,
            'priority': self.priority,
            'customer': {
                'id': self.customer.id,
                'name': self.customer.name,
                'email': self.customer.email
            } if self.customer else None,
            'vehicle': {
                'id': self.vehicle.id,
                'make': self.vehicle.make,
                'model': self.vehicle.model,
                'year': self.vehicle.year,
                'vin': self.vehicle.vin
            } if self.vehicle else None,
            'mechanic': {
                'id': self.assigned_mechanic.id,
                'name': self.assigned_mechanic.name,
                'specializations': [s.name for s in self.assigned_mechanic.specializations]
            } if self.assigned_mechanic else None,
            'service': {
                'id': self.service_type.id,
                'name': self.service_type.name,
                'base_price': self.service_type.base_price,
                'estimated_hours': self.service_type.estimated_hours
            } if self.service_type else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
