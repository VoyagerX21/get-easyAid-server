import os
import time
import random
from dotenv import load_dotenv
from google import genai

# Load environment
load_dotenv()

token = os.getenv("OPENAI_KEY")  # use a clear variable name
client = genai.Client(api_key=token)

def GetResponse(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text  # direct text access

        except Exception as e:
            print("Error:", e)

            # Retry only if overloaded
            if "503" in str(e) or "overloaded" in str(e).lower():
                wait = (2 ** attempt) + random.random()
                time.sleep(wait)
                continue

            raise e

    raise Exception("Service temporarily unavailable. Please try again")

if __name__ == "__main__":
    prompt = input("Enter the prompt: ")
    print(GetResponse(prompt))
