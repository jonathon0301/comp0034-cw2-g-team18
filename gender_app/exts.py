from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
ma = Marshmallow()
bootstrap = Bootstrap()


def initialize_extensions(app: Flask):
    """Binds extensions to the Flask application instance (app)"""
    # Flask-SQLAlchemy
    db.init_app(app)
    # Flask-Marshmallows
    ma.init_app(app)
    bootstrap.init_app(app)

