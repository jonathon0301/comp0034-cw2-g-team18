"""Flask configuration."""
from pathlib import Path

# Sets the project root folder
PROJECT_ROOT = Path(__file__).parent


class Config:
    """Base config."""

    SECRET_KEY = "YY3R4fQ5OmlmVKOSlsVHew"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(
        PROJECT_ROOT.joinpath("data", "gender.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class ProdConfig(Config):
    """Production config.

    Not currently implemented.
    """

    pass


class DevConfig(Config):
    """Development config"""

    FLASK_ENV = "development"
    DEBUG = False
    TESTING = True
    SERVER_NAME = "127.0.0.1:9000"


class TestConfig(Config):
    """Testing config"""

    TESTING = True
    SQLALCHEMY_ECHO = True
    WTF_CSRF_ENABLED = False
    SERVER_NAME = "127.0.0.1:8000"
