import os
import time
import random
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENAI_KEY")

# Create OpenAI client
client = OpenAI(api_key=API_KEY)

def get_response(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-5.4-nano",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            if response.choices[0].message.content:
                return response.choices[0].message.content

            raise Exception("Empty response")

        except Exception as e:
            print("Error:", e)

            # Retry only for overload / rate limit
            if "429" in str(e) or "overloaded" in str(e).lower():
                wait = (2 ** attempt) + random.random()
                time.sleep(wait)
                continue

            return None

    return None


def GetResponse(prompt):
    result = get_response(prompt)
    if result:
        return result

    raise Exception("Service temporarily unavailable.")


if __name__ == "__main__":
    prompt = input("Enter the prompt: ")
    print(GetResponse(prompt))