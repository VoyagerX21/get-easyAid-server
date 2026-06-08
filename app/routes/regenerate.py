from flask import Blueprint, request

regen_bp = Blueprint("regen", __name__)

@regen_bp.route("/", methods=["POST"])
def main():
    if request.method.lower() == "post":
        return