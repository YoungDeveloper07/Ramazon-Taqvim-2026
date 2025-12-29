import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

# Tokenni o'zgaruvchiga olish
BOT_TOKEN = os.getenv("BOT_TOKEN")
