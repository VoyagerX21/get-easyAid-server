from flask import Blueprint, request
from app.controllers.regenerate import regen

regen_bp = Blueprint("regen", __name__)

@regen_bp.route("/", methods=["POST"], strict_slashes=False)
def main():
    if request.method.lower() == "post":
        return regen()