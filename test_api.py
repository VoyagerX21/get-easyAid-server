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
    "stream": True,
    "chat_template_kwargs": {"enable_thinking": True},  # 🔴 disable reasoning noise
}

response = requests.post(invoke_url, headers=headers, json=payload, stream=True)

if response.status_code != 200:
    print("Error:", response.text)
    exit()

print("\nResponse:\n")
result = ""

for line in response.iter_lines():
    if not line:
        continue

    line = line.decode("utf-8")

    # Skip done signal
    if line.strip() == "data: [DONE]":
        break

    if line.startswith("data: "):
        try:
            data = json.loads(line[6:])  # remove "data: "
            delta = data["choices"][0]["delta"]

            # ✅ Only print actual content (ignore reasoning)
            if "content" in delta and delta["content"]:
                result += delta["content"]
                # print(delta["content"], end="", flush=True)

        except json.JSONDecodeError:
            continue

# print("\n")
print(result)