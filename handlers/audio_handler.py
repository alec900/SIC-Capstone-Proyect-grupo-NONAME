from telebot.types import Message
from services.audio_service import transcribir_audio
from services.trivia_service import verificar_respuesta, obtener_pregunta
from handlers.text_handler import usuario_estado

def register_audio(bot):

    @bot.message_handler(content_types=["voice"])
    def audio(message: Message):
        uid = message.from_user.id

        file_info = bot.get_file(message.voice.file_id)
        file = bot.download_file(file_info.file_path)

        texto = transcribir_audio(file)
        if not texto:
            bot.send_message(uid, "No pude transcribir ese audio 😢")
            return

        # Si está en trivia
        if uid in usuario_estado:
            pregunta_obj = usuario_estado[uid]
            if verificar_respuesta(pregunta_obj, texto):
                bot.send_message(uid, "✅ ¡Correcto, capo!")
            else:
                bot.send_message(uid, f"❌ Incorrecto. La respuesta era: {pregunta_obj['respuesta']}")
            nueva = obtener_pregunta()
            usuario_estado[uid] = nueva
            bot.send_message(uid, "Pregunta: " + nueva["pregunta"])
        else:
            bot.send_message(uid, "Soy un bot de trivia, solo puedo hacer preguntas y corregirte 😎") 