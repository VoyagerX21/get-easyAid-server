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
first = ". Using only the information provided above, write a personal and sincere financial aid request of 150–200 words in a single paragraph. Include the real details from the text (name, institute/organization, academic year or position, and previously completed courses) in a natural way. If any detail is missing, simply skip it and do not add placeholders like [Your Name] or [Course Title], and do not describe what information is missing. Avoid generic phrasing and template-sounding language such as 'this course is directly relevant to my objectives'. Write like a real person explaining their situation and financial need. Do not include explanations, meta comments, or instructions in the answer. Keep the tone neutral and factual without addressing me by name inside the answer. Write the answer in plain text, no bold or italics things."
second = ". Using only the information provided above, write a personalized 150–200 word explanation in one paragraph about how this course supports my career and academic goals. Include real details from the text (name, institute/organization, academic year or position, and previously completed courses) in a natural way. If any detail is missing, skip it silently rather than adding placeholders like [Your Position] or meta comments. Avoid generic or template phrasing such as 'this course is directly relevant to my objectives'. Focus on the real journey, learning progress, and why the course matters now. Do not include explanations about missing data or instructions for me. Keep a neutral, direct tone without addressing me by name inside the answer. Write the answer in plain text, no bold or italics things."

def personalisedDetails(data):
    def get_value(key, default=['']):
        value = data.get(key, default)
        return value[0] if isinstance(value, list) else value

    name = get_value('name')
    course = get_value('courseType')
    specialization = get_value('specialization')
    institute = get_value('institute')
    organization = get_value('organization')
    position = get_value('position')
    year = get_value('year')
    courses = data.get('courses', [])

    res = f"My name is {name}, and I am applying for financial aid for the course titled {course} on Coursera."

    if specialization:
        spec_name = specialization.split('/')[-1] if '/' in specialization else specialization
        res += f" The course is part of the specialization *{spec_name}*, which I actively pursue to strengthen my knowledge."

    if courses:
        if len(courses) > 1:
            res += f" I have already completed {len(courses)} courses in this specialization, including {', '.join(courses[:-1])}, and {courses[-1]}, which helped me develop a strong foundation."
        else:
            res += f" I have completed the course *{courses[0]}* under this specialization and it helped me develop an initial understanding."

    if institute:
        if year:
            res += f" I am currently studying at {institute} in my {year} year, and I am actively planning my academic path toward a clear career direction."
        else:
            res += f" I am currently studying at {institute} and working toward a clear academic and career direction."
    elif organization:
        if position:
            res += f" I am currently working at {organization} as a {position}, and I want to expand my skills for professional growth."
        else:
            res += f" I am currently working at {organization}, and I want to expand my skills for professional growth."

    res += " I am deeply motivated to learn, but managing the cost of the course is challenging for me at this stage. Access to financial aid will allow me to continue learning without interruption."

    return res

@app.get("/")
def getHome():
    return jsonify({"msg": "Server running at 5000"})

@app.get("/getAllCourses")
def getCourses():
    data = list(mycollection.find({}, {'_id': 0}))
    return jsonify(data)

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
    data = request.form.to_dict(flat=False)
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