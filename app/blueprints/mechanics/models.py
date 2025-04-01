from app.extensions import db

class Mechanic(db.Model):
    """Mechanic model representing a mechanic in the auto repair shop."""
    __tablename__ = 'mechanic'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<Mechanic {self.name}>'
    
    def to_dict(self):
        """Convert mechanic object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'specialization': self.specialization
        }
