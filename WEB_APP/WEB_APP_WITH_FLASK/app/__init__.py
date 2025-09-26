from flask import Flask
from pymongo import MongoClient

db = None

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('config.Config')
    global db

    try:
        client = MongoClient(app.config['MONGO_URI'])
        db = client.get_default_database()
    except Exception as e:
        print(f'Error on setup database config {e}')

    from .routes.main import main__bp
    app.register_blueprint(main__bp)

    return app