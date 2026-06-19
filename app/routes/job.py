from flask_smorest import Blueprint
from flask.views import MethodView
from app.controllers.job import getJobStatus, retryjob
from app.schemas.jobSchema import JobRes
from app.schemas.retrySchema import RetryRes

job_bp = Blueprint("job", __name__)

@job_bp.route("/<jobid>")
class Main(MethodView):

    @job_bp.response(200, JobRes)
    def get(self, jobid):
        return getJobStatus(jobid)
    
@job_bp.route("/retry/<jobid>/<int:num>")
class Retry(MethodView):

    @job_bp.response(200, RetryRes)
    def post(self, jobid, num):
        return retryjob(jobid, num)