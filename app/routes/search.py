from flask_smorest import Blueprint
from flask.views import MethodView
from app.controllers.search import searchCourse
from app.schemas.searchSchema import SearchRes, SearchQuery

search_bp = Blueprint("search", __name__)

@search_bp.route("/", strict_slashes=False)
class Search(MethodView):

    @search_bp.arguments(SearchQuery, location="query")
    @search_bp.response(200, SearchRes)
    def get(self, args):
        return searchCourse(args)