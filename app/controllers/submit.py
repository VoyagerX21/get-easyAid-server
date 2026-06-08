from flask import request, jsonify
from app.utils.scrapepage import scrap

def submitReq():
    data = request.get_json()
    obj = data.get('obj')
    scrapped = scrap(obj['title'], obj['URL'])
    if scrapped:
        url, courselist = scrapped
        courselist = list(enumerate(courselist))
    else:
        url, courselist = None, []
    res = {
        "success": True,
        "obj": obj,
        "url": url,
        "courselist": courselist
    }
    return jsonify(res)