import json
from app import create_app
from app.extensions import db
from app.models.courses import Course

app = create_app()

with app.app_context():

    with open("app/data/easyAid.courses.json", encoding="utf-8") as f:
        courses = json.load(f)
    for i in courses:
        course = Course(
            title=i["title"],
            rating=i["rating"],
            description=i["Description"],
            url=i["URL"],
            org=i["Organization"]
        )
        db.session.add(course)
    db.session.commit()
    print("Done")