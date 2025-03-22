from flask import Flask
from app.routes.customers import customers_bp
from app.routes.vehicles import vehicles_bp
from app.routes.services import services_bp
from app.mechanic import mechanic_bp
from app.service_ticket import service_ticket_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(customers_bp, url_prefix='/customers')
    app.register_blueprint(vehicles_bp, url_prefix='/vehicles')
    app.register_blueprint(services_bp, url_prefix='/services')
    app.register_blueprint(mechanic_bp, url_prefix='/mechanics')
    app.register_blueprint(service_ticket_bp, url_prefix='/service-tickets')

    @app.route("/")
    def home():
        return "Welcome to the Mechanic Shop API. Use the endpoints to manage customers, vehicles, mechanics, and service tickets."

    return app
