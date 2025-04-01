from app.extensions import db
from app.common.models import BaseModel

class Part(BaseModel):
    """Part model representing auto parts inventory."""
    __tablename__ = 'part'
    
    name = db.Column(db.String(100), nullable=False)
    part_number = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    quantity_in_stock = db.Column(db.Integer, default=0)
    manufacturer = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<Part {self.part_number} - {self.name}>'
