from flask_smorest import Blueprint
from flask.views import MethodView
from app.controllers.getallcourses import getallcourses
from app.schemas.getallcoursesSchema import GetCoursesRes, GetCourseReq

getallcourses_bp = Blueprint("getallcourses", __name__)

@getallcourses_bp.route("/", strict_slashes=False)
class AllCourses(MethodView):

    @getallcourses_bp.arguments(GetCourseReq, location="query")
    @getallcourses_bp.response(200, GetCoursesRes)
    def get(self, args):
        return getallcourses(args)