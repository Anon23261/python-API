from app import create_app
from app.routes.auth import auth_bp
from app.extensions import db
from app import create_app
from app.routes.auth import auth_bp
from app.extensions import db

app = create_app()

# Register the auth blueprint
app.register_blueprint(auth_bp, url_prefix='/auth')

# Ensure database tables are created
if __name__ == '__main__':
    with app.app_context():
        from app.models import Customer
        db.create_all()
        if not Customer.query.filter_by(email="john.doe@example.com").first():
            test_customer = Customer(name="John Doe", email="john.doe@example.com")
            db.session.add(test_customer)
            db.session.commit()
    app.run(debug=True)