from flask import Blueprint, request
from app.controllers.submit import submitReq

submit_bp = Blueprint("submit", __name__)

@submit_bp.route("/", methods=["POST"], strict_slashes=False)
def main():
    if request.method.lower() == "post":
        return submitReq()