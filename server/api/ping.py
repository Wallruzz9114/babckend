from flask import Blueprint
from flask_restplus import Api, Resource

ping_blueprint = Blueprint("ping", __name__)
api = Api(ping_blueprint)


class Ping(Resource):
    def get(self):
        return {"status": "success", "message": "myPong!"}


api.add_resource(Ping, "/ping")
