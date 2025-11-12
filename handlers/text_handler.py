from telebot.types import Message
from services.trivia_service import obtener_pregunta, verificar_respuesta

usuario_estado = {}

def register_text(bot):

    @bot.message_handler(commands=["trivia"])
    def start_trivia(message: Message):
        uid = message.from_user.id
        pregunta = obtener_pregunta(uid)
        usuario_estado[uid] = pregunta
        bot.send_message(uid, "¡Arranca la trivia! 🎮")
        bot.send_message(uid, "Pregunta: " + pregunta["pregunta"])
    
    @bot.message_handler(func=lambda m: True, content_types=["text"])
    def handle_text(message: Message):
        uid = message.from_user.id
        texto = message.text.strip().lower()
        if uid in usuario_estado:
            pregunta_obj = usuario_estado[uid]
            if verificar_respuesta(pregunta_obj, texto):
                bot.send_message(uid, "✅ ¡Correcto! Vamos con otra...")
            else:
                bot.send_message(uid, f"❌ Incorrecto. La respuesta era: {pregunta_obj['respuesta']}")
            nueva = obtener_pregunta(uid)
            usuario_estado[uid] = nueva
            bot.send_message(uid, "Pregunta: " + nueva["pregunta"])
            return
        bot.send_message(uid, "Soy un bot de trivia 🤖. Escribí /trivia para comenzar.")