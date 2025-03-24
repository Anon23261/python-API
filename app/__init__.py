from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.routes.customers import customers_bp
from app.routes.vehicles import vehicles_bp
from app.routes.services import services_bp
from app.mechanic import mechanic_bp
from app.service_ticket import service_ticket_bp

db = SQLAlchemy()
limiter = Limiter(get_remote_address)

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mechanic_shop.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    limiter.init_app(app)

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
