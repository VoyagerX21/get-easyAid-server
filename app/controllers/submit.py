from flask import jsonify
from app.utils.scrapepage import scrap
from app.extensions import db
from app.models.courses import Course
from app.models.specs import Spec

def submitReq(data):
    obj = data.get('obj')
    course = Course.query.filter_by(title=obj["title"], url=obj["URL"]).first()

    if course.seenStatus:
        if course.specstatus:
            courselist = []
            url = course.specurl
            ptr = 0
            for i in course.speclist:
                courselist.append([ptr, i.name])
                ptr+=1
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
                        name=course_name[1],
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