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
    API_TITLE='Get-EasyAid'
    API_VERSION="v3"
    OPENAPI_VERSION="3.0.3"
    OPENAPI_URL_PREFIX="/"
    OPENAPI_SWAGGER_UI_PATH="/docs"
    OPENAPI_SWAGGER_UI_URL="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"