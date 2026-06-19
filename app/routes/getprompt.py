from flask_smorest import Blueprint
from flask.views import MethodView
from app.controllers.getprompt import prompt
from app.schemas.promptSchema import PromptReq, PromptRes

getprompt_bp = Blueprint("getprompt", __name__)

@getprompt_bp.route("/", strict_slashes=False)
class Main(MethodView):

    @getprompt_bp.arguments(PromptReq)
    @getprompt_bp.response(201, PromptRes)
    def post(self, data):
        return prompt(data)
