from app.extensions import db

class Mechanic(db.Model):
    """Mechanic model representing a mechanic in the shop."""
    __tablename__ = 'mechanic'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    specialization = db.Column(db.String(100))  # e.g., 'Engine', 'Transmission', 'Electrical'
    is_active = db.Column(db.Boolean, default=True)
    
    # Relationships
    service_tickets = db.relationship('ServiceTicket', backref='assigned_mechanic', lazy=True)
    
    def __repr__(self):
        return f'<Mechanic {self.name}>'
    
    def to_dict(self):
        """Convert mechanic object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'specialization': self.specialization,
            'is_active': self.is_active
        }
