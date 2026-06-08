from flask import Blueprint, request
from app.controllers.search import searchCourse

search_bp = Blueprint("search", __name__)

@search_bp.route("/", methods=["GET"], strict_slashes=False)
def main():
    if request.method.lower() == "get":
        return searchCourse()