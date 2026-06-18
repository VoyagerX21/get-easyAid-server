from flask import Blueprint, request
from app.controllers.job import getJobStatus, retryjob

job_bp = Blueprint("job", __name__)

@job_bp.route("/<jobid>", methods=["GET"])
def main(jobid):
    if request.method.lower() == "get":
        return getJobStatus(jobid)
    
@job_bp.route("/retry/<jobid>/<int:num>", methods=["POST"])
def retry(jobid, num):
    if request.method.lower() == "post":
        return retryjob(jobid, num)