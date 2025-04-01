from flask import Flask
from flask_cors import CORS
from config import Config
from app.extensions import db, jwt, limiter, cache, migrate
from flask_migrate import Migrate

def init_sample_data(app):
    """Initialize sample data for development."""
    with app.app_context():
        from app.blueprints.customers.models import Customer
        from app.blueprints.mechanics.models import Mechanic
        from app.blueprints.services.models import Service
        from app.blueprints.vehicles.models import Vehicle
        from app.blueprints.service_tickets.models import ServiceTicket
        
        if not Customer.query.first():  # Only initialize if no data exists
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

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)
    limiter.init_app(app)
    cache.init_app(app)
    migrate.init_app(app, db)

    # Import blueprints
    from app.blueprints.service_tickets import service_tickets_bp
    from app.blueprints.customers import customers_bp
    from app.blueprints.mechanics import mechanics_bp
    from app.blueprints.auth import auth_bp
    from app.blueprints.services import services_bp
    from app.blueprints.vehicles import vehicles_bp

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(customers_bp, url_prefix='/api/customers')
    app.register_blueprint(mechanics_bp, url_prefix='/api/mechanics')
    app.register_blueprint(service_tickets_bp, url_prefix='/api/service-tickets')
    app.register_blueprint(services_bp, url_prefix='/api/services')
    app.register_blueprint(vehicles_bp, url_prefix='/api/vehicles')

    # Create database tables and initialize sample data
    with app.app_context():
        db.create_all()
        init_sample_data(app)

    @app.route('/')
    def home():
        """API Home page with documentation."""
        return '''
        <html>
            <head>
                <title>Auto Repair Shop API</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                    }
                    .header {
                        text-align: center;
                        padding: 20px;
                        background-color: #f5f5f5;
                        border-radius: 5px;
                    }
                    .endpoints {
                        margin-top: 20px;
                    }
                    ul {
                        list-style-type: none;
                        padding-left: 0;
                    }
                    li {
                        padding: 10px;
                        margin: 5px 0;
                        background-color: #f9f9f9;
                        border-radius: 3px;
                    }
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>Welcome to the Auto Repair Shop API</h1>
                    <p>This API provides endpoints for managing an auto repair shop's operations.</p>
                </div>
                <div class="endpoints">
                    <h2>Available Endpoints:</h2>
                    <ul>
                        <li>/api/auth - Authentication</li>
                        <li>/api/customers - Customer management</li>
                        <li>/api/vehicles - Vehicle management</li>
                        <li>/api/services - Service management</li>
                        <li>/api/mechanics - Mechanic management</li>
                        <li>/api/service-tickets - Service ticket management</li>
                    </ul>
                    <p>Please refer to the API documentation for detailed usage instructions.</p>
                </div>
            </body>
        </html>
        '''

    return app
