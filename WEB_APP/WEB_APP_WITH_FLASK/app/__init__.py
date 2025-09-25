from flask import Flask
from .routes.main import main__bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(main__bp)
    return app