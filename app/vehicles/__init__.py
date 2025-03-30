from flask import Blueprint

vehicles_bp = Blueprint('vehicles', __name__)

from . import routes  # noqa
