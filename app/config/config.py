import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI=f'mongodb+srv://VoyagerX21:{os.getenv('MONGO_PASS')}@cluster1.kw3xd3o.mongodb.net'
    INVOKE_URL='https://integrate.api.nvidia.com/v1/chat/completions'
    HEADERS={
        "Authorization": f"Bearer {os.getenv("KEY")}",
        "Content-Type": "application/json"
    }