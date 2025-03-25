from flask import Flask
from app.extensions import db, limiter, cache
from app.routes.customers import customers_bp
from app.routes.vehicles import vehicles_bp
from app.routes.services import services_bp
from app.mechanic import mechanic_bp
from app.service_ticket import service_ticket_bp

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mechanic_shop.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Caching configuration
    app.config['CACHE_TYPE'] = 'SimpleCache'
    app.config['CACHE_DEFAULT_TIMEOUT'] = 300

    # Initialize extensions
    db.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    # Register blueprints
    app.register_blueprint(customers_bp, url_prefix='/customers')
    app.register_blueprint(vehicles_bp, url_prefix='/vehicles')
    app.register_blueprint(services_bp, url_prefix='/services')
    app.register_blueprint(mechanic_bp, url_prefix='/mechanics')
    app.register_blueprint(service_ticket_bp, url_prefix='/service-tickets')

    @app.route("/")
    def home():
        return "Welcome to the Mechanic Shop API. Use the endpoints to manage customers, vehicles, mechanics, and service tickets."

    return app
