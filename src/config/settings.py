from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")