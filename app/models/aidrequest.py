from app.extensions import db
from uuid import uuid4
from datetime import timezone, datetime

class Aidrequest(db.Model):

    id = db.Column(db.String(255), primary_key=True, default=lambda: str(uuid4()))
    status = db.Column(db.String(20), default="pending")
    payload = db.Column(db.JSON, nullable=False)
    first_ans = db.Column(db.Text)
    second_ans = db.Column(db.Text)
    error = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    completed_at = db.Column(db.DateTime(timezone=True))

    def to_dict(self):
        if self.status == "failed":
            return {
                "job_id": self.id,
                "status": self.status,
                "error": self.error,
                "time": (self.completed_at-self.created_at).total_seconds() / 60
            }
        if self.status == "running" or self.status == "pending":
            return {
                "job_id": self.id,
                "status": self.status,
            }
        return {
            "job_id": self.id,
            "status": self.status,
            "firstRes": self.first_ans,
            "secondRes": self.second_ans,
            "time": (self.completed_at-self.created_at).total_seconds() / 60
        }