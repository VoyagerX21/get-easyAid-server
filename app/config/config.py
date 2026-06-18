import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    INVOKE_URL='https://integrate.api.nvidia.com/v1/chat/completions'
    HEADERS={
        "Authorization": f"Bearer {os.getenv("KEY")}",
        "Content-Type": "application/json"
    }
    SQLALCHEMY_DATABASE_URI=os.getenv("SQLITE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL="redis://localhost:6379/0"
    CELERY_RESULT_BACKEND="redis://localhost:6379/0"