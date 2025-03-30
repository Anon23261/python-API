from app import create_app
from app.extensions import db
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = create_app()

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