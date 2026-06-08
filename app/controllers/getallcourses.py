from app.extensions import db
from flask import jsonify

mycollection = db["courses"]

def getallcourses():
    data = list(mycollection.find({}, {'_id': 0}))
    return jsonify(data)