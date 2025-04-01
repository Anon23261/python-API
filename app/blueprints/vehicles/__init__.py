from flask import Blueprint

bp = Blueprint('vehicles', __name__)

from app.blueprints.vehicles import routes
