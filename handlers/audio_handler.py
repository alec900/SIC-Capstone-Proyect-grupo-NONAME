import os
from telebot.types import Message
from services.audio_service import transcribir_audio
from services.groq_service import groq_text_response
from handlers.trivia_handler import iniciar_trivia

def register_audio(bot):
    @bot.message_handler(content_types=["voice"])
    def handle_audio(message: Message):
        try:
            # Descargar archivo
            file_info = bot.get_file(message.voice.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            os.makedirs("temp", exist_ok=True)
            file_path = f"temp/audio_{message.from_user.id}.ogg"

            with open(file_path, "wb") as f:
                f.write(downloaded_file)

            # 1) Transcribir (no se lo mostramos al usuario)
            texto = transcribir_audio(file_path).strip().lower()

            # Si no se pudo transcribir nada
            if not texto:
                bot.send_message(message.chat.id, "No entendí el audio 🤔 ¿Me repetís?")
                os.remove(file_path)
                return

            # 2) Detectar si pidió jugar a la trivia
            if "trivia" in texto or "jugar" in texto:
                iniciar_trivia(bot, message)
                os.remove(file_path)
                return

            # 3) Pasar texto a la IA con historial
            respuesta = groq_text_response(message.from_user.id, texto)

            # 4) Responder normalmente
            bot.send_message(message.chat.id, respuesta)

            # 5) Borrar archivo temporal
            os.remove(file_path)

        except Exception as e:
            bot.send_message(message.chat.id, f"⚠️ Error al procesar tu audio: {e}")

