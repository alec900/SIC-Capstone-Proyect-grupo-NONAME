from telebot.types import Message
from services.groq_service import groq_text_response

usuarios_saludados = set()

# Lista de palabras que se consideran saludo
SALUDOS = ["hola", "holaa", "buenas", "hey", "qué tal", "buen día", "buenas tardes", "buenas noches"]

def register_text(bot):

    @bot.message_handler(commands=["start"])
    def start(message: Message):
        user_id = message.from_user.id
        bot.send_message(
            message.chat.id,
            "👋 ¡Hola! Soy *Triviabot*, un bot dedicado exclusivamente al juego de trivia.\n"
            "Usá /trivia para comenzar el desafío 🧠 o enviame un audio y te lo transcribo 🎤",
            parse_mode="Markdown"
        )
        usuarios_saludados.add(user_id)  # Marca al usuario como presentado

    @bot.message_handler(func=lambda message: not message.text.startswith("/"), content_types=["text"])
    def handle_text(message: Message):
        texto = message.text.lower().strip()
        user_id = message.from_user.id

        # Detecta saludos
        if any(saludo in texto for saludo in SALUDOS):
            if user_id not in usuarios_saludados:
                usuarios_saludados.add(user_id)
                bot.send_message(
                    message.chat.id,
                    "👋 ¡Hola! Soy Triviabot, un bot dedicado exclusivamente al juego de trivia.\n"
                    "Escribí /trivia para comenzar a jugar 🎯"
                )
                return
            else:
                # Si ya se presentó, no repetir saludo
                return

        # Mensaje sobre trivia
        if "trivia" in texto:
            bot.send_message(message.chat.id, "¿Querés jugar una trivia? Escribí /trivia para comenzar 🎯")
            return

        # Todo lo demás pasa a la IA
        respuesta = groq_text_response(
            str(message.from_user.id),
            f"Sos Triviabot, un bot simpático de trivia. "
            f"Si alguien te habla de algo que no sea trivia, respondé amablemente que solo sabés de trivia, "
            f"pero con humor o simpatía. El usuario dijo: '{texto}'."
        )
        bot.send_message(message.chat.id, respuesta) 

        