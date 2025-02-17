import os
from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

# instantiate the db
db = SQLAlchemy()
admin = Admin(template_mode="bootstrap3")


# new
def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    if os.getenv("FLASK_ENV") == "development":
        admin.init_app(app)

    # register blueprints
    from server.api.ping import ping_blueprint

    app.register_blueprint(ping_blueprint)
    from server.api.users.views import users_blueprint

    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
