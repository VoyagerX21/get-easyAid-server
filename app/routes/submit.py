from flask_smorest import Blueprint
from flask.views import MethodView
from app.controllers.submit import submitReq
from app.schemas.submitSchema import SubmitReq, SubmitRes

submit_bp = Blueprint("submit", __name__)

@submit_bp.route("/", strict_slashes=False)
class Main(MethodView):

    @submit_bp.arguments(SubmitReq)
    @submit_bp.response(200, SubmitRes)
    def post(self, data):
        return submitReq(data)