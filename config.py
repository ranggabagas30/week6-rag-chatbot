import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ["ANTHROPIC_API_KEY"]
BASE_URL = "http://localhost:20128"
MODEL = "combo1"
