from app.extensions import db
from app.models.aidrequest import Aidrequest
from flask import jsonify, current_app
from app.utils.errors import AppError
from threading import Thread
from app.services.ai_jobs import aiCall

def getJobStatus(job_id):
    try:
        job = db.session.get(Aidrequest, job_id)
        if not job:
            raise AppError("No job found", 404)
        obj = job.to_dict()
        if job.status == "failed":
            obj["statusCode"] = 503
            obj["title"] = "Service not available"
            obj["desc"] = "Something went wrong. Please try again."
            obj["btn"] = "Try again"
        return jsonify(obj), 200
    except AppError:
        raise
    except Exception:
        raise AppError("Internal server Error", 500)

def retryjob(job_id, num):
    job = db.session.get(Aidrequest, job_id)
    if not job:
        return AppError("Job not found", 404)
    job.status="pending"
    db.session.commit()
    if num not in {1,2,3}:
        return jsonify({
            "success": False,
            "msg": "path parameter num is missing"
        }), 400
    Thread(
        target=aiCall,
        args=(job.id, current_app._get_current_object(), num),
        daemon=True
    ).start()
    return jsonify({
        "success": True,
    }), 200