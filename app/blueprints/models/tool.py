from app.extensions import db
from app.common.models import BaseModel

class Tool(BaseModel):
    """Tool model representing specialized equipment and tools."""
    __tablename__ = 'tool'
    
    name = db.Column(db.String(100), nullable=False)
    tool_code = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    requires_certification = db.Column(db.Boolean, default=False)
    maintenance_interval_days = db.Column(db.Integer)
    last_maintenance_date = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'<Tool {self.tool_code} - {self.name}>'
