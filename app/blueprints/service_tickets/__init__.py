from flask import Blueprint

bp = Blueprint('service_tickets', __name__)

from app.blueprints.service_tickets import routes
