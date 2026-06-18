import json
from app import create_app
from app.extensions import db
from app.models.courses import Course

app = create_app()

with app.app_context():

    if Course.query.count() > 0:
        print("Courses already exist")
        exit()

    with open("app/data/easyAidcourses.json", encoding="utf-8") as f:
        courses = json.load(f)
    for i in courses:
        exists = Course.query.filter_by(
            url=i["URL"]
        ).first()

        if exists:
            continue
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