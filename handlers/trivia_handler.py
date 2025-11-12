from telebot.types import Message
from services.trivia_service import obtener_pregunta, verificar_respuesta

# Estado simple en memoria
usuario_estado = {}

def register_trivia(bot):

    @bot.message_handler(commands=["trivia"])
    def start_trivia(message: Message):
        user_id = message.from_user.id
        pregunta = obtener_pregunta(user_id)  # Pasamos el user_id
        usuario_estado[user_id] = pregunta
        bot.send_message(user_id, "¡Arranca la trivia! 🎮")
        bot.send_message(user_id, "Pregunta: " + pregunta["pregunta"])
    
    @bot.message_handler(func=lambda m: True, content_types=["text"])
    def handle_text(message: Message):
        user_id = message.from_user.id
        texto = message.text.strip().lower()

        if user_id in usuario_estado:
            pregunta_obj = usuario_estado[user_id]

            if verificar_respuesta(pregunta_obj, texto):
                bot.send_message(user_id, "✅ ¡Correcto! Vamos con otra...")
            else:
                bot.send_message(user_id, f"❌ Incorrecto. La respuesta era: {pregunta_obj['respuesta']}")

            # Nueva pregunta
            nueva = obtener_pregunta(user_id)
            usuario_estado[user_id] = nueva
            bot.send_message(user_id, "Pregunta: " + nueva["pregunta"])
            return

        # Mensaje que no es parte de la trivia
        bot.send_message(user_id, "Soy un bot de trivia 🤖. Escribí /trivia para comenzar.")


        from services.trivia_service import obtener_pregunta, verificar_respuesta

def register_trivia(bot):
    """
    Aquí podrías agregar handlers extra relacionados con la trivia
    si querés separar de text_handler.
    Por ahora solo devolvemos la función para importar desde main.py
    """
    pass 

