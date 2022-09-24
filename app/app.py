import flask
from flask_cors import CORS, cross_origin
import pymongo
import json
from app.owner import Owner

class PostOwner:
    def __init__(self, params) -> None:
        self.__app = flask.Flask(__name__)
        CORS(self.__app)
        self.__app.add_url_rule('/owners', 'post_owner', self.post_owner, methods=['POST'])

        self.__mongo = pymongo.MongoClient(params["mongo_host"], params["mongo_port"])
        self.__db = self.__mongo[params["mongo_db"]]

    @cross_origin()
    def post_owner(self) -> flask.Response:
        data = flask.request.get_json()
        collection = self.__db['owners']
        try:
            owner = Owner(data)
            collection.insert_one(owner.to_save_data())
            return flask.Response(json.dumps(owner.to_respond()), status=201, mimetype="application/json")
        except Exception as e:
            message = {
                "message": str(e)
            }
            return flask.Response(json.dumps(message), status=400, mimetype="application/json")

    def run(self):
        self.__app.run('0.0.0.0', 8000)
