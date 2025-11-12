import os
from telebot import TeleBot

# Handlers
from handlers.text_handler import register_text
from handlers.audio_handler import register_audio
from handlers.trivia_handler import register_trivia

# Opcional: intentar cargar .env
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(r"C:\Users\AlexZ\OneDrive\Escritorio\SIC\.env")
load_dotenv(dotenv_path)

# Variables de entorno, con fallback directo si .env falla
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN") or "8382707119:AAGmEJLOxtzkRUBKrgiHEdEO9J5XzNg75B0"
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or "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"

# Debug: mostrar si se cargaron
print("TOKEN:", TELEGRAM_TOKEN)
print("GROQ:", GROQ_API_KEY)

# Crear el bot
bot = TeleBot(TELEGRAM_TOKEN)

# Validar
if not TELEGRAM_TOKEN:
    raise ValueError("No se cargó el token de Telegram")
if not GROQ_API_KEY:
    raise ValueError("No se cargó la API Key de Groq")

# Registrar handlers
register_text(bot)
register_audio(bot)
register_trivia(bot)

print("✅ Handlers cargados correctamente")

if __name__ == "__main__":
    print("✅ Bot iniciado...")
    bot.infinity_polling()