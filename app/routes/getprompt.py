from flask import Blueprint, request
from app.controllers.getprompt import prompt

getprompt_bp = Blueprint("getprompt", __name__)

@getprompt_bp.route("/", methods=["POST"], strict_slashes=False)
def main():
    if request.method.lower() == "post":
        return prompt()