import os
from flask import Flask
from flask_restplus import Api
from server.models.ping import Ping
from flask_sqlalchemy import SQLAlchemy

# Instanciate the app
app = Flask(__name__)
api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)

# Set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

api.add_resource(Ping, '/ping')
