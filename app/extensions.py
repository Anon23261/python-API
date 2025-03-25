from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
limiter = Limiter(get_remote_address)
cache = Cache()
jwt = JWTManager()
