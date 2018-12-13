from flask import current_app
#from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

from .config import FLASK_ENV


#db = SQLAlchemy()
cache = Cache(config={'CACHE_TYPE': 'simple'})


def init_app(app):
    #db.init_app(app)
    cache.init_app(app)
