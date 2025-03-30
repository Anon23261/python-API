from flask import Flask
from app.extensions import db, limiter, cache, jwt
from app.customers.routes import customers_bp
from app.vehicles.routes import vehicles_bp
from app.services.routes import services_bp
from app.mechanic.routes import mechanic_bp
from app.service_ticket.routes import service_ticket_bp
from app.auth import auth_bp
import os

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///mechanic_shop.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Caching configuration
    app.config['CACHE_TYPE'] = os.getenv('CACHE_TYPE', 'SimpleCache')
    app.config['CACHE_DEFAULT_TIMEOUT'] = int(os.getenv('CACHE_TIMEOUT', '300'))

    # JWT configuration
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'CHANGE_THIS_IN_PRODUCTION')  # Required in production
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', '3600'))  # 1 hour by default

    # Rate limiting configuration
    app.config['RATELIMIT_STORAGE_URL'] = os.getenv('REDIS_URL', 'memory://')
    app.config['RATELIMIT_STRATEGY'] = 'fixed-window'

    # Initialize extensions
    db.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')  # Register auth blueprint first
    app.register_blueprint(customers_bp, url_prefix='/customers')
    app.register_blueprint(vehicles_bp, url_prefix='/vehicles')
    app.register_blueprint(services_bp, url_prefix='/services')
    app.register_blueprint(mechanic_bp, url_prefix='/mechanics')
    app.register_blueprint(service_ticket_bp, url_prefix='/service-tickets')

    @app.route("/")
    def home():
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Mechanic Shop API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    line-height: 1.6;
                }
                h1 {
                    color: #2c3e50;
                    border-bottom: 2px solid #3498db;
                    padding-bottom: 10px;
                }
                .endpoints {
                    background-color: #f8f9fa;
                    padding: 20px;
                    border-radius: 5px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Mechanic Shop API</h1>
            <div class="endpoints">
                <h2>Available Endpoints:</h2>
                <ul>
                    <li>/auth - Authentication</li>
                    <li>/customers - Customer management</li>
                    <li>/vehicles - Vehicle management</li>
                    <li>/services - Service management</li>
                    <li>/mechanics - Mechanic management</li>
                    <li>/service-tickets - Service ticket management</li>
                </ul>
                <p>Please refer to the API documentation for detailed usage instructions.</p>
            </div>
        </body>
        </html>
        """

    return app
