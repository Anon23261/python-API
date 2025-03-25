from app import create_app
from app.routes.auth import auth_bp
from app.extensions import db
app = create_app()
app = create_app()
# Register the auth blueprint
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(auth_bp, url_prefix='/auth')

# Ensure database tables are created








    app.run(debug=True)if __name__ == '__main__':        db.session.commit()        db.session.add(test_customer)        test_customer = Customer(name="John Doe", email="john.doe@example.com")


    app.run(debug=True)if __name__ == '__main__':    db.create_all()
    if not Customer.query.filter_by(email="john.doe@example.com").first():with app.app_context():    from app.models import Customer