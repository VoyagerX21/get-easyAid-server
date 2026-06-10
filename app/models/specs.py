from app.extensions import db
from uuid import uuid4

class Spec(db.Model):

    id = db.Column(db.String(255), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.Text, nullable=False, index=True)
    course_id = db.Column(db.String(255), db.ForeignKey("course.id"))

    course = db.relationship("Course", back_populates="speclist")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "course": self.course.title
        }