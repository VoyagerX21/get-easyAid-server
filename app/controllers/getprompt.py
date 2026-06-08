from flask import request, jsonify
from app.services.promptgen import promptGen
from app.services.responsegen import GetResponse

def prompt():
    data = request.get_json()
    p1, p2 = promptGen(data)
    try:
        return jsonify({
            "success": True,
            "firstRes": GetResponse(p1),
            "secondRes" : GetResponse(p2)
        })
    except Exception as e:
        if "503" in str(e) or "overloaded" in str(e):
            return jsonify({
                "success": False,
                "statusCode": 503,
                "title": "Service Temporarily Unavailable",
                "desc": "Our AI service is currently experiencing high traffic. Please try again in a few moments.",
                "btn": "Retry"
            })
        else:
            return jsonify({
                "success": False,
                "statusCode": 500,
                "title": "Internal Server Error",
                "desc": "Something went wrong. Please try again later.",
                "btn": "Try Again"
            })