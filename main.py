from app import create_app
from app.auth import auth_bp
from app.customers import customers_bp
from app.services import services_bp
from app.vehicles import vehicles_bp
from app.mechanic import mechanic_bp
from app.service_ticket import service_ticket_bp
from app.extensions import db

app = create_app()

# Register all blueprints
blueprints = [
    (auth_bp, '/auth'),
    (customers_bp, '/customers'),
    (services_bp, '/services'),
    (vehicles_bp, '/vehicles'),
    (mechanic_bp, '/mechanics'),
    (service_ticket_bp, '/service-tickets')
]

for blueprint, url_prefix in blueprints:
    app.register_blueprint(blueprint, url_prefix=url_prefix)

# Ensure database tables are created
if __name__ == '__main__':
    with app.app_context():
        from app.customers.models import Customer
        db.create_all()
        if not Customer.query.filter_by(email="john.doe@example.com").first():
            test_customer = Customer(name="John Doe", email="john.doe@example.com")
            db.session.add(test_customer)
            db.session.commit()
    app.run(debug=True)