from uuid import UUID
import os
import bson
import flask
from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

host = os.environ.get("MONGO_HOST", "localhost")
port = int(os.environ.get("MONGO_PORT", 27017))

client = MongoClient(host, port)

db = client[os.environ.get("MONGO_DB", 'mayaprotect')]
col = db['owners']

@cross_origin()
@app.route('/owners/<owner_id>', methods=['POST'])
def update_owner(owner_id):
    data = request.get_json()
    update_selector = {'uuid': bson.Binary.from_uuid(UUID(owner_id))}
    update_data = {'$push': {'events': [data]}}
    result = col.update_one(update_selector, update_data)
    return flask.Response(status=201)


app.run(host="0.0.0.0", port=8080, debug=True)
