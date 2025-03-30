from app.extensions import db

class Service(db.Model):
    """Service model representing available services in the auto repair shop."""
    __tablename__ = 'service'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Service {self.name}>'
    
    def to_dict(self):
        """Convert service object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }
