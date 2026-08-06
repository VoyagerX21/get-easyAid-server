import time
import random
from google import genai
from app.config.config import Config

client = genai.Client(api_key=Config.GEMINI_API_KEY)

def get_response(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            return response.text
        except Exception as e:
            if "429" in str(e):
                wait = (2 ** attempt) + random.random()
                time.sleep(wait)
                continue
            print(f"Gemini Error: {e}")
            return None
    return None

def GetResponse(prompt):
    result = get_response(prompt)
    if result:
        return result
    raise Exception("Service temporarily unavailable.")