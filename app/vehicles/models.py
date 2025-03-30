from app.extensions import db

class Vehicle(db.Model):
    """Vehicle model representing a customer's vehicle."""
    __tablename__ = 'vehicle'
    
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    
    # Relationships
    owner = db.relationship('Customer', backref=db.backref('vehicles', lazy=True))
    
    def __repr__(self):
        return f'<Vehicle {self.year} {self.make} {self.model}>'
    
    def to_dict(self):
        """Convert vehicle object to dictionary."""
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'owner_id': self.owner_id
        }
