from app.extensions import db
from app.common.models import BaseModel

class Specialization(BaseModel):
    """Specialization model representing different areas of expertise."""
    __tablename__ = 'specialization'
    
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    required_certification = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<Specialization {self.name}>'
