import os
from dotenv import load_dotenv

load_dotenv()

TINKOFF_TOKEN = os.getenv("TINKOFF_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
