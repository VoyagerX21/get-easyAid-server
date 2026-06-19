from flask_smorest import Blueprint
from flask.views import MethodView
from app.schemas.healthSchema import HealthRes

health_bp = Blueprint("health", __name__)

@health_bp.route("/", strict_slashes=False)
class Health(MethodView):

    @health_bp.response(200, HealthRes)
    def get(self):
        return {
            "success": "API is running"
        }