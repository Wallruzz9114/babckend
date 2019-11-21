import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server.api.blueprints.ping import ping_blueprint

from dotenv import load_dotenv
load_dotenv()

# Instanciate the database
db = SQLAlchemy()


def create_app(script_info=None):
    # Instantiate the app
    app = Flask(__name__)
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    # set up extensions
    db.init_app(app)
    # register blueprints
    app.register_blueprint(ping_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
