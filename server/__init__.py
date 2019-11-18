import os
from flask import Flask
from flask_restplus import Api
from server.models.ping import Ping

# Instanciate the app
app = Flask(__name__)
api = Api(app)

# Set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

api.add_resource(Ping, '/ping')
