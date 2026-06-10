from flask import request, jsonify
from app.models.courses import Course

def searchCourse():
    query = request.args.get("query", "").strip()

    if not query:
        return jsonify({"success": True, "results": []})

    courses = Course.query.filter(
        (Course.title.ilike(f"%{query}%")) |
        (Course.org.ilike(f"%{query}%"))
    ).all()

    results = [course.to_dict() for course in courses]

    return jsonify({
        "success": True,
        "results": results
    })