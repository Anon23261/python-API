from app.extensions import db
from app.common.models import BaseModel
from app.blueprints.associations import service_parts, service_required_tools

class Service(BaseModel):
    """Service model representing available services in the auto repair shop."""
    __tablename__ = 'service'
    
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    base_price = db.Column(db.Float, nullable=False)
    estimated_hours = db.Column(db.Float)
    complexity_level = db.Column(db.Integer)  # 1-5 scale
    is_diagnostic = db.Column(db.Boolean, default=False)
    
    # Many-to-Many relationships
    required_parts = db.relationship('Part',
                                   secondary=service_parts,
                                   lazy='subquery',
                                   backref=db.backref('used_in_services', lazy=True))
    
    required_tools = db.relationship('Tool',
                                   secondary=service_required_tools,
                                   lazy='subquery',
                                   backref=db.backref('used_in_services', lazy=True))
    
    # One-to-Many relationships
    service_tickets = db.relationship('ServiceTicket', backref='service_type', lazy=True)
    
    def calculate_total_price(self):
        """Calculate total price including parts."""
        parts_cost = sum(part.price for part in self.required_parts)
        return self.base_price + parts_cost
    
    def __repr__(self):
        return f'<Service {self.name}>'
    
    def to_dict(self):
        """Convert service object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'base_price': self.base_price,
            'total_price': self.calculate_total_price(),
            'estimated_hours': self.estimated_hours,
            'complexity_level': self.complexity_level,
            'is_diagnostic': self.is_diagnostic,
            'required_parts': [p.to_dict() for p in self.required_parts],
            'required_tools': [t.name for t in self.required_tools],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
