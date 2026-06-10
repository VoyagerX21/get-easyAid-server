from app.models.courses import Course
from flask import jsonify

def getallcourses():
    data = Course.query.all()
    return jsonify(data)