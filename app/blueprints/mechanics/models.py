from app.extensions import db
from app.common.models import BaseModel
from app.blueprints.associations import (
    mechanic_specializations,
    mechanic_tool_certifications,
    customer_preferred_mechanics
)

class Mechanic(BaseModel):
    """Mechanic model representing an auto repair technician."""
    __tablename__ = 'mechanic'
    
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    hourly_rate = db.Column(db.Float)
    years_of_experience = db.Column(db.Integer)
    
    # Many-to-Many relationships
    specializations = db.relationship('Specialization', 
                                    secondary=mechanic_specializations,
                                    lazy='subquery',
                                    backref=db.backref('mechanics', lazy=True))
    
    certified_tools = db.relationship('Tool',
                                    secondary=mechanic_tool_certifications,
                                    lazy='subquery',
                                    backref=db.backref('certified_mechanics', lazy=True))
    
    # One-to-Many relationships
    service_tickets = db.relationship('ServiceTicket', backref='assigned_mechanic', lazy=True)
    
    def __repr__(self):
        return f'<Mechanic {self.name}>'
    
    def to_dict(self):
        """Convert mechanic object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'hourly_rate': self.hourly_rate,
            'years_of_experience': self.years_of_experience,
            'specializations': [s.name for s in self.specializations],
            'certified_tools': [t.name for t in self.certified_tools],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
