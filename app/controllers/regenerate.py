from flask import request, jsonify
from app.services.promptgen import promptGen
from app.services.responsegen import GetResponse

def regen():
    data = request.get_json()
    if not data or "payload" not in data or "boxNumber" not in data:
        return jsonify({"error": "Invalid request"}), 400
    p1, p2 = promptGen(data["payload"])
    prompts = {
        1: p1,
        2: p2
    }
    prompt = prompts.get(data["boxNumber"])
    if not prompt:
        return jsonify({"error": "Invalid boxNumber"}), 400
    newRes = GetResponse(prompt)
    return jsonify({"response": newRes})