import requests
import json

invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
stream = True

headers = {
    "Authorization": "Bearer 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",
    "Accept": "text/event-stream"
}

payload = {
    "model": "qwen/qwen3.5-122b-a10b",
    "messages": [{"role": "user", "content": "current PM on INDIA?"}],
    "max_tokens": 1024,
    "temperature": 0.6,
    "top_p": 0.95,
    "chat_template_kwargs": {"enable_thinking": True},  # 🔴 disable reasoning noise
}

response = requests.post(invoke_url, headers=headers, json=payload, stream=True)
# print(response.text)
# if response.status_code != 200:
#     raise Exception(f"{response.status_code} - {response.text}")

# result = ""

# for line in response.iter_lines():
#     if not line:
#         continue

#     line = line.decode("utf-8")

#     # stop stream
#     if line.strip() == "data: [DONE]":
#         break

#     if line.startswith("data: "):
#         try:
#             data = json.loads(line[6:])

#             choice = data["choices"][0]
#             # NEW FORMAT
#             if "message" in choice:
#                 message = choice["message"]

#                 if "content" in message and message["content"]:
#                     result += message["content"]

#                 if "reasoning_content" in message and message["reasoning_content"]:
#                     reasoning += message["reasoning_content"]

#             # OLD STREAMING FORMAT (fallback)
#             elif "delta" in choice:
#                 delta = choice["delta"]

#                 if "content" in delta and delta["content"]:
#                     result += delta["content"]

#         except json.JSONDecodeError:
#             continue
if response.status_code != 200:
    raise Exception(f"{response.status_code} - {response.text}")

data = response.json()

message = data["choices"][0]["message"]

content = message.get("content", "")
reasoning = message.get("reasoning_content", "")
# print("\n")
print(reasoning)