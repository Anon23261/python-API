from flask import jsonify
from app import create_app
from app.extensions import db
from app.blueprints.customers.models import Customer
from app.blueprints.mechanics.models import Mechanic
from app.blueprints.services.models import Service
from app.blueprints.vehicles.models import Vehicle
from app.blueprints.service_tickets.models import ServiceTicket

app = create_app()

@app.cli.command("init-db")
def init_db():
    """Initialize the database with sample data."""
    db.drop_all()
    db.create_all()
    
    # Create sample customers
    customer1 = Customer(name="John Doe", email="john@example.com")
    customer1.set_password("password123")
    customer2 = Customer(name="Jane Smith", email="jane@example.com")
    customer2.set_password("password456")
    
    # Create sample mechanics
    mechanic1 = Mechanic(name="Bob Wilson", specialization="Engine Repair")
    mechanic2 = Mechanic(name="Alice Brown", specialization="Brake Systems")
    
    # Create sample services
    service1 = Service(name="Oil Change", description="Full synthetic oil change", price=49.99, duration_hours=1.0)
    service2 = Service(name="Brake Service", description="Brake pad replacement", price=199.99, duration_hours=2.0)
    
    # Add all to session
    db.session.add_all([customer1, customer2, mechanic1, mechanic2, service1, service2])
    db.session.commit()
    
    # Create sample vehicles
    vehicle1 = Vehicle(make="Toyota", model="Camry", year=2020, vin="1HGCM82633A123456", customer_id=customer1.id)
    vehicle2 = Vehicle(make="Honda", model="Civic", year=2019, vin="2HGES16575H123456", customer_id=customer2.id)
    
    # Create sample service tickets
    ticket1 = ServiceTicket(
        description="Regular maintenance",
        status="pending",
        customer_id=customer1.id,
        vehicle_id=1,
        mechanic_id=mechanic1.id,
        service_id=service1.id
    )
    
    # Add vehicles and tickets
    db.session.add_all([vehicle1, vehicle2, ticket1])
    db.session.commit()
    
    print("Database initialized with sample data!")

if __name__ == "__main__":
    app.run(debug=True)