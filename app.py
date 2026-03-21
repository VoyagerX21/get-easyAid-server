from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
from ScrapPage import scrap
from ResponseGen import GetResponse
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
load_dotenv()
client = MongoClient(f"mongodb+srv://VoyagerX21:{os.getenv('MONGO_PASS')}@cluster1.kw3xd3o.mongodb.net")
db = client["easyAid"]
mycollection = db["courses"]

global d
first = """. Using only the information provided above, write a personal and sincere financial aid request of 150–200 words in a single paragraph. Include the real details from the text (name, institute/organization, academic year or position, and previously completed courses) in a natural way. If any detail is missing, simply skip it and do not add placeholders like [Your Name] or [Course Title], and do not describe what information is missing. Avoid generic phrasing and template-sounding language such as 'this course is directly relevant to my objectives'. Write like a real person explaining their situation and financial need. Do not include explanations, meta comments, or instructions in the answer. Keep the tone neutral and factual without addressing me by name inside the answer. Write the answer in plain text, no bold or italics things. You are writing a financial aid application for a Coursera course.

You MUST use the provided user details naturally in the paragraph.

Task:
Write a sincere financial aid request in 150–180 words in ONE paragraph.

Rules:
- Use real user details naturally
- Do NOT use generic template phrases
- Do NOT mention missing info
- Do NOT add placeholders
- Plain text only """
second = """. Using only the information provided above, write a personalized 150–200 word explanation in one paragraph about how this course supports my career and academic goals. Include real details from the text (name, institute/organization, academic year or position, and previously completed courses) in a natural way. If any detail is missing, skip it silently rather than adding placeholders like [Your Position] or meta comments. Avoid generic or template phrasing such as 'this course is directly relevant to my objectives'. Focus on the real journey, learning progress, and why the course matters now. Do not include explanations about missing data or instructions for me. Keep a neutral, direct tone without addressing me by name inside the answer. Write the answer in plain text, no bold or italics things.
You are writing a career and academic goals explanation for a Coursera financial aid application.

You MUST use the provided user details naturally.

Task:
Write a personalized explanation in 150–180 words in ONE paragraph explaining how this course supports career and academic growth.

Rules:
- Use real user details naturally
- Avoid generic phrasing
- No placeholders
- Plain text only"""

def personalisedDetails(data):
    def get_value(key):
        value = data.get(key, "")
        if isinstance(value, list):
            return value[0].strip() if value else ""
        return str(value).strip()
    name = get_value("name")
    course = get_value("courseType")
    specialization = get_value("specialization")
    institute = get_value("institute")
    organization = get_value("organization")
    position = get_value("position")
    year = get_value("year")

    courses = data.get("courses", [])
    if isinstance(courses, list):
        courses = ", ".join(courses)

    if specialization and "/" in specialization:
        specialization = specialization.split("/")[-1]

    fields = []

    if name:
        fields.append(f"Name: {name}")

    if institute:
        fields.append(f"Institute: {institute}")

    if year:
        fields.append(f"Academic Year: {year}")

    if organization:
        fields.append(f"Organization: {organization}")

    if position:
        fields.append(f"Position: {position}")

    if courses:
        fields.append(f"Completed Courses: {courses}")

    if specialization:
        fields.append(f"Specialization: {specialization}")

    if course:
        fields.append(f"Course Applying For: {course}")

    structured = "User Details:\n" + "\n".join(fields)

    return structured

@app.get("/")
def getHome():
    return jsonify({"msg": "Server running"})

@app.get("/getAllCourses")
def getCourses():
    data = list(mycollection.find({}, {'_id': 0}))
    return jsonify(data)

@app.get("/search")
def search():
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

@app.post("/submit")
def submit():
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

@app.post("/GetPrompt")
def getprompt():
    global d
    data = request.get_json()
    d = personalisedDetails(data)
    p1 = personalisedDetails(data)+first
    p2 = personalisedDetails(data)+second
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

@app.post("/regenerate")
def regen():
    global d
    data = request.get_json()
    if data['boxNumber'] == 1:
        newRes = GetResponse(d+first)
    else:
        newRes = GetResponse(d+second)

    return jsonify({"response": newRes})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
