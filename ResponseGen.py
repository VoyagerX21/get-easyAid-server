import os
import time
import random
from dotenv import load_dotenv
import requests
import json

load_dotenv()

KEY = os.getenv("KEY")

def get_response(prompt, max_retries=3):
    for _ in range(max_retries):
        try:
            invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {KEY}",
                "Accept": "text/event-stream"
            }
            payload = {
                "model": "qwen/qwen3.5-122b-a10b",
                "messages": [{"role": "user", "content": f"{prompt}"}],
                "max_tokens": 1024,
                "temperature": 0.6,
                "top_p": 0.95,
                "stream": True,
                "chat_template_kwargs": {"enable_thinking": False},  # 🔴 disable reasoning noise
            }
            response = requests.post(invoke_url, headers=headers, json=payload, stream=True)
            if response.status_code != 200:
                raise Exception(f"{response.status_code} - {response.text}")
            result = ""
            for line in response.iter_lines():
                if not line:
                    continue
                line = line.decode("utf-8")
                if line.strip() == "data: [DONE]":
                    break
                if line.startswith("data: "):
                    try:
                        data = json.loads(line[6:])
                        delta = data["choices"][0]["delta"]
                        if "content" in delta and delta["content"]:
                            result += delta["content"]
                    except json.JSONDecodeError:
                        continue
            return result
        except Exception as e:
            print("Error:", e)
            if "429" in str(e) or "quota" in str(e).lower():
                wait = (2 ** _) + random.random()
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