import os
import time
import random
from dotenv import load_dotenv
from google import genai

# Load environment
load_dotenv()

PRIMARY_KEY = os.getenv("OPENAI_KEY")
SECONDARY_KEY = os.getenv("OPENAI_KEY2")

def create_client(api_key):
    return genai.Client(api_key=api_key)

def get_response_with_key(prompt, api_key, max_retries=3):
    client = create_client(api_key)
    
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            if response.text:
                return response.text
            
            # if response exists but no text, treat as failure
            raise Exception("Empty response")

        except Exception as e:
            print(f"Error with key {api_key}:", e)

            # Retry only if overloaded
            if "503" in str(e) or "overloaded" in str(e).lower():
                wait = (2 ** attempt) + random.random()
                time.sleep(wait)
                continue

            # No overload → immediately fail
            return None

    return None


def GetResponse(prompt):
    # Try primary key
    result = get_response_with_key(prompt, PRIMARY_KEY)
    if result:
        return result

    print("⚠ Primary key failed. Trying secondary key...")

    # Try secondary key
    result = get_response_with_key(prompt, SECONDARY_KEY)
    if result:
        return result

    raise Exception("Service temporarily unavailable. Both keys failed.")


if __name__ == "__main__":
    prompt = input("Enter the prompt: ")
    print(GetResponse(prompt))
