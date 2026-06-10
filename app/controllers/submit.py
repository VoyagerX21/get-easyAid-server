from flask import request, jsonify
from app.utils.scrapepage import scrap
from app.extensions import db
from app.models.courses import Course
from app.models.specs import Spec

def submitReq():
    data = request.get_json()
    obj = data.get('obj')
    course = Course.query.filter_by(title=obj["title"], url=obj["URL"]).first()
    print(course)
    if course.seenStatus:
        if course.specstatus:
            url, courselist = course.specurl, [i.name for i in course.speclist]
        else:
            url, courselist = None, []
    else:
        scrapped = scrap(obj['title'], obj['URL'])
        course.seenStatus = True
        if scrapped:
            course.specstatus = True
            url, courselist = scrapped
            course.specurl = url
            courselist = list(enumerate(courselist))
            specs = []
            for course_name in courselist:
                specs.append(
                    Spec(
                        name=course_name,
                        course_id=course.id
                    )
                )
            db.session.add_all(specs)
        else:
            course.specstatus = False
            url, courselist = None, []
    db.session.commit()
    res = {
        "success": True,
        "obj": obj,
        "url": url,
        "courselist": courselist
    }
    return jsonify(res)