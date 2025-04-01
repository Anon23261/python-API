from app.extensions import db
from app.service_ticket.models import ServiceTicket
from werkzeug.security import generate_password_hash, check_password_hash

class Customer(db.Model):
    """Customer model representing a client in the auto repair shop."""
    __tablename__ = 'customer'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    
    # Relationships
    service_tickets = db.relationship('ServiceTicket', backref='customer', lazy=True)
    
    def set_password(self, password):
        """Set the password hash for the customer."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if the provided password matches."""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<Customer {self.name}>'
    
    def to_dict(self):
        """Convert customer object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
