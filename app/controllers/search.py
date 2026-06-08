from flask import request, jsonify
from app.extensions import db

mycollection = db["courses"]

def searchCourse():
    query = request.args.get("query")
    if not query:
        return jsonify({"success": True, "results": []})
    search_filter = {
        "$or": [
            {"title": { "$regex": query, "$options": "i" }},
            {"Organization": {"$regex": query, "$options": "i"}}
        ]
    }
    results = list(mycollection.find(search_filter, {"_id": 0}))
    return jsonify({"success": True, "results": results})