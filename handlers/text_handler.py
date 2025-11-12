from telebot.types import Message
from services.groq_service import groq_text_response

def register_text(bot):

    @bot.message_handler(commands=["start"])
    def start(message: Message):
        bot.send_message(
            message.chat.id,
            "👋 ¡Hola! Soy *Triviabot*, un bot dedicado al juego de trivia.\n"
            "Usá /trivia para comenzar el desafío 🧠 o enviame un audio y te lo transcribo 🎤",
            parse_mode="Markdown"
        )

    @bot.message_handler(func=lambda message: not message.text.startswith("/"), content_types=["text"])
    def handle_text(message: Message):
        texto = message.text.lower()

        # Si el mensaje no tiene relación con trivia
        if "trivia" not in texto:
            respuesta = groq_text_response(
                f"Sos Triviabot, un bot simpático de trivia. "
                f"Si alguien te habla de algo que no sea trivia, respondé amablemente que solo sabés de trivia, "
                f"pero con humor o simpatía. El usuario dijo: '{texto}'."
            )
            bot.send_message(message.chat.id, respuesta)
        else:
            bot.send_message(message.chat.id, "¿Querés jugar una trivia? Escribí /trivia para comenzar 🎯") 