from telebot.types import Message
from services.audio_service import transcribir_audio

def register_audio(bot):

    @bot.message_handler(content_types=["voice"])
    def handle_audio(message: Message):
        bot.send_message(message.chat.id, "🎧 Procesando tu audio, dame un momento...")

        try:
            text = transcribir_audio(message)
            bot.send_message(message.chat.id, f"🗣️ Transcripción: {text}")
        except Exception as e:
            bot.send_message(message.chat.id, f"❌ Error al transcribir el audio: {e}")