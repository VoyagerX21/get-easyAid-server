from app.extensions import db
from app.models.aidrequest import Aidrequest
from app.services.promptgen import promptGen
from app.services.responsegen import GetResponse
from datetime import datetime, timezone

def aiCall(job_id, app, flag = 3):
    with app.app_context():
        job = db.session.get(Aidrequest, job_id)
        if not job:
            return

        try:
            job.status = "running"
            db.session.commit()

            if flag == 1 or flag == 3:
                ans1 = GetResponse(promptGen(job.payload, 1))
                job.first_ans = ans1
                db.session.commit()

            if flag == 2 or flag == 3:
                ans2 = GetResponse(promptGen(job.payload, 2))
                job.second_ans = ans2
                db.session.commit()

            job.status = "completed"
            job.completed_at = datetime.now(timezone.utc)
            db.session.commit()

        except Exception as e:

            db.session.rollback()

            job = db.session.get(Aidrequest, job_id)

            if job:
                job.status = "failed"
                job.error = str(e)
                job.completed_at = datetime.now(timezone.utc)
                db.session.commit()