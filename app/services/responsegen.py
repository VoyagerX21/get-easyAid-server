import time
import random
import requests
from app.config.config import Config

def get_response(prompt, max_retries=3):
    for _ in range(max_retries):
        try:
            invoke_url = Config.INVOKE_URL
            headers = Config.HEADERS
            payload = {
                "model": "qwen/qwen3.5-122b-a10b",
                "messages": [{"role": "user", "content": f"{prompt}"}],
                "max_tokens": 400,
                "temperature": 0.6,
                "top_p": 0.95,
                "chat_template_kwargs": {"enable_thinking": False},  # 🔴 disable reasoning noise
            }
            start=time.perf_counter()
            response = requests.post(invoke_url, headers=headers, json=payload, timeout=120)
            print(f"Request took {time.perf_counter()-start:.2f}s")
            if response.status_code != 200:
                raise Exception(f"{response.status_code} - {response.text}")
            data = response.json()
            message = data["choices"][0]["message"]
            result = message.get("content", "")
            return result
        except Exception as e:
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