from flask import Blueprint

bp = Blueprint('customers', __name__)

from app.blueprints.customers import routes
