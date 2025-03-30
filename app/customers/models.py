from app.extensions import db

class Customer(db.Model):
    """Customer model representing a client in the auto repair shop."""
    __tablename__ = 'customer'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    # Relationships
    vehicles = db.relationship('Vehicle', backref='owner', lazy=True)
    service_tickets = db.relationship('ServiceTicket', backref='customer', lazy=True)
    
    def __repr__(self):
        return f'<Customer {self.name}>'
    
    def to_dict(self):
        """Convert customer object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
