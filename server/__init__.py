from flask import Flask
from flask_restplus import Api
from server.models.ping import Ping

# Instanciate the app
app = Flask(__name__)
api = Api(app)

# Set config
app.config.from_object('server.config.DevelopmentConfig')

api.add_resource(Ping, '/ping')
