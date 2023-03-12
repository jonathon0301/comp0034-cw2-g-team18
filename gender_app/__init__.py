from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "4IX2rckBgBvzMHWMmT9GxA"

    with app.app_context():
        from gender_app import gender

    return app
