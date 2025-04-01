from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
limiter = Limiter(key_func=get_remote_address)
cache = Cache()
jwt = JWTManager()
migrate = Migrate()
