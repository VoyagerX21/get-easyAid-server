from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("OPENAI_KEY")
client = genai.Client(api_key=token)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="current president of india"
)
print(response.text)