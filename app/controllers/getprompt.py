from flask import request, jsonify, current_app
from app.models.aidrequest import Aidrequest
from app.extensions import db
from threading import Thread
from app.services.ai_jobs import aiCall

def prompt():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "success": False,
            "message": "Invalid payload"
        }), 400
    job = Aidrequest(
        payload=data
    )
    db.session.add(job)
    db.session.commit()
    Thread(
        target=aiCall,
        args=(job.id, current_app._get_current_object()),
        daemon=True
    ).start()
    return jsonify({
        "job_id": job.id,
        "success": True
    }), 202