from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from app.common.models import BaseModel
from app.blueprints.associations import customer_preferred_mechanics

class Customer(BaseModel):
    """Customer model representing a client in the auto repair shop."""
    __tablename__ = 'customer'
    
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    preferred_contact_method = db.Column(db.String(20), default='email')
    notes = db.Column(db.Text, nullable=True)
    
    # Many-to-Many relationships
    preferred_mechanics = db.relationship('Mechanic',
                                       secondary=customer_preferred_mechanics,
                                       lazy='subquery',
                                       backref=db.backref('preferred_by_customers', lazy=True))
    
    # One-to-Many relationships
    vehicles = db.relationship('Vehicle', backref='owner', lazy=True,
                             cascade='all, delete-orphan')
    service_tickets = db.relationship('ServiceTicket', backref='customer', lazy=True,
                                    cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Set the password hash for the customer."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if the provided password matches."""
        return check_password_hash(self.password_hash, password)
    
    def add_preferred_mechanic(self, mechanic):
        """Add a mechanic to customer's preferred list."""
        if mechanic not in self.preferred_mechanics:
            self.preferred_mechanics.append(mechanic)
    
    def remove_preferred_mechanic(self, mechanic):
        """Remove a mechanic from customer's preferred list."""
        if mechanic in self.preferred_mechanics:
            self.preferred_mechanics.remove(mechanic)
    
    def __repr__(self):
        return f'<Customer {self.name}>'
    
    def to_dict(self):
        """Convert customer object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'preferred_contact_method': self.preferred_contact_method,
            'vehicles': [vehicle.to_dict() for vehicle in self.vehicles],
            'preferred_mechanics': [
                {
                    'id': m.id,
                    'name': m.name,
                    'specializations': [s.name for s in m.specializations]
                } for m in self.preferred_mechanics
            ],
            'service_tickets': [ticket.to_dict() for ticket in self.service_tickets],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
