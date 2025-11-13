from telebot.types import Message
from services.audio_service import transcribir_audio
from services.groq_service import groq_text_response
import os

def register_audio(bot):

    @bot.message_handler(content_types=["voice"])
    def handle_voice(message: Message):
        try:
            # Descargar el audio a un archivo temporal
            file_info = bot.get_file(message.voice.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            temp_path = os.path.join("temp.ogg")  # ruta temporal
            with open(temp_path, "wb") as f:
                f.write(downloaded_file)

            # Transcribir audio usando la ruta del archivo
            texto = transcribir_audio(temp_path)

            # Mandar el texto a la IA y obtener respuesta
            respuesta = groq_text_response(
                f"Eres Triviabot, un bot de trivia. "
                f"El usuario dijo: '{texto}'. "
                f"Responde solo con información relacionada con trivia o tu rol de bot de trivia."
            )

            # Enviar la respuesta de la IA directamente
            bot.send_message(message.chat.id, respuesta)

            # Eliminar archivo temporal
            os.remove(temp_path)

        except Exception as e:
            bot.send_message(message.chat.id, f"⚠️ Error al procesar tu audio: {e}") 
