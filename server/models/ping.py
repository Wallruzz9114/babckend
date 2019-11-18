from flask_restplus import Resource


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }
