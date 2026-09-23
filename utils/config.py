%%writefile AI-Roadmap-Generator/utils/config.py

import os
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)


MODEL = "openai/gpt-oss-120b"
