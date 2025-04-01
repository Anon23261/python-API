from flask import Blueprint

bp = Blueprint('mechanics', __name__)

from app.blueprints.mechanics import routes
