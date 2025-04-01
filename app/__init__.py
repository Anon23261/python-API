from flask import Flask
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from config import Config

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()
limiter = Limiter(key_func=get_remote_address)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    limiter.init_app(app)

    # Register blueprints
    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.blueprints.customers import bp as customers_bp
    app.register_blueprint(customers_bp, url_prefix='/customers')

    from app.blueprints.vehicles import bp as vehicles_bp
    app.register_blueprint(vehicles_bp, url_prefix='/vehicles')

    from app.blueprints.mechanics import bp as mechanics_bp
    app.register_blueprint(mechanics_bp, url_prefix='/mechanics')

    from app.blueprints.services import bp as services_bp
    app.register_blueprint(services_bp, url_prefix='/services')

    from app.blueprints.service_tickets import bp as service_tickets_bp
    app.register_blueprint(service_tickets_bp, url_prefix='/service-tickets')

    return app
