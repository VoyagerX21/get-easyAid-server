from app.extensions import db
from uuid import uuid4

class Course(db.Model):
    
    id = db.Column(db.String(255), primary_key=True, default=lambda: str(uuid4()))
    title = db.Column(db.String(100), index=True, nullable=False)
    rating = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    org = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(500), nullable=False)
    seenStatus = db.Column(db.Boolean, default=lambda: False)
    specstatus = db.Column(db.Boolean)
    specurl = db.Column(db.String(500))

    speclist = db.relationship("Spec", back_populates="course")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "rating": self.rating,
            "URL": self.url,
            "cached": self.seenStatus
        }