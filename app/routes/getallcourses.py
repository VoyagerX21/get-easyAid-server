from flask import Blueprint, request
from app.controllers.getallcourses import getallcourses

getallcourses_bp = Blueprint("getallcourses", __name__)

@getallcourses_bp.route("/", methods=["GET"], strict_slashes=False)
def getAll():
    if request.method.lower() == "get":
        return getallcourses()