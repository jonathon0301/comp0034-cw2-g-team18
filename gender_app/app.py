from flask import Flask
from config import DevConfig
from pathlib import Path
from exts import initialize_extensions, db, ma

PROJECT_ROOT = Path(__file__).parent
app = Flask(__name__)
app.config.from_object(DevConfig)


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    initialize_extensions(app)
    with app.app_context():
        # db.create_all()
        import routes
        from models import Gender_pay
    return app


if __name__ == "__main__":
    app = create_app(DevConfig)
    app.run()